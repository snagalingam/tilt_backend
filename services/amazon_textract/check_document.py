import os
import boto3
import datetime
import json
from dateutil.relativedelta import relativedelta
from .get_tables import start_tables_extraction, get_table_data
from .get_words import start_words_extraction, get_words_data

access_key = os.environ.get("AWS_ACCESS")
secret_key = os.environ.get("AWS_SECRET")
region = os.environ.get("REGION")
bucket_name = os.environ.get("BUCKET")
#Get the document from S3
resource = boto3.resource(
    's3',     
    region_name=region,
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key)

client = boto3.client(
    's3',     
    region_name=region,
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key)

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

def delete_document(bucket_name, document):
    client.delete_object(
        Bucket=bucket_name,
        Key=document,
    )
    print(f"DELETED: {document}")

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

def strip_money_string(word):
    start_index = word.index("$")
    stripped = word[start_index:].strip()
    last_char = stripped[-1]
    new_word = None
    end_index = None

    # NUMBERS on line 26
    if last_char in NUMBERS:
        new_word = stripped
    else:
        if last_char == ",":
            end_index = stripped.index(",")
        elif " " in stripped:
            end_index = stripped.index(" ")
        elif "." in stripped:
            end_index = stripped.index(".")
        elif "*" in stripped:
            end_index = stripped.index("*")

        new_word = stripped[0:end_index]
    
    return new_word

def money_list(words):
    money_words = []
    dollar_signs = []

    for word in words:
        if "$" in word:
            dollar_signs.append(word)

    for check_word in dollar_signs:
        # NUMBERS on line 26
        if check_word[0] == "$" and check_word[-1] in NUMBERS:
            money_words.append(check_word)
        else:
            new_word = strip_money_string(check_word)
            money_words.append(new_word)

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

def check_tables(tables, words):
    money = money_list(words)

    for table_word in tables:
        for amount in money:
            if amount in table_word:
                money.remove(amount)
                break

    if len(money) > 0:
        data = {
            "number_of_missing": len(money),
            "missing_amounts" : money,
            "pass_fail": "Failed" 
        }
    else:
        data = {
            "number_of_missing": len(money),
            "missing_amounts" : money,
            "pass_fail": "Passed" 
        }

    return data

def document_check(words, tables):
    tables_words = table_list(tables)
    check = check_tables(tables_words, words)

    if check["pass_fail"] == "Passed": 
        # Green True
        print(f"=====> CHECK: \033[92m{check}\033[0m")
    else: 
        # Red False
        print(f"=====> CHECK: \033[91m{check}\033[0m")

    return check

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
        words_id = start_words_extraction(document)
        tables_id = start_tables_extraction(document)
        print(f"====> Document: \033[94m{document}\033[0m")
        print(f"====> Words Job ID: \033[93m{words_id}\033[0m")
        print(f"====> Tables Job ID: \033[93m{tables_id}\033[0m")

        job_dict[document] = {
            "words_id": words_id,
            "tables_id": tables_id
        }

    return job_dict

def get_bucket_check(bucket, jobs_dict):
    file_list = get_documents(bucket)
    passed = []
    failed = []
    missing = {}

    for key in file_list:
        words_id = jobs_dict[key].get('words_id')
        tables_id = jobs_dict[key].get('tables_id')
        w = get_words_data(words_id)
        t = get_table_data(tables_id)
        check = document_check(w, t)

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
