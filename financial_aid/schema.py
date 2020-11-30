import graphene
from graphene_django import DjangoObjectType
import json
import os
import time
from django.contrib.auth import get_user_model
from .models import DocumentResult, DocumentData, BucketCheck, BucketResult
from services.amazon_textract.get_words import start_words_extraction, get_words_data
from services.amazon_textract.get_tables import start_tables_extraction, get_table_data
from services.amazon_textract.check_document import document_check, start_bucket_check, get_bucket_check, get_documents


class DocumentDataType(DjangoObjectType):
    class Meta:
        model = DocumentData
        fields = "__all__"

class BucketResultType(DjangoObjectType):
    class Meta:
        model = BucketResult
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
    documents = graphene.List(DocumentDataType, limit=graphene.Int())
    document_by_name = graphene.Field(DocumentDataType, name=graphene.String())

    def resolve_documents(self, info, limit=None):
        return DocumentData.objects.all()[0:limit]

    def resolve_document_by_name(self, info, name=None):
        return DocumentData.objects.get(name=name)

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

        for document in documents:
            words_id = start_words_extraction(document)
            tables_id = start_tables_extraction(document)

            document_result = DocumentResult(
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

    class Arguments:
        documents = graphene.List(graphene.String)

    def mutate(
        self,
        info,
        documents=None,
    ):
        checked_list = []
        words_failed = None
        tables_failed = None

        # interate through list 
        for document in documents:
            doc = DocumentResult.objects.get(name=document)

            # check if words are processed
            try:
                words = get_words_data(doc.words_id)
            except:
                doc.processed = False
                words_failed = True 

            if words_failed:
                checked_list.append(
                    CheckedResultType(name=doc.name, 
                                words="Failed", 
                                tables=None, 
                                pass_fail=None, 
                                processed=False))
            else:
                # check if tables are processed
                try:
                    tables = get_table_data(doc.tables_id)
                except:
                    doc.processed = False
                    tables_failed = True
                
                if tables_failed:
                    checked_list.append(
                        CheckedResultType(
                            name=doc.name, 
                                words=None, 
                                tables="Failed", 
                                pass_fail=None, 
                                processed=False))

                # check if document passed or failed
                elif not words_failed and not tables_failed:
                    doc.processed = True 
                    check = document_check(words, tables)

                    if check:
                        doc.pass_fail = True
                        checked_list.append(
                            CheckedResultType(
                                name=doc.name, 
                                words="Passed", 
                                tables="Passed", 
                                pass_fail="Passed", 
                                processed=True))
                    else: 
                        doc.pass_fail = False
                        checked_list.append(
                            CheckedResultType(
                                name=doc.name, 
                                words="Passed", 
                                tables="Passed", 
                                pass_fail="Failed", 
                                processed=True))

                    # check if data exists
                    try:
                        data = DocumentData.objects.get(name=doc.name)
                    except:
                        data = None

                    if data is None:
                        # save data
                        data = DocumentData(
                            name=doc.name, 
                            words=words,
                            tables=tables
                        )
                        data.save()

            # save document_result after each iteration 
            doc.save()

        return CheckDocuments(checked_list=checked_list)

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
            get_bucket = get_bucket_check(bucket, job_dict)
        except Exception as e:
            raise e
            
        total = get_bucket.get('Total')
        passed_count = get_bucket.get('Passed Count')
        passed_list = get_bucket.get('Passed List')
        failed_count = get_bucket.get('Failed Count')
        failed_list = get_bucket.get('Failed List')

        results = BucketResult(
            bucket=bucket,
            total_documents=total,
            passed_count=passed_count,
            passed_list=passed_list,
            failed_count=failed_count,
            failed_list=failed_list,
        )
        results.save()

        return GetBucketResult(bucket_result=results)

class Mutation(graphene.ObjectType):
    analyze_documents = AnalyzeDocuments.Field()
    check_documents = CheckDocuments.Field()
    get_bucket = GetBucket.Field()
    start_bucket_check = StartBucketCheck.Field()
    get_bucket_result = GetBucketResult.Field()
