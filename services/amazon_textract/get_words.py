import os
import boto3
import time
import json
import time

access_key = os.environ.get("AWS_ACCESS")
secret_key = os.environ.get("AWS_SECRET")
region = os.environ.get("REGION")
bucket_name = os.environ.get("BUCKET")
textract = boto3.client(
    "textract", 
    region_name=region,
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key)

def start_job(file_name):

    response = textract.start_document_text_detection(
        DocumentLocation={
            "S3Object": {
                "Bucket": bucket_name,
                "Name": file_name
        }}
    )

    return response["JobId"]

def get_result(job_id):
    pages = []
    response = textract.get_document_text_detection(JobId=job_id)
    pages.append(response)
    nextToken = None

    error = response.get('Error', None)
    if error is not None:
        breakpoint()    
        
    if('NextToken' in response):
        nextToken = response['NextToken']

    while(nextToken):
        response = textract.get_document_text_detection(JobId=job_id, NextToken=nextToken)
        pages.append(response)
        nextToken = None

        if('NextToken' in response):
            nextToken = response['NextToken']

    return pages

def start_words_extraction(document):
    job_id = start_job(document)
    print(f"====> Document: \033[94m{document}\033[0m")
    print(f"====> Started job with id: \033[93m{job_id}\033[0m")
    return job_id

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