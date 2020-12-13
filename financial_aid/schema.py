import graphene
from graphene_django import DjangoObjectType
import json
import os
import time
from django.contrib.auth import get_user_model
from .models import DocumentResult, DocumentData, BucketCheck, BucketResult, AidCategory, AidData
from college_status.models import CollegeStatus
from services.amazon_textract.get_words import start_words_extraction, get_words_data
from services.amazon_textract.get_tables import start_tables_extraction, get_table_data
from services.amazon_textract.check_document import start_document_check, start_bucket_check, get_bucket_results, get_documents
from services.amazon_textract.parse_data import get_aid_data, find_aid_category, filter_possibilities
from services.sendgrid_api.send_email import send_report_email, send_notification_email
class DocumentResultType(DjangoObjectType):
    class Meta:
        model = DocumentResult
        fields = "__all__"

class DocumentDataType(DjangoObjectType):
    class Meta:
        model = DocumentData
        fields = "__all__"

class BucketCheckType(DjangoObjectType):
    class Meta:
        model = BucketCheck
        fields = "__all__"

class BucketResultType(DjangoObjectType):
    class Meta:
        model = BucketResult
        fields = "__all__"
class AidCategoryType(DjangoObjectType):
    class Meta:
        model = AidCategory
        fields = "__all__"

class AidDataType(DjangoObjectType):
    class Meta:
        model = AidData
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
    bucket_checks = graphene.List(BucketCheckType, limit=graphene.Int())
    bucket_results = graphene.List(BucketResultType, limit=graphene.Int())
    aid_categories = graphene.List(AidCategoryType, limit=graphene.Int())
    aid_datas = graphene.List(AidDataType, limit=graphene.Int())

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

    # aid_categories
    aid_categories_by_fields = graphene.List(
        AidCategoryType, 
        name=graphene.String(),
        main_category=graphene.String(),
        sub_category=graphene.String(),
        sub_sub_category=graphene.String(),
        year=graphene.Int())

    # aid_datas
    aid_datas_by_fields = graphene.List(
        AidDataType, 
        name=graphene.String(),
        amount=graphene.Int(),
        table_number=graphene.Int(),
        row_index=graphene.Int(),
        col_index=graphene.Int(),
        college_status=graphene.ID(),
        aid_category=graphene.ID())

    # get_all()
    def resolve_document_results(self, info, limit=None):
        qs = DocumentResult.objects.all()[0:limit]
        return qs

    def resolve_document_datas(self, info, limit=None):
        qs = DocumentData.objects.all()[0:limit]
        return qs

    def resolve_bucket_checks(self, info, limit=None):
        qs = BucketCheck.objects.all()[0:limit]
        return qs

    def resolve_bucket_results(self, info, limit=None):
        qs = BucketResult.objects.all()[0:limit]
        return qs

    def resolve_aid_categories(self, info, limit=None):
        qs = AidCategory.objects.all()[0:limit]
        return qs

    def resolve_aid_datas(self, info, limit=None):
        qs = AidData.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_document_results_by_fields(self, info, **fields):
        qs = DocumentResult.objects.filter(**fields)
        return qs

    def resolve_document_datas_by_fields(self, info, **fields):
        qs = DocumentData.objects.filter(**fields)
        return qs

    def resolve_aid_categories_by_fields(self, info, **fields):
        qs = AidCategory.objects.filter(**fields)
        return qs

    def resolve_aid_datas_by_fields(self, info, **fields):
        qs = AidData.objects.filter(**fields)
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
            words_id = start_words_extraction(document)
            tables_id = start_tables_extraction(document)

            document_result = DocumentResult(
                user=user,
                name=document,
                words_id=words_id,
                tables_id=tables_id,
                sent=True
            )
            document_result.save()
            sent_list.append(AnalyzedResultType(name=document, sent=True))
        
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
            doc = DocumentResult.objects.get(name=document)
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

                # aid_data from 'parse_data.py' scripts
                pos = get_aid_data(tables, doc.name)
                pos_error = pos.get("Document Error", None)

                if not pos_error:
                    # auto reviewed=True if check passed and pos_error=False 
                    if check["pass_fail"] == "Passed":
                        doc.reviewed = True

                    for key in pos.keys():
                        table_number = int(key[6:])

                        for each in pos[key]:
                            name = each.get("Name")
                            amount =  each.get("Amount")
                            row_index = each.get("Row Index")
                            col_index = each.get("Col Index")
                            row_data = each.get("Row Data")

                            # get college_status_id from document
                            college_status = CollegeStatus.objects.get(pk=college_status_id)

                            # filter/match for category 
                            possibilities = find_aid_category(name, document)
                            category = filter_possibilities(possibilities)
                            aid_category = AidCategory.objects.get(name=category)

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
                                    aid_category=aid_category
                                )
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
                                    "row_data": row_data,
                                })
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
                                        aid_category=aid_category
                                    )
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
                "reviewed": doc.reviewed,
                "errors": errors,
                "aid_data": aid_data_report,
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

