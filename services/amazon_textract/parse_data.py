import json
import time
import math
from .get_tables import get_table_data

def json_writer(file_name, data, _type="w"):
    with open(f'{file_name}.json', f'{_type}') as new_file:
        d = json.dumps(data, indent=2)
        if _type == "+a":
            new_file.write(d + "," + "\n")
        else:
            new_file.write(d)
    # print(f'JSON: ===> {file_name} written')

def print_variables(**kwargs):
    key = kwargs.get("key")
    row_title = kwargs.get("row_title")
    seen = kwargs.get("seen")
    tracker = kwargs.get("tracker")

    print(f"""
    key:      ===> {key}
    title:    ===> {row_title}
    seen:     ===> {seen}
    tracker:  ===> {tracker}""")

# -------------- Change Money to Integer

def change_to_int(money):
    if ".00" == money[-3:] or ",00" == money[-3:]:
        money = money[1:-3]
    if "." in money:
        money = money.replace(".", "")
    if "," in money:
        money = money.replace(",", "")
    if money == "0":
        money = "$" + money
    money = int(money[1:].replace(",", ""))
    return money

# -------------- Tests For Clean Money

def test_money(money):
    if len(money) > 1 and money[0] == "$":
        if type(change_to_int(money)) is int:
            return True
    return False

# -------------- Returns Max Amount From String With Dup Money

def get_max_amount(**kwargs):
    word = kwargs.get("word", None)
    col_data = kwargs.get("col_data", None)
    max_check = {}

    if word:
        # check for space 
        try:
            split = word.index(" ")
            arr = word.split(" ")
        # if no space split on second dollar sign 
        except:
            split = word.rindex("$")
            arr = [word[0:split], word[split:]]

        for ele in arr:
            if test_money(ele):
                max_check[change_to_int(ele)] = ele
                
    elif col_data:
        for key in col_data:
            value = col_data[key]
            if test_money(value):
                max_check[change_to_int(value)] = value

    if len(max_check) > 0:
        index = max(max_check)
        return max_check[index]
    else:
        return "0"

# -------------- Formats Money or Or Returns Non-money words 

def format_money(word):
    if len(word) < 3 or len(word) > 50 or "$" not in word:
        return word

    numbers = {
        "0": True,
        "1": True,
        "2": True,
        "3": True,
        "4": True,
        "5": True,
        "6": True,
        "7": True,
        "8": True,
        "9": True }

    symbols = {
        "/": True,
        "-": True,
        "+": True,
        "=": True,
        "*": True,
        "/": True,
    }

    money = None

    # base case for non-numeric words
    for num in numbers:
        if num in word:
            money = word
            break

    # gauranteed to be money past this point
    if money is None:
        return word

    # check and remove symbols
    for symbol in symbols:
        if symbol in money:
            start = money.index("$")
            money = money[start:]
            break

    # check for dups money in one string
    if word.count("$") > 1:
        money = get_max_amount(word=word)

    # check for periods
    if ".00" == money[-3:] or ",00" == money[-3:]:
        money = money[0:-3]
    if "." in money:
        money = money.replace(".", ",")

    # check for spaces within money
    if " " in money:
        arr = money.split(" ")
        for each in arr:
            if "$" in each:
                money = each
                break

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

    if money[-1] == ",": 
        money = money[0:-1]

    if money[0] != "$":
        money = "$" + money

    # test money 
    if test_money(money):
        return money
    return word

# -------------- Formats Amounts To Verify Highest Amount Within Row

def clean_money(col_data):
    amount = None

    if len(col_data) == 1:
        first = col_data['Col-1']
        if "$" in first:
            amount = first

    elif len(col_data) > 1:
        amount = get_max_amount(col_data=col_data)

    # if money return integers else return None
    return amount

# -------------- Creates Dictionary for Col-Index Values

def dict_builder(arr):
    if len(arr) < 2:
        return {}

    words = {}
    first = 1
    last = len(arr)

    for idx in range(first, last):
        word = arr[idx].replace('"', "")
        words[f'Col-{idx}'] = format_money(word)

    return words

