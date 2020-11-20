import os
import boto3
import time
import json
import csv
import re
import asyncio
from .get_tables import start_tables_extraction, get_table_data
from .get_words import start_words_extraction, get_words_data

access_key = os.environ.get("AWS_ACCESS")
secret_key = os.environ.get("AWS_SECRET")
region = os.environ.get("REGION")
bucket_name = os.environ.get("BUCKET")

s3 = boto3.resource(
    's3',     
    region_name=region,
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key)

def get_documents(bucket_name, limit=None):
    try:
        bucket = s3.Bucket(bucket_name)

    except Exception as e:
        print(f"""
            GET BUCKET ======> ERROR
            {e}
            """)
        return e

    file_list = []

    for obj in bucket.objects.limit(limit):
        file_list.append(obj.key)

    return file_list

def strip_money_string(word):
    digits = {
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
                ",": True,
                ".": True,
            }
    start_index = word.index("$")
    stripped = word[start_index:]
    end_index = stripped[-1]

    if end_index in digits.keys():
        new_word = stripped
    else:
        end_index = stripped.index(" ")
        new_word = stripped[0:end_index]

    return new_word

def money_list(words):
    money = []
    word_list = []
    digits = {
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

    for word in words:
        if "$" in word:
            word_list.append(word)

    for check_word in word_list:
        if check_word[0] != "$" or check_word[-1] not in digits.keys():
            new_word = strip_money_string(check_word)
            money.append(new_word)
        else:   
            money.append(check_word)

    return money

def table_list(csv_obj):
    tables = csv_obj.split()
    table_list = []

    for word in tables:
        if word != " ":
            if word[0] == ",":
                new_word = word[1:]
                table_list.append(new_word)
            else:
                table_list.append(word)

    return table_list

def check_tables(tables, words):
    money = money_list(words)
    not_found = []

    for table_word in tables:
        for amount in money:
            if amount in table_word:
                money.remove(amount)
                break

    if len(money) > 0:
        print (f"""
Missing Amounts: \033[93m{money}\033[0m""")
        return False
    else:
        return True

def document_check(words, tables):
    tables_words = table_list(tables)
    check = check_tables(tables_words, words)

    if check: 
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
        raise Exception("\033[91mRange out of bounds\033[0m")

    for document in file_list[start:end]:
        words_id = start_words_extraction(document)
        tables_id = start_tables_extraction(document)

        job_dict[document] = {
            "words_id": words_id,
            "tables_id": tables_id
        }

    return job_dict

def get_bucket_check(bucket, jobs_dict):
    file_list = get_documents(bucket)
    passed = []
    failed = []

    for key in file_list:
        words_id = jobs_dict[key].get('words_id')
        tables_id = jobs_dict[key].get('tables_id')
        w = get_words_data(words_id)
        t = get_table_data(tables_id)
        check = document_check(w, t)

        if check: 
            passed.append(key)
        else: 
            failed.append(key)

    results = {
        "Total": len(passed) + len(failed),
        "Passed Count": len(passed),
        "Failed Count": len(failed),
        "Passed List": passed,
        "Failed List": failed
    }

    return results