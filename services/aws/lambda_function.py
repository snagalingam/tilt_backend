import boto3
import json
import requests
import time

AWS_REGION = "us-east-2"
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""

textract = boto3.client(
    "textract",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def lambda_handler(event, context):
    table_job_ids = event["table_job_ids"]
    text_job_ids = event["text_job_ids"]

    for id in table_job_ids:
        table_status = textract.get_document_analysis(JobId=id)["JobStatus"]

        counter = 1
        while table_status == "IN_PROGRESS" and counter < 10:
            time.sleep(10)
            table_status = textract.get_document_analysis(JobId=id)["JobStatus"]
            counter += 1

    for id in text_job_ids:
        text_status = textract.get_document_text_detection(JobId=id)["JobStatus"]

        counter = 1
        while text_status == "IN_PROGRESS" and counter < 10:
            time.sleep(10)
            text_status = textract.get_document_text_detection(JobId=id)["JobStatus"]
            counter += 1

    mutation = '''
        mutation ($documents: [String!]) {
            parseDocuments (documents: $documents) {
                success
            }
        }
    '''

    res = requests.post(
        event["graphql_endpoint"],
        json={
            'query': mutation,
            'variables': event
        },
        verify=False
    )
    print(res)
