import graphene

from colleges.models import CollegeStatus
from django.conf import settings
from financial_aid.models import AidCategory, AidFinalData, AidRawData, DocumentError, DocumentResult
from graphene_django import DjangoObjectType
from services.aws.lambda_handler import lambda_handler
from services.aws.textract import (
    get_table_data,
    get_text_data,
    start_table_analysis,
    start_text_analysis
)
from services.helpers.check_aid_raw_data import check_aid_raw_data
from services.helpers.parse_aid_letters import (
    compare_tables_and_text,
    parse_data
)
from services.sendgrid.send_email import send_notification_email, send_report_email
from services.slack.send_message import (
    send_award_letter_uploaded_notification,
    send_award_letter_reviewed_notification
)


################################################################################
# Standard Model Definitions
################################################################################
class AidCategoryType(DjangoObjectType):
    class Meta:
        model = AidCategory
        fields = ('id', 'name', 'primary', 'secondary', 'tertiary')

class AidFinalDataType(DjangoObjectType):
    class Meta:
        model = AidFinalData
        fields = ('id', 'aid_category', 'amount', 'college_status', 'name')


################################################################################
# Query
################################################################################

class Query(graphene.ObjectType):
    aid_categories = graphene.List(AidCategoryType, limit=graphene.Int())
    aid_final_data = graphene.List(AidFinalDataType, limit=graphene.Int())

    aid_categories_by_fields = graphene.List(
        AidCategoryType,
        name=graphene.String(),
        primary=graphene.String(),
        secondary=graphene.String(),
        tertiary=graphene.String()
    )
    aid_final_data_by_college_status = graphene.List(
        AidFinalDataType,
        college_status_id=graphene.Int()
    )
    aid_final_data_by_fields = graphene.List(
        AidFinalDataType,
        aid_category_id=graphene.Int(),
        amount=graphene.Int(),
        col_index=graphene.Int(),
        college_status_id=graphene.Int(),
        name=graphene.String(),
        table_number=graphene.Int(),
        row_index=graphene.Int(),
    )
    my_aid_final_data = graphene.List(AidFinalDataType)

    # get_all()
    def resolve_aid_categories(self, info, limit=None):
        qs = AidCategory.objects.all()[0:limit]
        return qs

    def resolve_aid_final_data(self, info, limit=None):
        qs = AidFinalData.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_aid_categories_by_fields(self, info, **kwargs):
        qs = AidCategory.objects.filter(**kwargs)
        return qs

    def resolve_aid_final_data_by_college_status(self, info, college_status_id=None):
        qs = AidFinalData.objects.filter(college_status__id=college_status_id)
        return qs

    def resolve_aid_final_data_by_fields(self, info, **kwargs):
        qs = AidFinalData.objects.filter(**kwargs)
        return qs

    def resolve_my_aid_final_data(self, info):
        user = info.context.user
        qs = AidFinalData.objects.filter(college_status__user__id=user.id)
        return qs


