import graphene
import json
import os
import time

from .models import Category, Data, DocumentData, DocumentResult
from college.models import Status
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from services.amazon_textract.check_document import start_document_check
from services.amazon_textract.get_words import get_words_data, start_words_analysis
from services.amazon_textract.get_tables import get_table_data, start_tables_analysis
from services.amazon_textract.lambda_handler import lambda_handler
from services.amazon_textract.parse_data import filter_possibilities, find_aid_category, get_aid_data
from services.sendgrid_api.send_email import send_notification_email, send_report_email


################################################
### Standard Model Definitions
################################################
class AidCategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class AidDataType(DjangoObjectType):
    class Meta:
        model = Data
        fields = "__all__"


class AidDocumentDataType(DjangoObjectType):
    class Meta:
        model = DocumentData
        fields = "__all__"


class AidDocumentResultType(DjangoObjectType):
    class Meta:
        model = DocumentResult
        fields = "__all__"


################################################
### Query
################################################
class AnalyzedResultType(graphene.ObjectType):
    document_name = graphene.String()
    sent = graphene.String()


class CheckedResultType(graphene.ObjectType):
    document_name = graphene.String()
    pass_fail = graphene.String()
    processed = graphene.Boolean()
    tables = graphene.String()
    words = graphene.String()


class Query(graphene.ObjectType):
    aid_data = graphene.List(AidDataType, limit=graphene.Int())
    aid_categories = graphene.List(AidCategoryType, limit=graphene.Int())
    aid_document_data = graphene.List(AidDocumentDataType, limit=graphene.Int())
    aid_document_results = graphene.List(AidDocumentResultType, limit=graphene.Int())

    aid_categories_by_fields = graphene.List(
        AidCategoryType,
        name=graphene.String(),
        primary=graphene.String(),
        secondary=graphene.String(),
        tertiary=graphene.String()
    )
    aid_data_by_fields = graphene.List(
        AidDataType,
        amount=graphene.Int(),
        category=graphene.ID(),
        col_index=graphene.Int(),
        college_status=graphene.ID(),
        name=graphene.String(),
        table_number=graphene.Int(),
        row_index=graphene.Int(),
    )
    aid_document_data_by_fields = graphene.List(
        AidDocumentDataType,
        document_name=graphene.String()
    )
    aid_document_results_by_fields = graphene.List(
        AidDocumentResultType,
        document_name=graphene.String(),
        pass_fail=graphene.Boolean(),
        processed=graphene.Boolean(),
        sent=graphene.Boolean()
    )

    # get_all()
    def resolve_aid_categories(self, info, limit=None):
        qs = AidCategory.objects.all()[0:limit]
        return qs

    def resolve_aid_data(self, info, limit=None):
        qs = AidData.objects.all()[0:limit]
        return qs

    def resolve_aid_document_data(self, info, limit=None):
        qs = AidDocumentData.objects.all()[0:limit]
        return qs

    def resolve_aid_document_results(self, info, limit=None):
        qs = AidDocumentResult.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_aid_categories_by_fields(self, info, **fields):
        qs = AidCategory.objects.filter(**fields)
        return qs

    def resolve_aid_data_by_fields(self, info, **fields):
        qs = AidData.objects.filter(**fields)
        return qs

    def resolve_aid_document_results_by_fields(self, info, **fields):
        qs = AidDocumentResult.objects.filter(**fields)
        return qs

    def resolve_aid_document_data_by_fields(self, info, **fields):
        qs = AidDocumentData.objects.filter(**fields)
        return qs

################################################
### Mutation
################################################
class AnalyzeDocuments(graphene.Mutation):
    sent_list = graphene.List(AnalyzedResultType)

    class Arguments:
        documents = graphene.List(graphene.String)

    def mutate(
        self,
        info,
        documents=None,
    ):
        sent_list = []
        user = info.context.user

        for document in documents:
            # send document for analysis
            words_id = start_words_analysis(document)
            tables_id = start_tables_analysis(document)

            # save job_ids to database
            document_result = AidDocumentResult(
                document_name=document,
                words_id=words_id,
                tables_id=tables_id,
                sent=True)
            document_result.save()
            sent_list.append(AnalyzedResultType(document_name=document, sent=True))

            # find college_status and update award_uploaded=True
            end_index = document.index("_file")
            college_status_id = int(document[3:end_index])
            college_status = Status.objects.get(pk=college_status_id)
            college_status.award_uploaded = True
            college_status.save()

        # trigger lambda to checkDocuments after 5 minutes
        lambda_handler(documents)
        return AnalyzeDocuments(sent_list=sent_list)