# -------------- Parse Original CSV Tables Into A Table Dictionary

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

                    # filter titles longer than 50 characters
                    if len(title) > 50 and len(row_arr) > 1:
                        title = row_arr[1]
                        row_arr = row_arr[1:]

                    values = dict_builder(row_arr)
                    if values:
                        table_dict[header][title] = values

        # keeps track of row num
        row += 1

    return table_dict

# -------------- Format Table Dictionary For Titles And Highest Amounts 

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
        "financial",
        ]

    formatted_data = {}
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
                            formatted_data[row_title] = amount 
                    else:
                        for value in col_data.values():
                            if test_money(value):
                                amount = clean_money(col_data)
                                current_amt = change_to_int(amount)
                                existing_amt = change_to_int(formatted_data[row_title])

                                # if row_title is dup apply greatest dollar amount
                                if current_amt > existing_amt:
                                    formatted_data[row_title] = amount                            

    if len(formatted_data) > 0:
        return formatted_data
    else:
        return False 

# -------------- Track Rows And Cols For Final Object For Database 

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
                    row_data = [key]

                    if len(formatted_data[key]) > 0:
                        amount = change_to_int(formatted_data[key])
                    else:
                        amount = formatted_data[key]

                    # check if amount is in row_values
                    if amount in row_values:
                        col_num = row_values.index(amount) + 1
                    else:
                        col_num = None

                    for each in table_data[key].values():
                        row_data.append(each)

                    data = {
                            "Name": key,
                            "Amount": amount,
                            "Row Index": row_num,
                            "Col Index": col_num,
                            f"Row Data": row_data
                    }

                    tracker[f'Table_{table_num}'].append(data)
    return tracker

# -------------- Method To Start Operations

def get_aid_data(csv_data, name):
    table_dict = parse_tables(csv_data)
    formatted_data = format_data(table_dict)

    if formatted_data:
        pos = track_position(formatted_data, table_dict)
    else:
        pos = { "Document Error": name }

    return pos

# -------------- Method To Filter Possibilties Of Aid Categories Match

def find_aid_category(name, doc_name):
    categories = {
        "tuition": "tuition",
        "fees": "fees",
        "room": "room",
        "meal": "meals",
        "books": "books",
        "pell": "pell",
        "seog": "seog",
        "plus": "plus",
        "unsub": "unsubsidized",
        "unsubsidized": "unsubsidized",
        "sub": "subsidized",
        "subsidized": "subsidized",
        "il": "il map",
        "map": "il map",
        "cost": "total direct cost",
        "personal": "personal expenses",
        "expense": "personal expenses",
        "health": "health insurance",
        "insurance": "health insurance",
        "off": "off campus housing",
        "campus": "off campus housing",
        "housing": "off campus housing",
        "stafford": "stafford loan fees",
        "grants": "total grants", 
        "loans": "total loans",
        "grant": "other grant",
        "loan": "other loan",
        "scholarship": "other grant",
        "aid": "total aid",
        "work": "work study",
        "tuition": "tuition",
        "indirect": "total indirect cost",
        "estimate": "total cost defined by school",
        "total": "totals",
        "award": "other grant",
    }

    try: 
        index = name.index(" ")
    except:
        index = None 

    possibility = []

    # split string with spaces
    if type(index) is int:
        name_split = name.split(" ")

        for n in name_split:
            each = n.lower()

            if each in categories:
                possibility.append(categories[each])

    # single words
    else:
        each = name.lower()

        if each in categories:
            possibility.append(categories[each])

    # double check 
    if len(possibility) < 1:
        for double_check in categories:
            if double_check in name.lower():
                possibility.append(categories[double_check])
    
    # set uncategorized as default
    if len(possibility) < 1:
        possibility = ["uncategorized"]

    possibilities = {
        "document": doc_name,
        "name": name,
        "category": possibility
    }

    return possibilities

# -------------- Method To Format Data To Match Database Aid Categories 

def filter_possibilities(possibilities):
    name = possibilities.get("name")
    category = possibilities.get("category")

    if len(possibilities) < 2:
        return category[0]
    else:
        if "tuition" in category and "other grant" in category:
            return "other grant"
        elif "totals" in category:
            if "work" in name.lower():
                return "work study"
            elif "grant" in name.lower():
                return "total grants"     
            elif "loan" in name.lower():
                return "total loans"
            elif "aid" in name.lower():
                return "total aid"
            return "total cost"
        else:
            return category[0]
