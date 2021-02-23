import os
import boto3
import json

from django.conf import settings


aws_lambda = boto3.client(
    "lambda",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

def lambda_handler(documents, graphql_endpoint, table_job_ids, text_job_ids):
    variables = {
        "documents": documents,
        "graphql_endpoint": graphql_endpoint,
        "table_job_ids": table_job_ids,
        "text_job_ids": text_job_ids
    }

    aws_lambda.invoke(
        FunctionName=settings.AWS_LAMBDA_FUNCTION,
        InvocationType="Event",
        Payload=json.dumps(variables)
    )

    pass
