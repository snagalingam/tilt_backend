import graphene
import json
import os
import time

from financial_aid.models import AidCategory, AidData, DocumentResult
from colleges.models import CollegeStatus
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from services.amazon_textract.check_document import start_document_check
from services.amazon_textract.get_words import get_words_data, start_words_analysis
from services.amazon_textract.get_tables import get_table_data, start_tables_analysis
from services.amazon_textract.lambda_handler import lambda_handler
from services.amazon_textract.parse_data import filter_possibilities, find_aid_category, get_aid_data
from services.amazon_textract.s3_methods import upload_document, delete_document
from services.sendgrid_api.send_email import send_notification_email, send_report_email


################################################
# Standard Model Definitions
################################################
class AidCategoryType(DjangoObjectType):
    class Meta:
        model = AidCategory
        fields = ('id', 'name', 'primary', 'secondary', 'tertiary')


class AidDataType(DjangoObjectType):
    class Meta:
        model = AidData
        fields = ('id', 'aid_category', 'amount', 'college_status', 'name')


################################################
# Query
################################################

class Query(graphene.ObjectType):
    aid_categories = graphene.List(AidCategoryType, limit=graphene.Int())
    aid_data = graphene.List(AidDataType, limit=graphene.Int())

    aid_categories_by_fields = graphene.List(
        AidCategoryType,
        name=graphene.String(),
        primary=graphene.String(),
        secondary=graphene.String(),
        tertiary=graphene.String()
    )
    aid_data_by_college_status = graphene.List(
        AidDataType,
        college_status_id=graphene.Int()
    )
    aid_data_by_fields = graphene.List(
        AidDataType,
        aid_category_id=graphene.Int(),
        amount=graphene.Int(),
        col_index=graphene.Int(),
        college_status_id=graphene.Int(),
        name=graphene.String(),
        table_number=graphene.Int(),
        row_index=graphene.Int(),
    )
    my_aid_data = graphene.List(AidDataType)

    # get_all()
    def resolve_aid_categories(self, info, limit=None):
        qs = AidCategory.objects.all()[0:limit]
        return qs

    def resolve_aid_data(self, info, limit=None):
        qs = AidData.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_aid_categories_by_fields(self, info, **kwargs):
        qs = AidCategory.objects.filter(**kwargs)
        return qs

    def resolve_aid_data_by_college_status(self, info, college_status_id=None):
        qs = AidData.objects.filter(college_status__id=college_status_id)
        return qs

    def resolve_aid_data_by_fields(self, info, **kwargs):
        qs = AidData.objects.filter(**kwargs)
        return qs

    def resolve_my_aid_data(self, info):
        user = info.context.user
        qs = AidData.objects.filter(college_status__user__id=user.id)
        return qs


