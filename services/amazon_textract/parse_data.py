import csv
import json
import time
import math
from .get_tables import get_table_data

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
        end = money.rindex(",")
        money = money[0:end]

    return money

def dict_builder(arr):
    words = {}
    first = 1
    last = len(arr)

    if len(arr) < 2:
        return words
    else:
        for idx in range(first, last):
            stripped = arr[idx].replace('"', "")
            money = format_money(stripped)
            words[f'Col-{idx}'] = money

    return words

def parse_tables(source):
    table_dict = {}
    arr = source.split("\n\n")
    row = 0
    header = None

    for line in arr:
        if len(line) < 1:
            continue

        if line[0:13] == "Table: Table_":
            row = 0

        if len(line) > 0: 
            if row == 0:
                header = line
                table_dict[header] = {}
            else:
                table_arr = line.split(",\n")

                for each_row in table_arr:
                    row_arr = each_row.split('","')
                    title = row_arr[0].replace('"', "")

                    table_dict[header][title] = dict_builder(row_arr)
            # keeps track of row num
        row += 1

    return table_dict

def money_check(word):
    if len(word) < 1:
        return False
    elif word[0] == "$":
        return True

    return False

def clean_money(col_data):
    amount = None

    if len(col_data) == 1:
        first = col_data['Col-1']

        if "$" in first:
            amount = first 

    elif len(col_data) > 1:
        check = {}
            
        # check for max value money
        for key in col_data:
            temp = col_data[key]

            if len(temp) > 0 and temp[0] == "$":
                integers = temp[1:].replace(',', "")
                check[int(integers)] = temp

            if len(check) > 0:
                max_int = max(check.keys())
                amount = check[max_int]

    # if money return integers else return None
    return amount

def format_data(table_dict):
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
    table_list = list(table_dict.keys())

    for table in table_list:
        table_data = table_dict[table]

        for row_title in table_data:
            row_list = list(table_data.keys())
            col_data = table_data[row_title]

            for key in keywords: 
                if key in row_title.lower():
                    # check for dup keys
                    if row_title not in seen:
                        seen.append(row_title)
                        amount = clean_money(col_data)
                        if amount is not None:
                            formatted[row_title] = amount 
                    else:
                        for value in col_data.values():
                            if money_check(value):
                                amount = clean_money(col_data)
                                current_amt = int(amount[1:].replace(',', ""))
                                existing_amt = int(formatted[row_title][1:].replace(',', ""))

                                # if row_title is dup apply greatest dollar amount
                                if current_amt > existing_amt:
                                    formatted[row_title] = amount

                    # print_variables(key=key, row_title=row_title, seen=seen, tracker=None)                                

    if len(formatted) > 0:
        return formatted
    else:
        return False


def track_position(formatted_data, parsed_table):
    seen = []
    tracker = {}
    table_list = list(parsed_table.keys())

    for table in table_list:
        table_data = parsed_table[table]
        table_num = table_list.index(table) + 1
        tracker[f'Table_{table_num}'] = []

        for row_title in table_data:
            row_list = list(table_data.keys())
            row_values = list(table_data[row_title].values())

            for key in formatted_data: 
                if key == row_title and row_title not in seen:
                    seen.append(row_title)
                    row_num = row_list.index(row_title)
                    amount = formatted_data[key]
                    col_num = row_values.index(amount) + 1
                    integer = amount[1:].replace(',', "")
                    row_data = [key,]

                    for each in table_data[key].values():
                        row_data.append(each)

                    data = {
                        "Name": key,
                        "Amount": int(integer),
                        "Row Index": row_num,
                        "Col Index": col_num,
                        f"Row Data": row_data
                    }

                    tracker[f'Table_{table_num}'].append(data)

    return tracker
    
def get_aid_data(csv_data, name):
    parsed = parse_tables(csv_data)
    formatted = format_data(parsed)

    if formatted:
        pos = track_position(formatted, parsed)
    else:
        pos = { "Document Error": name }

    return pos

def find_aid_category(name):
    single = {
        "tuition": "tuition",
        "fees": "fees",
        "room": "room",
        "meals": "meals",
        "books": "books",
        "pell": "pell",
        "seog": "seog",
        "plus": "plus",
        "unsub": "unsubsidized",
        "unsubsidized": "unsubsidized",
        "sub": "subsidized",
        "subsidized": "subsidized",
    }

    multi = {
        "il": "il map",
        "map": "il map",
        "cost": "total direct cost",
        "costs": "total direct cost",
        "personal": "personal expenses",
        "expense": "personal expenses",
        "expenses": "personal expenses",
        "health": "health insurance",
        "insurance": "health insurance",
        "off": "off campus housing",
        "on": "on campus housing",
        "housing": "housing",
        "stafford": "stafford loan fees",
        "grant": "grant",
        "scholarship": "grant",
        "work": "work study",
        "loan": "other loan",
    }

    total = {
        "indirect": "total indirect cost",
        "defined by school": "total cost defined by school",
        "total": "total cost defined by school",
        "grants": "total grants", 
        "loans": "total loans",
        "aid": "total aid",
    }

    net_price = {       
        "defined by school": "net price defined by school",
        "after grants": "net price after grants",
        "after grants and loans": "net price after grants and loans",
    }

    try: 
        index = name.index(" ")
    except:
        index = None 

    possibility = []

    if type(index) is int:
        name_split = name.split(" ")

        for n in name_split:
            each = n.lower()

            if each in single:
                possibility.append(single[each])
            elif each in multi:
                possibility.append(multi[each])
            elif each in total:
                possibility.append(total[each])
            elif each in net_price:
                possibility.append(net_price[each])
    else:
        each = name.lower()

        if each in single:
            possibility.append(single[each])
        elif each in multi:
            possibility.append(multi[each])
        elif each in total:
            possibility.append(total[each])
        elif each in net_price:
            possibility.append(net_price[each])

    if len(possibility) < 1:
        possibility = ["uncategorized"]

    data = {
        "name": name,
        "category": possibility
    }
    
    return "fees"
