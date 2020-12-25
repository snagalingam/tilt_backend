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


# -------------- Format Money String 

def format_money(word):
    if word.count("$") > 1 and word[1] != "$":
        return word

    start_index = word.index("$")
    formatted_money = word[start_index:].strip()

    if "*" in formatted_money:
        formatted_money = formatted_money.replace("*", "")

    if "=" in formatted_money:
        formatted_money = formatted_money.replace("=", "")

    if "+" in formatted_money:
        formatted_money = formatted_money.replace("+", "")

    if "-" in formatted_money:
        formatted_money = formatted_money.replace("-", "")

    if " " in formatted_money:
        idx = formatted_money.index(" ")
        if formatted_money[idx + 1] in NUMBERS:
            formatted_money.replace(" ", "")
        else:
          formatted_money = formatted_money[0:idx]
    
    if "/" in formatted_money:
        idx = formatted_money.index("/")
        formatted_money = formatted_money[0:idx]

    if formatted_money[-1] == ",":
        formatted_money = formatted_money[0:-1]
    
    if formatted_money[-1] == ".":
        formatted_money = formatted_money[0:-1]

    if formatted_money[-3:-2] == ".":
        formatted_money = formatted_money[0:-3]

    if formatted_money[-3:-2] == ",":
        formatted_money = formatted_money[0:-3]

    if "." in formatted_money:
        formatted_money = formatted_money.replace(".", ",")

    return formatted_money

# -------------- Create List Of All Money In Document

def document_money_list(all_document_words):
    money_words = []

    for word in all_document_words:
        if "$" in word:
            money = format_money(word)
            money_words.append(money)

    return money_words

# -------------- Create List Of Words From Table

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


# -------------- Create List Of Words From Table

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

# -------------- Check Document Pass/Fail

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

