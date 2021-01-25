import boto3

from django.conf import settings


textract = boto3.client(
    "textract",
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

################################################################################
# Start and get table data
################################################################################
def start_table_analysis(document):
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
    errors = []

    response = textract.get_document_analysis(JobId=job_id)
    status =  response["JobStatus"]

    if status == "SUCCEEDED":
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
            errors.append({
                "type": "No table found",
                "message": "Table analysis returned no tables"
            })

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

    else:
        errors.append({
            "type": "Table analysis did not succeed",
            "message": f"Textract returned {status}"
        })

    return data, errors


################################################################################
# Start and get text data
################################################################################
def start_text_analysis(document):
    response = textract.start_document_text_detection(
        DocumentLocation={
            "S3Object": {
                "Bucket": settings.AWS_BUCKET,
                "Name": document
        }}
    )
    return response["JobId"]

def get_text_data(job_id):
    errors= []
    pages = []
    text = []

    response = textract.get_document_text_detection(JobId=job_id)
    status =  response["JobStatus"]

    if status == "SUCCEEDED":
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

    else:
        errors.append({
            "type": "Text analysis did not succeed",
            "message": f"Textract returned {status}"
        })

    return text, errors
