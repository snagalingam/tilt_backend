import graphene
from graphene_django import DjangoObjectType
import json
import os
import time
from django.contrib.auth import get_user_model
from .models import DocumentResult, DocumentData, Category, Data

from colleges.models import Status
from services.amazon_textract.lambda_handler import lambda_handler
from services.amazon_textract.get_words import start_words_analysis, get_words_data
from services.amazon_textract.get_tables import start_tables_analysis, get_table_data
from services.amazon_textract.check_document import start_document_check
from services.amazon_textract.parse_data import get_data, find_category, filter_possibilities
from services.sendgrid_api.send_email import send_report_email, send_notification_email

class DocumentResultType(DjangoObjectType):
    class Meta:
        model = DocumentResult
        fields = "__all__"

class DocumentDataType(DjangoObjectType):
    class Meta:
        model = DocumentData
        fields = "__all__"

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class DataType(DjangoObjectType):
    class Meta:
        model = Data
        fields = "__all__"

class AnalyzedResultType(graphene.ObjectType):
    name = graphene.String()       
    sent = graphene.String()

class CheckedResultType(graphene.ObjectType):
    name = graphene.String()       
    pass_fail = graphene.String()
    processed = graphene.Boolean()
    words = graphene.String()
    tables = graphene.String()

class Query(graphene.ObjectType):
    document_results = graphene.List(DocumentResultType, limit=graphene.Int())
    document_datas = graphene.List(DocumentDataType, limit=graphene.Int())
    categories = graphene.List(CategoryType, limit=graphene.Int())
    datas = graphene.List(DataType, limit=graphene.Int())

    # document_result
    document_results_by_fields = graphene.List(
        DocumentResultType, 
        name=graphene.String(),
        sent=graphene.Boolean(),
        processed=graphene.Boolean(),
        pass_fail=graphene.Boolean(),
        expired=graphene.Boolean(),
        start_date=graphene.Boolean())

    # document_datas
    document_datas_by_fields = graphene.List(
        DocumentDataType, 
        name=graphene.String())

    # categories
    categories_by_fields = graphene.List(
        CategoryType, 
        name=graphene.String(),
        main_category=graphene.String(),
        sub_category=graphene.String(),
        sub_sub_category=graphene.String(),
        year=graphene.Int())

    # datas
    datas_by_fields = graphene.List(
        DataType, 
        name=graphene.String(),
        amount=graphene.Int(),
        table_number=graphene.Int(),
        row_index=graphene.Int(),
        col_index=graphene.Int(),
        status=graphene.ID(),
        category=graphene.ID())

    # get_all()
    def resolve_document_results(self, info, limit=None):
        qs = DocumentResult.objects.all()[0:limit]
        return qs

    def resolve_document_datas(self, info, limit=None):
        qs = DocumentData.objects.all()[0:limit]
        return qs

    def resolve_categories(self, info, limit=None):
        qs = Category.objects.all()[0:limit]
        return qs

    def resolve_datas(self, info, limit=None):
        qs = Data.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_document_results_by_fields(self, info, **fields):
        qs = DocumentResult.objects.filter(**fields)
        return qs

    def resolve_document_datas_by_fields(self, info, **fields):
        qs = DocumentData.objects.filter(**fields)
        return qs

    def resolve_categories_by_fields(self, info, **fields):
        qs = Category.objects.filter(**fields)
        return qs

    def resolve_datas_by_fields(self, info, **fields):
        qs = Data.objects.filter(**fields)
        return qs

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
            document_result = DocumentResult(
                name=document,
                words_id=words_id,
                tables_id=tables_id,
                sent=True
            )
            document_result.save()
            sent_list.append(AnalyzedResultType(name=document, sent=True))

            # find status and update award_uploaded=True
            end_index = document.index("_file")
            status_id = int(document[3:end_index])
            status = Status.objects.get(pk=status_id)
            status.award_uploaded = True 
            status.save()

        # trigger lambda to checkDocuments after 5 minutes
        lambda_handler(documents)
        return AnalyzeDocuments(sent_list=sent_list)