class CheckDocuments(graphene.Mutation):
    checked_list = graphene.List(CheckedResultType)
    aid_data_list = graphene.List(AidDataType)

    class Arguments:
        documents = graphene.List(graphene.String)

    def mutate(
        self,
        info,
        documents=None,
    ):

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
        for idx, document in enumerate(documents):
            doc = DocumentResult.objects.get(document_name=document)
            end_index = document.index("_file")
            college_status_id = int(document[3:end_index])
            college_status_id = 1

            # keep track of college_status_id positions
            if idx < last_index:
                # next_college_status_id = int(documents[idx + 1][3:end_index])
                next_college_status_id = college_status_id + 1
            elif idx == last_index:
                next_college_status_id = -1

            # check if words are processed
            try:
                words = get_words_data(doc.words_id)
            except:
                doc.processed = False
                words_failed = True

            # check if tables are processed
            try:
                tables = get_table_data(doc.tables_id)
            except:
                doc.processed = False
                tables_failed = True

            # if textract analysis fails
            if words_failed and tables_failed:
                checked_list.append(
                    CheckedResultType(
                        document_name=doc.name,
                        words="Failed",
                        tables="Failed",
                        pass_fail=None,
                        processed=False))
            elif words_failed and not tables_failed:
                checked_list.append(
                    CheckedResultType(
                        document_name=doc.name,
                        words="Failed",
                        tables=None,
                        pass_fail=None,
                        processed=False))
            elif tables_failed and not words_failed:
                checked_list.append(
                    CheckedResultType(
                        document_name=doc.name,
                        words=None,
                        tables="Failed",
                        pass_fail=None,
                        processed=False))

            # if document has words and tables
            elif not words_failed and not tables_failed:
                doc.processed = True
                check = start_document_check(words, tables)

                if check["pass_fail"] == "Failed":
                    checked_list.append(
                        CheckedResultType(
                            document_name=doc.name,
                            words="Passed",
                            tables="Passed",
                            pass_fail="Failed",
                            processed=True))
                else:
                    checked_list.append(
                        CheckedResultType(
                            document_name=doc.name,
                            words="Passed",
                            tables="Passed",
                            pass_fail="Passed",
                            processed=True))

                # aid_data from 'parse_data.py' scripts
                pos = get_aid_data(tables, doc.name)
                pos_error = pos.get("Document Error", None)

                if not pos_error:
                    for key in pos.keys():
                        table_number = int(key[6:])

                        for each in pos[key]:
                            name = each.get("Name")
                            amount =  each.get("Amount")
                            row_index = each.get("Row Index")
                            col_index = each.get("Col Index")
                            row_data = each.get("Row Data")

                            # get college_status_id from document
                            college_status = Status.objects.get(pk=college_status_id)

                            # auto award_reviewed=True if check passed and pos_error=False
                            if check["pass_fail"] == "Passed":
                                college_status.reviewed = True
                                college_status.save()

                            # filter/match for category
                            possibilities = find_aid_category(name, document)
                            category_name = filter_possibilities(possibilities)
                            aid_category = AidCategory.objects.get(name=category_name)

                            # check for dups
                            try:
                                aid_data = AidData.objects.get(
                                    name=name,
                                    amount=amount,
                                    table_number=table_number,
                                    row_index=row_index,
                                    col_index=col_index,
                                    row_data=row_data,
                                    college_status=college_status,
                                    aid_category=aid_category)
                                aid_data_list.append(aid_data)

                                # add aid data for report
                                aid_data_report.append({
                                    "college_status": college_status_id,
                                    "aid_category": aid_category.name,
                                    "name": name,
                                    "amount": amount,
                                    "table_number": table_number,
                                    "row_index": row_index,
                                    "col_index": col_index,
                                    "row_data": row_data})
                            except:
                                aid_data = None

                                # create AidDate if no dups
                                if aid_data is None:
                                    aid_data = AidData(
                                        name=name,
                                        amount=amount,
                                        table_number=table_number,
                                        row_index=row_index,
                                        col_index=col_index,
                                        row_data=row_data,
                                        college_status=college_status,
                                        aid_category=aid_category)
                                    aid_data.save()
                                    aid_data_list.append(aid_data)

                                    # add aid data for report
                                    aid_data_report.append({
                                        "college_status": college_status_id,
                                        "aid_category": aid_category.name,
                                        "name": name,
                                        "amount": amount,
                                        "table_number": table_number,
                                        "row_index": row_index,
                                        "col_index": col_index,
                                        "row_data": row_data})

                # check if document_data exists
                try:
                    document_data = DocumentData.objects.get(name=doc.name)
                except:
                    document_data = None

                # else create new document_data
                if document_data is None:
                    document_data = DocumentData(
                        name=doc.name,
                        words=words,
                        tables=tables)
                    document_data.save()

            if check is not None:
                # update and save document_data results on each document
                pass_fail = check.get("pass_fail", None)
                number_of_missing = check.get("number_of_missing", None)
                missing_amounts = check.get("missing_amounts", None)
                doc.pass_fail = pass_fail
                doc.number_of_missing = number_of_missing
                doc.missing_amounts = missing_amounts
            doc.save()

            # handle errors
            if pos_error:
                errors.append({
                    "type": "Aid Data Processing Error",
                    "message": "Aid data has not been processed."})

            if words_failed:
                errors.append({
                    "type": "Textract Error",
                    "message": "Words analysis stll in progress."})

            if tables_failed:
                errors.append({
                    "type": "Textract Error",
                    "message": "Tables analysis stll in progress."})

            if check is not None and check["pass_fail"] == "Failed":
                errors.append({
                    "type": "Document Check Failed",
                    "message": "There are missing words in tables.",
                    "number_of_missing": number_of_missing,
                    "missing_amounts": missing_amounts})

            # create report_data for sendgrid
            report_data = {
                "document_name": document,
                "document_check": pass_fail,
                "award_reviewed": college_status.reviewed,
                "errors": errors,
                "aid_data": aid_data_report}

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


class CreateAidCategory(graphene.Mutation):
    aid_category = graphene.Field(AidCategoryType)
    success = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        primary = graphene.String()
        secondary = graphene.String()
        tertiary = graphene.String()

    def mutate(
        self,
        info,
        name=None,
        primary=None,
        secondary=None,
        tertiary=None
    ):
        try:
            aid_category = AidCategory.objects.get(name=name)
        except:
            aid_category = None

        if aid_category is None:
            aid_category = AidCategory(
                name=name,
                primary=primary,
                secondary=secondary,
                tertiary=tertiary,
                year=year
            )
            aid_category.save()

            return CreateAidCategory(aid_category=aid_category, success=True)
        raise Exception ('Aid category already exists')


class Mutation(graphene.ObjectType):
    analyze_documents = AnalyzeDocuments.Field()
    check_documents = CheckDocuments.Field()
    create_aid_category = CreateAidCategory.Field()
