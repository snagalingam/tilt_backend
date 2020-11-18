import os
import boto3
import time
import json
import time
import math

access_key = os.environ.get("AWS_ACCESS")
secret_key = os.environ.get("AWS_SECRET")
region = "us-east-2"   
bucket_name = "financial-letters"
textract = boto3.client(
    "textract", 
    region_name=region,
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key)


def start_job(file_name):
    try:
        response = textract.start_document_text_detection(
            DocumentLocation={
                "S3Object": {
                    "Bucket": bucket_name,
                    "Name": file_name
                }
        })

    except Exception as e:
        print(f"""
            START JOB ===========> ERROR
            {json.dumps(e.response, indent=4)}
            """)
        return e.response
    
    return response["JobId"]


def complete_job(job_id):
    time.sleep(5)
    count = 0
    response = textract.get_document_text_detection(JobId=job_id)
    status = response["JobStatus"]

    while(status == "IN_PROGRESS"):
        time.sleep(5)
        count += 5
        # Sky Blue {count} seconds:
        print(f"===========> {status}: \033[96m{count} seconds\033[0m")
        response = textract.get_document_text_detection(JobId=job_id)
        status = response["JobStatus"]

    return status

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

def get_words(document):
    job_id = start_job(document)
    print(f"====> Document: \033[94m{document}\033[0m")
    # Orange job_id
    print(f"====> Started job with id: \033[93m{job_id}\033[0m")

    if(complete_job(job_id)):
        response = get_result(job_id)
        words = []

        # Print all words in list 
        for resultPage in response:
            for item in resultPage["Blocks"]:
                if item["BlockType"] == "LINE":
                    words.append(item["Text"])
                    # print('\033[94m' + item[ "Text"] + '\033[0m')

        # Create JSON file of WORDS
        # with open(f'textract_words.json', 'a+') as f:
        #     data = json.dumps({document: words}, indent=2, ensure_ascii=False)
        #     f.write(data + ',')
        
        # Blue {document} WORDS COMPLETE
        print(f"====> Words Complete: \033[94m{document}\033[0m")
        return words