class CheckDocuments(graphene.Mutation):
    checked_list = graphene.List(CheckedResultType)
    data_list = graphene.List(DataType)
    
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
        data_report = []
        words_failed = None
        tables_failed = None
        pos_error = None 
        next_status_id = None
        last_index = len(documents) - 1
        checked_list = []
        data_list = []

        # interate through list 
        for idx, document in enumerate(documents):
            doc = DocumentResult.objects.get(name=document)
            end_index = document.index("_file")
            status_id = int(document[3:end_index])
            status_id = 1

            # keep track of status_id positions
            if idx < last_index:
                # next_status_id = int(documents[idx + 1][3:end_index])
                next_status_id = status_id + 1
            elif idx == last_index:
                next_status_id = -1

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
                        name=doc.name, 
                        words="Failed", 
                        tables="Failed", 
                        pass_fail=None, 
                        processed=False))
            elif words_failed and not tables_failed:
                checked_list.append(
                    CheckedResultType(
                        name=doc.name, 
                        words="Failed", 
                        tables=None, 
                        pass_fail=None, 
                        processed=False))
            elif tables_failed and not words_failed:
                checked_list.append(
                    CheckedResultType(
                        name=doc.name, 
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
                            name=doc.name, 
                            words="Passed", 
                            tables="Passed", 
                            pass_fail="Failed", 
                            processed=True))
                else: 
                    checked_list.append(
                        CheckedResultType(
                            name=doc.name, 
                            words="Passed", 
                            tables="Passed", 
                            pass_fail="Passed", 
                            processed=True))

                # data from 'parse_data.py' scripts
                pos = get_data(tables, doc.name)
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

                            # get status_id from document
                            college_status = Status.objects.get(pk=status_id)

                            # auto award_reviewed=True if check passed and pos_error=False 
                            if check["pass_fail"] == "Passed":
                                college_status.award_reviewed = True
                                college_status.save()

                            # filter/match for category 
                            possibilities = find_category(name, document)
                            category = filter_possibilities(possibilities)
                            category = Category.objects.get(name=category)

                            # check for dups
                            try:
                                data = Data.objects.get(
                                    name=name, 
                                    amount=amount,
                                    table_number=table_number,
                                    row_index=row_index,
                                    col_index=col_index,
                                    row_data=row_data,
                                    status=college_status,
                                    category=category
                                )
                                data_list.append(data)

                                # add aid data for report
                                data_report.append({
                                    "status": status_id,
                                    "category": category.name,
                                    "name": name,
                                    "amount": amount,
                                    "table_number": table_number,
                                    "row_index": row_index,
                                    "col_index": col_index,
                                    "row_data": row_data,
                                })
                            except:
                                data = None

                                # create AidDate if no dups
                                if data is None:
                                    data = Data(
                                        name=name,
                                        amount=amount,
                                        table_number=table_number,
                                        row_index=row_index,
                                        col_index=col_index,
                                        row_data=row_data,
                                        status=college_status,
                                        category=category
                                    )
                                    data.save()
                                    data_list.append(data)

                                    # add aid data for report
                                    data_report.append({
                                        "status": status_id,
                                        "category": category.name,
                                        "name": name,
                                        "amount": amount,
                                        "table_number": table_number,
                                        "row_index": row_index,
                                        "col_index": col_index,
                                        "row_data": row_data,
                                    })
                
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
                        tables=tables
                    )
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
                    "message": "Aid data has not been processed.",
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
                    "missing_amounts": missing_amounts,
                })           

            # create report_data for sendgrid
            report_data = {
                "document_name": document,
                "document_check": pass_fail,
                "award_reviewed": college_status.award_reviewed,
                "errors": errors,
                "data": data_report,
            }

            # catch all multiples of the same document
            if status_id == next_status_id:
                collection.append(report_data)
                data_report = []
                errors = []
            else:
                # send report and reset for next different document
                collection.append(report_data)
                send_report_email(status_id, collection)
                collection = []
                data_report = []
                errors = []

        return CheckDocuments(checked_list=checked_list, data_list=data_list)

class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)
    success = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        main_category = graphene.String()
        sub_category = graphene.String()
        sub_sub_category = graphene.String()
        year = graphene.Int()

    def mutate(
        self,
        info,
        name=None,
        main_category=None,
        sub_category=None,
        sub_sub_category=None,
        year=None,
    ):
        try:
            category = Category.objects.get(name=name)
        except:
            category = None

        if category is None:
            category = Category(
                name=name, 
                main_category=main_category,
                sub_category=sub_category,
                sub_sub_category=sub_sub_category,
                year=year)
            category.save()
            return CreateCategory(category=category, success=True)
        else:
            raise Exception ('Aid category already exists')

class Mutation(graphene.ObjectType):
    analyze_documents = AnalyzeDocuments.Field()
    check_documents = CheckDocuments.Field()