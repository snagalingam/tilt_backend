import os
import boto3
import time
import json
import csv
from .table_methods import get_rows_columns_map, get_text, generate_table_csv

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

    response = textract.start_document_analysis(
        DocumentLocation={
            "S3Object": {
                "Bucket": bucket_name,
                "Name": file_name
            }}, 
        FeatureTypes=["TABLES"],
    )

    return response["JobId"]

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

def start_tables_extraction(document):
    job_id = start_job(document)
    print(f"====> Document: \033[94m{document}\033[0m")
    print(f"====> Start Tables Analysis with ID: \033[93m{job_id}\033[0m")
    return job_id

def get_table_data(job_id):
    response = get_result(job_id)
    status =  response[0]["JobStatus"]

    if status == "SUCCEEDED":
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

        return csv

    elif status == "IN_PROGRESS":
        raise Exception(f"Analysis still in progress")