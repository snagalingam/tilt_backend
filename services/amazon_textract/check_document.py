import os
import boto3
import time
import json
import csv
import re
import asyncio
from get_tables import get_tables
from get_words import get_words

access_key = os.environ.get("AWS_ACCESS")
secret_key = os.environ.get("AWS_SECRET")
region = "us-east-2"   
bucket_name = "financial-letters"
#Get the document from S3
s3 = boto3.resource(
    's3',     
    region_name=region,
    aws_access_key_id=access_key, 
    aws_secret_access_key=secret_key)

# for bucket in s3.buckets.all():
#     print(f' ===> {bucket.name}')


def get_documents(bucket_name):
    try:
        bucket = s3.Bucket(bucket_name)

    except Exception as e:
        print(f"""
            GET BUCKET ======> ERROR
            {e}
            """)
        return e

    file_list = []

    for obj in bucket.objects.all():
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


def check_document(document):
    words = get_words(document)
    get_tables_words = get_tables(document)
    tables = table_list(get_tables_words)
    check = check_tables(tables, words)

    if check: 
        # Green True
        print(f"\033[94m{document}\033[0m =====> CHECK: \033[92m{check}\033[0m")
    else: 
        # Red False
        print(f"\033[94m{document}\033[0m =====> CHECK: \033[91m{check}\033[0m")

    return check


def check_bucket(bucket):
    file_list = get_documents(bucket)
    passed = []
    failed = []

    for document in file_list[7:10]:
        check = check_document(document)
        if check: 
            passed.append(document)
        else: 
            failed.append(document)

    print(f"====> \033[94mTOTAL:\033[0m {len(passed) + len(failed)}")
    print(f"====> \033[92mPASSED:\033[0m {len(passed)}")
    print(f"====> Passed List: \033[93m{passed}\033[0m")
    print(f"====> \033[91mFAILED:\033[0m {len(failed)}")
    print(f"====> Failed List: \033[93m{failed}\033[0m")

    results = {
        "Total": len(passed) + len(failed),
        "Passed Count": len(passed),
        "Failed Count": len(failed),
        "Passed List": passed,
        "Failed List": failed
    }

    return results

# check_bucket("financial-letters")
# check_document('Alexandro Sanchez_Robert Morris University Illinois.pdf')

def local_check():
    words_file = "textract_words"
    docs = json.load(open(f'{words_file}.json'))

    for doc in docs:
        for key in doc.keys():
            words = doc[key]
            tables_file = "textract_tables"
            get_tables_words = open(f'textract_tables/{key}.csv', 'r')
            tables = table_list(get_tables_words.read())
            check = check_tables(tables, words)

            if check: 
                # Green True
                print(f"\033[94m{key}\033[0m =====> CHECK: \033[92m{check}\033[0m")
            else: 
                # Red False
                print(f"\033[94m{key}\033[0m =====> CHECK: \033[91m{check}\033[0m")

# local_check()