################################################
# Mutations
################################################
class AnalyzeDocuments(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        college_status_id = graphene.Int()
        documents = graphene.List(graphene.String)

    def mutate(self, info, college_status_id, documents):
        sent_list = []
        user = info.context.user

        for document_name in documents:
            # find college_status
            college_status = CollegeStatus.objects.get(pk=college_status_id)

            # send document for analysis
            words_id = start_words_analysis(document_name)
            tables_id = start_tables_analysis(document_name)

            # save job_ids to database
            document_result = DocumentResult.objects.create(
                document_name=document_name,
                words_id=words_id,
                tables_id=tables_id,
                sent=True
            )
            document_result.save()

        # trigger lambda to checkDocuments after 5 minutes
        lambda_handler(documents)
        return AnalyzeDocuments(success=True)


class CheckDocuments(graphene.Mutation):
    aid_data_list = graphene.List(AidDataType)

    class Arguments:
        documents = graphene.List(graphene.String)

    def mutate(self, info, documents=None):
        check = None
        pos_error = None
        pass_fail = None
        errors = []
        collection = []
        aid_data_report = []
        words_failed = None
        tables_failed = None
        pos_error = None
        next_college_status_id = None
        last_index = len(documents) - 1
        checked_list = []
        aid_data_list = []

        # interate through list
        for document_name in documents:
            document_result = DocumentResult.objects.get(document_name=document_name)

            # check if text processed
            try:
                text = get_text_data(document_result.text_job_id)
                document_result.text_succeeded = True
            except:
                document_result.text_succeeded = False

            # check if tables are processed
            try:
                tables = get_table_data(document_result.tables_id)
                document_result.table_succeeded = True
            except:
                document_result.table_succeeded = False

            # if textract analysis fails save the data
            if not document_result.text_succeeded or not document_result.table_succeeded:
                document_result.save()

            # if document has words and tables
            elif document_result.text_succeeded and document_result.table_succeeded:
                check = start_document_check(text, tables)

                if check["pass_fail"] == "Failed":
                    checked_list.append(
                        CheckedResultType(
                            document_name=document_name,
                            words="Passed",
                            tables="Passed",
                            pass_fail="Failed",
                            processed=True
                        ))
                else:
                    checked_list.append(
                        CheckedResultType(
                            document_name=document_name,
                            words="Passed",
                            tables="Passed",
                            pass_fail="Passed",
                            processed=True
                        ))

                # aid_data from 'parse_data.py' scripts
                pos = get_aid_data(tables, document_name)
                pos_error = pos.get("Document Error", None)

                if not pos_error:
                    for key in pos.keys():
                        table_number = int(key[6:])

                        for each in pos[key]:
                            aid_data_name = each.get("Name")
                            amount = each.get("Amount")
                            row_index = each.get("Row Index")
                            col_index = each.get("Col Index")
                            row_data = each.get("Row Data")

                            # get college_status_id from document
                            college_status = CollegeStatus.objects.get(
                                pk=college_status_id)

                            # auto award_reviewed=True if check passed and pos_error=False
                            if check["pass_fail"] == "Passed":
                                college_status.award_reviewed = True
                                college_status.save()

                            # filter/match for category
                            possibilities = find_aid_category(
                                aid_data_name, document_name)
                            category_name = filter_possibilities(possibilities)
                            aid_category = AidCategory.objects.get(
                                name=category_name)

                            # check for dups
                            try:
                                aid_data = AidData.objects.get(
                                    name=aid_data_name,
                                    amount=amount,
                                    table_number=table_number,
                                    row_index=row_index,
                                    col_index=col_index,
                                    row_data=row_data,
                                    college_status=college_status,
                                    aid_category=aid_category)
                            except:
                                aid_data = None

                            # create AidDate if no dups
                            if aid_data is None:
                                aid_data = AidData(
                                    name=aid_data_name,
                                    amount=amount,
                                    table_number=table_number,
                                    row_index=row_index,
                                    col_index=col_index,
                                    row_data=row_data,
                                    college_status=college_status,
                                    aid_category=aid_category
                                )
                                aid_data.save()

                            # for return results
                            aid_data_list.append(aid_data)

                            # for email report
                            aid_data_report.append({
                                "college_status": college_status_id,
                                "aid_category": aid_category.name,
                                "name": aid_data_name,
                                "amount": amount,
                                "table_number": table_number,
                                "row_index": row_index,
                                "col_index": col_index,
                                "row_data": row_data
                            })

                # check if document_data exists
                try:
                    document_data = DocumentData.objects.get(
                        document_name=document_name)
                except:
                    document_data = None

                # else create new document_data
                if document_data is None:
                    document_data = DocumentData(
                        document_name=document_name,
                        words=words,
                        tables=tables)
                    document_data.save()

            # if no error in document_check
            if check is not None:
                # update and save document_result results on each document
                pass_fail = check.get("pass_fail", "")
                number_of_missing = check.get("number_of_missing", "")
                missing_amounts = check.get("missing_amounts", "")
                document_result.pass_fail = pass_fail
                document_result.number_of_missing = number_of_missing
                document_result.missing_amounts = missing_amounts
            document_result.save()

            # handle errors
            if pos_error:
                errors.append({
                    "type": "Aid Data Processing Error",
                    "message": "Aid data has not been processed."
                })

            if words_failed:
                errors.append({
                    "type": "Textract Error",
                    "message": "Words analysis stll in progress."
                })

            if tables_failed:
                errors.append({
                    "type": "Textract Error",
                    "message": "Tables analysis stll in progress."
                })

            if check is not None and check["pass_fail"] == "Failed":
                errors.append({
                    "type": "Document Check Failed",
                    "message": "There are missing words in tables.",
                    "number_of_missing": number_of_missing,
                    "missing_amounts": missing_amounts
                })

            # create report_data for sendgrid
            report_data = {
                "document_name": document_name,
                "document_check": pass_fail,
                "award_reviewed": college_status.award_reviewed,
                "errors": errors,
                "aid_data": aid_data_report
            }

            # catch all multiples of the same document
            if college_status_id == next_college_status_id:
                collection.append(report_data)
                aid_data_report = []
                errors = []
            else:
                # send report and reset for next different document
                collection.append(report_data)
                send_report_email(college_status_id, collection)
                collection = []
                aid_data_report = []
                errors = []

        return CheckDocuments(checked_list=checked_list, aid_data_list=aid_data_list)


class Mutation(graphene.ObjectType):
    analyze_documents = AnalyzeDocuments.Field()
    check_documents = CheckDocuments.Field()