################################################################################
# Mutations
################################################################################
# Send documents to be analyzed by Textract
# Only send documents that apply to the same college_status
class SendDocuments(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        college_status_id = graphene.Int()
        documents = graphene.List(graphene.String)

    def mutate(self, info, college_status_id, documents):
        user = info.context.user
        table_job_ids = []
        text_job_ids = []

        for document_name in documents:
            college_status = CollegeStatus.objects.get(pk=college_status_id)

            # send document for analysis
            table_job_id = start_table_analysis(document_name)
            text_job_id = start_text_analysis(document_name)

            # save job_ids to database
            document_result = DocumentResult.objects.create(
                college_status=college_status,
                document_name=document_name,
                sent=True,
                table_job_id=table_job_id,
                text_job_id=text_job_id,
            )
            document_result.save()

            college_status.status = "accepted"
            college_status.award_status = "uploaded"
            college_status.save()

            table_job_ids.append(table_job_id)
            text_job_ids.append(text_job_id)


        # triggers lambda function to wait for results
        lambda_handler(
            documents=documents,
            graphql_endpoint=settings.GRAPHQL_ENDPOINT,
            table_job_ids=table_job_ids,
            text_job_ids=text_job_ids
        )

        # triggers slack channel message
        send_award_letter_uploaded_notification(
            channel=settings.SLACK_AWARD_CHANNEL,
            documents=documents,
            graphql_endpoint=settings.GRAPHQL_ENDPOINT,
            table_job_ids=table_job_ids,
            text_job_ids=text_job_ids
        )


        return SendDocuments(success=True)

# Only send documents that apply to the same college_status
class ParseDocuments(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        documents = graphene.List(graphene.String)

    def mutate(self, info, documents):
        # before running any analysis, delete aid data for this college status
        first_document = documents[0]
        first_document_result = DocumentResult.objects.get(document_name=first_document)
        aid_raw_data = AidRawData.objects.filter(college_status=first_document_result.college_status)
        if aid_raw_data.exists():
            aid_raw_data.delete()
            AidFinalData.objects.filter(college_status=first_document_result.college_status).delete()

        # then go through the documents
        sendgrid_documents = []

        for document in documents:
            errors = []
            document_result = DocumentResult.objects.get(document_name=document)
            college_status = document_result.college_status
            user = college_status.user
            college = college_status.college

            # delete any document errors
            DocumentError.objects.filter(document_result=document_result).delete()

            # check if text processed
            text, text_errors = get_text_data(document_result.text_job_id)
            document_result.text_data = text
            if not text_errors:
                document_result.text_succeeded = True
            else:
                document_result.text_succeeded = False
                for error in text_errors:
                    errors.append(error)

            # check if tables are processed
            tables, table_errors = get_table_data(document_result.table_job_id)
            document_result.table_data = tables

            if not table_errors:
                document_result.table_succeeded = True
            else:
                document_result.table_succeeded = False
                for error in table_errors:
                    errors.append(error)

            # if textract analysis fails save the data
            if not document_result.text_succeeded or not document_result.table_succeeded:
                for error in errors:
                    DocumentError.objects.create(
                        document_result=document_result,
                        type=error["type"],
                        message=error["message"]
                    )

            # if document has words and tables
            else:
                comparison = compare_tables_and_text(tables=tables, text=text)

                document_result.comparison_missing_amounts = comparison["comparison_missing_amounts"]
                document_result.comparison_missing_num = comparison["comparison_missing_num"]

                if comparison["comparison_succeeded"] is False:
                    errors.append({
                        "type": "Comparison between text and tables failed",
                        "message":
                            f"There are {document_result.comparison_missing_num} " \
                            "more dollar amounts in text. Those amounts include " \
                            f"{document_result.comparison_missing_amounts}."
                    })

                aid_raw_data, parse_errors = parse_data(tables=tables)
                if parse_errors:
                    for error in parse_errors:
                        errors.append(error)

                if aid_raw_data:
                    for aid in aid_raw_data:
                        AidRawData.objects.create(
                            college_status=document_result.college_status,
                            document_result=document_result,
                            aid_category=AidCategory.objects.get(name=aid["aid_category"]),
                            name=aid["name"],
                            amount=aid["amount"],
                            table_num=aid["table_num"],
                            row_num=aid["row_num"],
                            row_text=aid["row_text"]
                        )


                if not errors:
                    document_result.automated_review_succeeded = True

                    # automatically change award status to reviewed
                    # college_status.award_status = "reviewed"

                else:
                    document_result.automated_review_succeeded = False
                    for error in errors:
                        DocumentError.objects.create(
                            document_result=document_result,
                            type=error["type"],
                            message=error["message"]
                        )

            # create report_data for sendgrid
            sendgrid_document = {
                "document_name": document_result.document_name,
                "sent": document_result.sent,
                "table_succeeded": document_result.table_succeeded,
                "text_succeeded": document_result.text_succeeded,
                "automated_review_succeeded": document_result.automated_review_succeeded,
                "errors": errors,
                "aid_data": aid_raw_data
            }
            sendgrid_documents.append(sendgrid_document)
            document_result.save()

        # check data after all documents have been processed
        final_aid_raw_data = AidRawData.objects.filter(college_status=college_status)
        aid_categories = AidCategory.objects.all()
        final_check_errors = check_aid_raw_data(aid_data=final_aid_raw_data, aid_categories=aid_categories)

        # triggers Slack channel message
        send_award_letter_reviewed_notification(
            channel=settings.SLACK_AWARD_CHANNEL,
            college_name=college.name,
            college_status_id=college_status.pk,
            documents=sendgrid_documents,
            final_check_errors=final_check_errors,
            user_email=user.email
        )

        return ParseDocuments(success=True)


class Mutation(graphene.ObjectType):
    parse_documents = ParseDocuments.Field()
    send_documents = SendDocuments.Field()
