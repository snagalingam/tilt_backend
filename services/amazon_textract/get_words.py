import os
import boto3
import time
import json
import time
from django.conf import settings

textract = boto3.client(
    "textract",
    region_name=settings.REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY)

def start_job(file_name):
    response = textract.start_document_text_detection(
        DocumentLocation={
            "S3Object": {
                "Bucket": settings.BUCKET,
                "Name": file_name
        }})
    return response["JobId"]

def start_words_analysis(document):
    job_id = start_job(document)
    print(f"====> Document: \033[94m{document}\033[0m")
    print(f"====> Start Words Analysis with ID: \033[93m{job_id}\033[0m")
    return job_id
    
def get_result(job_id):
    pages = []
    response = textract.get_document_text_detection(JobId=job_id)
    pages.append(response)
    nextToken = None

    if('NextToken' in response):
        nextToken = response['NextToken']

    while(nextToken):
        response = textract.get_document_text_detection(JobId=job_id, NextToken=nextToken)
        pages.append(response)
        nextToken = None

        if('NextToken' in response):
            nextToken = response['NextToken']

    return pages

def get_words_data(job_id):
    response = get_result(job_id)
    status =  response[0]["JobStatus"]
    words = []

    if status == "SUCCEEDED":
        # Print all words in list
        for resultPage in response:
            for item in resultPage["Blocks"]:
                if item["BlockType"] == "LINE":
                    words.append(item["Text"])

        return words

    elif status == "IN_PROGRESS":
        raise Exception(f"Analysis still in progress")
