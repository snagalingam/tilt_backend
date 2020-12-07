import csv
import json
import time
import math

def format_money(word):

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
        "$": True }

    # base case for non-money words
    if len(word) < 1 or "/" in word or "-" in word:
        return word 
    elif word[0] not in digits.keys():
        return word

    money = word
    if word[-1] == ",": 
        money = word[0:-1]
    if money[0] != "$":
        money = "$" + money

    # check if last two digits are cents
    if ".00" == money[-3:] or ",00" == money[-3:]:
        money = money[0:-3]

    arr = money.split(" ")
    # check for period in money string
    if "." in money:
        money = money.replace(".", ",")
    # check if money has alpha chars
    elif len(arr) > 1:
        money = arr[0]

    # check for comma separating money string
    if "," not in money:
        length = len(money[1:])
        if length > 3:
            times = math.floor(length / 3)
            for num in range(times):
                idx = (num + 1) * -3
                money = money[0:idx] + "," + money[idx:]

    # final check
    if "," == money[-3:-2] or money.count(",") > 1:
        cut = money.rindex(",")
        money = money[0:cut]

    return money

def dict_builder(arr):
    words = {}

    if len(arr) < 2:
        return words
    
    first = 1
    last = len(arr)-1

    if len(arr) > 2:
        for idx in range(first, last):
            money = format_money(arr[idx])
            words[idx] = money

    return words

def parse_tables(source):
    count = 0
    table_dict = {}

    with open(f'{source}.csv', 'r') as f:
        csv_reader = csv.reader(f)
        row = 0
        header = None

        for line in csv_reader:
            if len(line) == 1:
                row = 0

            if len(line) > 0: 
                if row == 0:
                    header = line[0]
                    table_dict[header] = {}
                else:
                    title = line[0]
                    table_dict[header][title] = dict_builder(line)
            # keeps track of row num
            row += 1
    
    with open(f'{source}.json', 'w') as new_file:
        data = json.dumps(table_dict, indent=2)
        new_file.write(data)

    return table_dict

def format_data(table_dict, doc=None):
    keywords = [
        "pell grant",
        "scholarship",
        "grant",
        "subsidized",
        "unsubsidized",
        "unsub",
        "federal",
        "fed",
        "direct",
        "indirect",
        "plus",
        "stafford loan",
        "work study",
        "orientation",
        "tuition",
        "room",
        "meals",
        "books",
        "personal", 
        "expenses",
        "transportation",
        "health", 
        "insurance",
        "off campus", 
        "on campus",
        "housing",
        "loans",
        "fee",
        "total",
        "cost",
        "seog",
        "il map",
        "aid",
        "net", 
        "price",
        "grant",
        "loan",
        "non-resident",
        "resident",
        "award",
        "financial"
        ]

    formatted = {}
    seen = []

    for table in table_dict.keys():
        table_data = table_dict[table]

        for row_title in table_data:
            for key in keywords: 
                # if keywords match row_title and not dup
                if key in row_title.lower() and row_title not in seen:
                    seen.append(row_title)

    #                 print(f"""
    # key:   ===> {key}
    # title: ===> {row_title}
    # seen:  ===> {seen}
    #                 """)

                    col_data = table_data[row_title]
                    data = None

                    # For 2 column tables
                    if len(col_data) == 1:
                        first = col_data[1]
                        if "$" in first:
                            data = first

                    # Greater than 2 column tables
                    elif len(col_data) > 1:
                        check = {}
                        # check for max value money
                        for i in col_data:
                            temp = col_data[i]

                            if len(temp) > 0 and temp[0] == "$":
                                ints = temp[1:].replace(',', "")
                                check[int(ints)] = temp

                            if len(check) > 0:
                                key = max(check.keys())
                                data = check[key]

                    if data is not None:
                        formatted[row_title] = data 
    
    if len(formatted) > 0:
        return formatted
    else:
        return{ "Document Error": doc }

# parse_tables: takes csv table and formats a dict/json to rows and cols
# format_data: takes parsed data dict/json and filters for row_titles/dollars