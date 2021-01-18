import boto3
import csv

#from django.conf import settings
AWS_ACCESS_KEY = "AKIAY6JQE4YKQOHSVO6F"
AWS_BUCKET = "financial-letters"
AWS_LAMBDA_FUNCTION = "TiltGetAnalyzedData"
AWS_REGION = "us-east-2"
AWS_SECRET_KEY = "xLmHDvbbxITRhvKrZcn1P6IYMx0ZWixJEkjnMzkn"
GRAPHQL_ENDPOINT = "https://localhost:8000/graphql"


textract = boto3.client(
    "textract",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

################################################################################
# Start and get table data
################################################################################
def start_tables_analysis(document):
    response = textract.start_document_analysis(
        DocumentLocation={
            "S3Object": {
                "Bucket": settings.AWS_BUCKET,
                "Name": document
            }},
        FeatureTypes=["TABLES"]
    )
    return response["JobId"]

def get_table_data(job_id):
    pages = []

    response = textract.get_document_analysis(JobId=job_id)
    status =  response["JobStatus"]

    if status == "IN_PROGRESS":
        raise Exception("Analysis still in progress")

    elif status == "SUCCEEDED":
        pages.append(response)

        # goes through and receives all the pages for the document
        while "nextToken" in response:
            response = textract.get_document_analysis(JobId=job_id, NextToken=nextToken)
            pages.append(response)


    # adds all the text to a map
    blocks_map = {}
    table_blocks = []

    for page in pages:
        for block in page['Blocks']:
            blocks_map[block['Id']] = block
            if block['BlockType'] == "TABLE":
                table_blocks.append(block)

    if len(table_blocks) <= 0:
        print("No Table Found")

    else:
        data = {}
        for index, table in enumerate(table_blocks, start=1):
            # create new table in dictionary
            data[index] = {}
            table_data = data[index]

            for relationship in table['Relationships']:
                if relationship['Type'] == 'CHILD':
                    for child_id in relationship['Ids']:
                        # gets the cell value
                        cell = blocks_map[child_id]

                        # gets the cell
                        if cell['BlockType'] == 'CELL':
                            row_index = cell['RowIndex']
                            col_index = cell['ColumnIndex']
                            if row_index not in table_data:
                                # create new row
                                table_data[row_index] = {}

                            row_data = table_data[row_index]

                            if col_index not in row_data:
                                # create new column
                                row_data[col_index] = {}

                        # within the cell, it has the information on the text
                        if 'Relationships' in cell:
                            text = ""
                            for relationship in cell['Relationships']:
                                if relationship['Type'] == 'CHILD':
                                    for child_id in relationship['Ids']:
                                        word = blocks_map[child_id]
                                        if word['BlockType'] == 'WORD':
                                            if text == "":
                                                text += word['Text']

                                            # adds a space in between words
                                            else:
                                                text += " " + word['Text']
                        table_data[row_index][col_index] = text

        print(data)


################################################################################
# Start and get text data
################################################################################
def start_text_analysis(document):
    response = textract.start_document_text_detection(
        DocumentLocation={
            "S3Object": {
                "Bucket": AWS_BUCKET,
                "Name": document
        }}
    )
    return response["JobId"]

def get_text_data(job_id):
    pages = []
    text = []

    response = textract.get_document_text_detection(JobId=job_id)
    status =  response["JobStatus"]

    if status == "IN_PROGRESS":
        raise Exception("Analysis still in progress")

    elif status == "SUCCEEDED":
        pages.append(response)

        # goes through and receives all the pages for the document
        while "nextToken" in response:
            response = textract.get_document_text_detection(JobId=job_id, NextToken=nextToken)
            pages.append(response)

    # adds all the text words to a list
    for page in pages:
        for item in page["Blocks"]:
            if item["BlockType"] == "LINE":
                text.append(item["Text"])

    return text

get_table_data(job_id="ba4fa0f011a15f00cb5d06e0e803d745511ba802b57e07486daa775f37860e89")
