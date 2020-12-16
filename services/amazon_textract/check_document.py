import os
import boto3
import datetime
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