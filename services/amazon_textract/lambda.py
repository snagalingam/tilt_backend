import os
import boto3
import json
from django.conf import settings

FUNCTION_NAME = os.environ.get("FUNCTION_NAME")

aws_lambda = boto3.client(
    'lambda',     
    region_name=settings.REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY)

def lambda_handler(documents):
    payload = {
        "message": "From Tilt Access.",
        "documents": documents
    }

    #For InvocationType = "Event"
    response = aws_lambda.invoke(
        FunctionName=FUNCTION_NAME, 
        InvocationType="Event", 
        Payload=json.dumps(payload))

    #For InvocationType = "RequestResponse"
    # resp = aws_lambda.invoke(
    #     FunctionName=function_name, 
    #     InvocationType="RequestResponse", 
    #     Payload=json.dumps(payload))

    print(response)
    breakpoint()
    return "Lambda Triggered"