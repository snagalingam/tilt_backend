import os
import boto3
import json
from django.conf import settings

FUNCTION_NAME = os.environ.get("FUNCTION_NAME")
GRAPHQL_ENDPOINT = os.environ.get("GRAPHQL_ENDPOINT")

aws_lambda = boto3.client(
    'lambda',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY)

def lambda_handler(documents):
    payload = {
        "graphql_endpoint": GRAPHQL_ENDPOINT,
        "documents": documents
    }

    #For InvocationType = "Event"
    aws_lambda.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType="Event",
        Payload=json.dumps(payload))

    pass
