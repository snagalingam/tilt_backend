import boto3
from botocore.exceptions import ClientError
from django.conf import settings

client = boto3.client(
    's3',     
    region_name=settings.REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY)

def delete_document(document_name):
    try:
        response = client.delete_object(
            Bucket=settings.BUCKET,
            Key=document_name)
    except ClientError as e:
        print(e)
        return False
    return True

def upload_document(document_name, blob):
    try:
        response = client.upload_file(
            Filename=blob, 
            Bucket=settings.BUCKET,
            Key=document_name)
    except ClientError as e:
        print(e)
        return False
    return True