import os
import boto3
import datetime
from dateutil.relativedelta import relativedelta
from .get_tables import start_tables_analysis, get_table_data
from .get_words import start_words_analysis, get_words_data
from django.conf import settings

resource = boto3.resource(
    's3',     
    region_name=settings.REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY)

client = boto3.client(
    's3',     
    region_name=settings.REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY)

NUMBERS = {
  "0": True,
  "1": True,
  "2": True,
  "3": True,
  "4": True,
  "5": True,
  "6": True,
  "7": True,
  "8": True,
  "9": True,
}

# -------------- Delete Document From Bucket

def delete_document(bucket_name, document):
    client.delete_object(
        Bucket=bucket_name,
        Key=document,
    )
    print(f"DELETED: {document}")

# -------------- Get Bucket Documents For Bucket Check

def get_documents(bucket_name, limit=None):
    try:
        bucket = resource.Bucket(bucket_name)

    except Exception as e:
        print(f"""
            GET BUCKET ======> ERROR
            {e}
            """)
        return e

    file_list = []

    for obj in bucket.objects.limit(limit):
        # add month to object date
        date = obj.last_modified + relativedelta(days=30) 
        current = datetime.datetime.now()
        # if object date is eariler than current date
        expired = date.date() < current.date()

        if (expired):
            delete_document(bucket_name, obj.key)
        else:
            file_list.append(obj.key)
            
    if (len(file_list) < 1):
        raise Exception('Bucket is empty')
    else:
        return file_list

# -------------- Format Word To Valid Money Amount

def strip_money_string(word):
    if word.count("$") > 1 and word[1] != "$":
        return word

    start_index = word.index("$")
    stripped = word[start_index:].strip()

    if "*" in stripped:
        stripped = stripped.replace("*", "")

    if "=" in stripped:
        stripped = stripped.replace("=", "")

    if "+" in stripped:
        stripped = stripped.replace("+", "")

    if "-" in stripped:
        stripped = stripped.replace("-", "")

    if " " in stripped:
        idx = stripped.index(" ")
        if stripped[idx + 1] in NUMBERS:
            stripped.replace(" ", "")
        else:
          stripped = stripped[0:idx]
    
    if "/" in stripped:
        idx = stripped.index("/")
        stripped = stripped[0:idx]

    if stripped[-1] == ",":
        stripped = stripped[0:-1]
    
    if stripped[-1] == ".":
        stripped = stripped[0:-1]

    if stripped[-3:-2] == ".":
        stripped = stripped[0:-3]

    if stripped[-3:-2] == ",":
        stripped = stripped[0:-3]

    if "." in stripped:
        stripped = stripped.replace(".", ",")

    return stripped

# -------------- Create A List Of All Money In Document

def document_money_list(all_document_words):
    money_words = []

    for word in all_document_words:
        if "$" in word:
            money = strip_money_string(word)
            money_words.append(money)

    return money_words

def table_list(source):
    tables = source.split("\n\n")
    table_list = []

    for line in tables:
        if line[0:13] == "Table: Table_":
            continue
        else:
            if len(line) > 0: 
                table_arr = line.split(",\n")

                for each_row in table_arr:
                    row_arr = each_row.split('","')
                    for word in row_arr: 
                        table_list.append(word.replace('"', ""))

    return table_list

# -------------- Check If All Words In Documents Are In Tables 

def check_tables(tables_words, all_document_words):
    money_list = document_money_list(all_document_words)

    for word in tables_words:
        if "$" in word:
            for amount in money_list:
                if amount in word:
                    money_list.remove(amount)

    if len(money_list) > 0:
        data = {
            "number_of_missing": len(money_list),
            "missing_amounts" : money_list,
            "pass_fail": "Failed" 
        }
    else:
        data = {
            "number_of_missing": len(money_list),
            "missing_amounts" : money_list,
            "pass_fail": "Passed" 
        }

    return data

# -------------- Start Document Check

def start_document_check(all_document_words, csv_table):
    tables_words = table_list(csv_table)
    check = check_tables(tables_words, all_document_words)

    if check["pass_fail"] == "Passed": 
        # Green True
        print(f"=====> CHECK: \033[92m{check}\033[0m")
    else: 
        # Red False
        print(f"=====> CHECK: \033[91m{check}\033[0m")

    return check

# -------------- Start Bucket Check

def start_bucket_check(bucket, limit=None, start=0):
    file_list = get_documents(bucket)
    job_dict = {}

    if limit is not None:
        end = start + limit
    else:
        end = len(file_list)

    if end > len(file_list):
        raise Exception("Range out of bounds")

    for document in file_list[start:end]:
        words_id = start_words_analysis(document)
        tables_id = start_tables_analysis(document)
        print(f"====> Document: \033[94m{document}\033[0m")
        print(f"====> Words Job ID: \033[93m{words_id}\033[0m")
        print(f"====> Tables Job ID: \033[93m{tables_id}\033[0m")

        job_dict[document] = {
            "words_id": words_id,
            "tables_id": tables_id
        }

    return job_dict

# -------------- Get Bucket Results

def get_bucket_results(bucket, jobs_dict):
    file_list = get_documents(bucket)
    passed = []
    failed = []
    missing = {}

    for key in file_list:
        words_id = jobs_dict[key].get('words_id')
        tables_id = jobs_dict[key].get('tables_id')
        all_document_words = get_words_data(words_id)
        csv_table = get_table_data(tables_id)
        check = start_document_check(all_document_words, csv_table)

        if check["pass_fail"] == "Passed": 
            passed.append(key)
        else: 
            missing[key] = check["missing_amounts"]
            failed.append(key)

    results = {
        "Total": len(passed) + len(failed),
        "Passed Count": len(passed),
        "Failed Count": len(failed),
        "Passed List": passed,
        "Failed List": failed,
        "Missing Amounts": missing
    }

    return results