class GetBucket(graphene.Mutation):
    bucket_list = graphene.List(graphene.String)

    class Arguments:
        bucket = graphene.String()
        limit = graphene.Int()

    def mutate(
        self,
        info,
        bucket=None,
        limit=None,
    ):
        try:
            bucket_list = get_documents(bucket, limit)
        except Exception as e:
            error = e.response["Error"]["Message"]
            raise Exception(f'{error}')
        
        return GetBucket(bucket_list=bucket_list)

class StartBucketCheck(graphene.Mutation):
    pending = graphene.Boolean()

    class Arguments:
        bucket = graphene.String()
        limit = graphene.Int()

    def mutate(
        self,
        info,
        bucket=None,
        limit=None,
    ):
        qs = BucketCheck.objects.filter(bucket=bucket)

        if len(qs) > 0:
            raise Exception('Bucket already exists')
        else:
            job_dict = start_bucket_check(bucket, limit) 
            data = json.dumps(job_dict, indent=2)
            check = BucketCheck(bucket=bucket, job_dict=data)
            check.save()

        return StartBucketCheck(pending=True)

class GetBucketResult(graphene.Mutation):
    bucket_result = graphene.Field(BucketResultType)

    class Arguments:
        bucket = graphene.String()

    def mutate(
        self,
        info,
        bucket=None,
    ):
        try:
            data = BucketCheck.objects.get(bucket=bucket)
            job_dict =  json.loads(data.job_dict)
            get_bucket = get_bucket_results(bucket, job_dict)
        except Exception as e:
            raise e
            
        total = get_bucket.get('Total')
        passed_count = get_bucket.get('Passed Count')
        passed_list = get_bucket.get('Passed List')
        failed_count = get_bucket.get('Failed Count')
        failed_list = get_bucket.get('Failed List')
        missing = get_bucket.get('Missing Amounts')
        missing_amounts = json.dumps(missing, indent=2)

        results = BucketResult(
            bucket=bucket,
            total_documents=total,
            passed_count=passed_count,
            passed_list=passed_list,
            failed_count=failed_count,
            failed_list=failed_list,
            missing=missing_amounts
        )
        results.save()

        return GetBucketResult(bucket_result=results)

class CreateAidCategory(graphene.Mutation):
    aid_category = graphene.Field(AidCategoryType)
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
            aid_category = AidCategory.objects.get(name=name)
        except:
            aid_category = None

        if aid_category is None:
            aid_category = AidCategory(
                name=name, 
                main_category=main_category,
                sub_category=sub_category,
                sub_sub_category=sub_sub_category,
                year=year)
            aid_category.save()
            return CreateAidCategory(aid_category=aid_category, success=True)
        else:
            raise Exception ('Aid category already exists')

class Mutation(graphene.ObjectType):
    analyze_documents = AnalyzeDocuments.Field()
    check_documents = CheckDocuments.Field()
    get_bucket = GetBucket.Field()
    start_bucket_check = StartBucketCheck.Field()
    get_bucket_result = GetBucketResult.Field()
