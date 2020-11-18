import os
import boto3
import time
import json
import csv
from table_methods import get_rows_columns_map, get_text, generate_table_csv

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
        response = textract.start_document_analysis(
            DocumentLocation={
                "S3Object": {
                    "Bucket": bucket_name,
                    "Name": file_name
                }}, 
            FeatureTypes=["TABLES"],
        )

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
    response = textract.get_document_analysis(JobId=job_id)
    status = response["JobStatus"]

    while(status == "IN_PROGRESS"):
        time.sleep(5)
        count += 5
        # Sky Blue IN_PROGRESS:
        print(f"===========> {status}: \033[96m{count} seconds\033[0m")
        response = textract.get_document_analysis(JobId=job_id)
        status = response["JobStatus"]

    return status

def get_result(job_id):
    pages = []
    response = textract.get_document_analysis(JobId=job_id)
    pages.append(response)
    nextToken = None

    if('NextToken' in response):
        nextToken = response['NextToken']

    while(nextToken):
        response = textract.get_document_analysis(JobId=job_id, NextToken=nextToken)
        pages.append(response)
        nextToken = None

        if('NextToken' in response):
            nextToken = response['NextToken']

    return pages

def get_tables(document):
    job_id = start_job(document)
    print(f"====> Document: \033[94m{document}\033[0m")
    # Orange job_id
    print(f"====> Started job with id: \033[93m{job_id}\033[0m")

    if(complete_job(job_id)):
        response = get_result(job_id)
        blocks = response[0]['Blocks']
        blocks_map = {}
        table_blocks = []

        for block in blocks:
            blocks_map[block['Id']] = block
            if block['BlockType'] == "TABLE":
                table_blocks.append(block)

        if len(table_blocks) <= 0:
            print("<b> NO Table FOUND </b>")

        csv = ''
        for index, table in enumerate(table_blocks):
            csv += generate_table_csv(table, blocks_map, index +1)
            csv += '\n\n'

        # print('\033[94m' + csv + '\033[0m')

        # Create CSV file of TABLES
        # with open(f"textract_tables/{document}.csv", "wt") as f:
        #     f.write(csv)

        # Blue {document} TABLES COMPLETE
        print(f"=====> Tables Complete: \033[94m{document}\033[0m")
        return csv