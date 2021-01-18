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


################################################
# Standard Model Definitions
################################################

def start_document_check(text, tables):
    # create a list of all money in the document
    money_words = []
    for word in text:
        if "$" in word:

            # what the hell does this do
            if word.count("$") > 1 and word[1] != "$":
                return word

            start_index = word.index("$")
            formatted_money = word[start_index:].strip()

            # remove any of these symbols
            for letter in "*=+-":
                if letter in formatted_money:
                    formatted_money = formatted_money.replace(letter, "")

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


            money_words.append(money)

    # create a list of words from table
    for table in tables:
        for row in table:
            for column in row:
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

    if check["pass_fail"] == "Passed":
        # Green True
        print(f"=====> CHECK: \033[92m{check}\033[0m")
    else:
        # Red False
        print(f"=====> CHECK: \033[91m{check}\033[0m")

    return check



# -------------- Change Money to Integer

def change_to_int(word):
    if len(word) < 4 or "$" not in word:
        return word

    money = format_money(word)
    money = money[1:].replace(",", "")

    return int(money)

# -------------- Tests For Clean Money

def test_money(money):
    if len(money) > 1 and money[0] == "$":
        return type(change_to_int(money)) is int

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

    # check for blanks
    if len(max_check) < 1:
        return 0

    index = max(max_check)
    return max_check[index]

# -------------- Formats Money or Or Returns Non-money words

def check_if_money(word):
    if "$" not in word or len(word) < 3:
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
        "9": True
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

    # check for dups money in one string
    if word.count("$") > 1:
        money = get_max_amount(word=word)

    # from check_document.py
    money = format_money(money)

    # for money with only dollar sign
    if len(money) == 1:
        money = money + "0"

    return money

# -------------- Creates Dictionary for Col-Index Values

def dict_builder(arr):
    if len(arr) < 2:
        return {}

    words = {}
    first = 1
    last = len(arr)

    for idx in range(first, last):
        word = arr[idx].replace('"', "")

        # check for blank words
        if len(word) < 1:
           words[f'Col-{idx}'] = word
        else:
            # remove comma on last char
            if word[-1] == ",":
              word = word[0:-1]

            words[f'Col-{idx}'] = check_if_money(word)

    return words

# -------------- Parse Original CSV Tables Into A Table Dictionary

def parse_tables(source):
    table_dict = {}
    arr = source.split("\n")
    row = 0
    header = None

    for line in arr:
        # skip empty rows
        if len(line) < 1:
            continue
        # reset row index at new table
        elif line[0:13] == "Table: Table_":
            row = 0

        # if data exist in row iterate
        if len(line) > 0:
            if row == 0:
                header = line
                table_dict[header] = {}
            else:
                row_arr = line.split('","')
                title = row_arr[0].replace('"', "")

                if len(row_arr) > 1:
                    row_arr = row_arr[1:]

                values = dict_builder(row_arr)
                if values:
                    table_dict[header][title] = values

        # keeps track of row num
        row += 1

    return table_dict

# -------------- Format Table Dictionary For Titles And Highest Amounts

def format_data_to_max_amounts(table_dict):
    formatted_max = {}
    table_list = list(table_dict.keys())

    # for each table in document
    for table in table_list:
        table_data = table_dict[table]
        table_num = table[7:]
        formatted_max[table_num] = {}

        # for each title in table
        for row_title in table_data:
            col_data = table_data[row_title]
            amount = get_max_amount(col_data=col_data)

            if amount == 0:
                amount = "$0"

            formatted_max[table_num][row_title] = amount

    # return Falase if no formatted_max
    if len(formatted_max) < 1:
        return False

    return formatted_max

# -------------- Track Rows And Cols For Final Object For Database

def track_position(formatted_max, table_dict):
    seen = []
    tracker = {}
    table_list = list(table_dict.keys())

    for table in table_list:
        table_data = table_dict[table]
        table_num = table[7:]
        tracker[table_num] = []

        for row_title in table_data:
            row_list = list(table_data.keys())
            row_values = list(table_data[row_title].values())

            for key in formatted_max[table_num]:
                if key == row_title and row_title not in seen:
                    seen.append(row_title)
                    row_index = row_list.index(row_title)
                    row_data = [key]
                    row_val = formatted_max[table_num][key]
                    amount = row_val
                    col_index = None

                    # check if row_val is not blank
                    if row_val and len(row_val) > 0:
                        amount = change_to_int(row_val)

                    # check if amount is in row_values
                    if row_val in row_values:
                        col_index = row_values.index(row_val) + 1

                    for each in table_data[key].values():
                        row_data.append(each)

                    if amount == "$0":
                        amount = 0

                    data = {
                        "Name": key,
                        "Amount": amount,
                        "Row Index": row_index,
                        "Col Index": col_index,
                        "Row Data": row_data
                    }

                    tracker[table_num].append(data)
    return tracker

# -------------- Method To Start Operations

def get_aid_data(csv_data, document_name):
    table_dict = parse_tables(csv_data)
    formatted_max = format_data_to_max_amounts(table_dict)
    pos = { "Document Error": document_name }

    if formatted_max:
        pos = track_position(formatted_max, table_dict)

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
        "total": "total",
        "award": "other grant",
    }

    try:
        index = name.index(" ")
    except:
        index = None

    possibility = []

    # split string with spaces
    if type(index) is int:
        name_list = name.split(" ")

        for ele in name_list:
            each = ele.lower()
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

    if "tuition" in category and "other grant" in category:
        return "other grant"

    elif "total" in category:
        if "work" in name.lower():
            return "work study"
        elif "grant" in name.lower():
            return "total grants"
        elif "loan" in name.lower():
            return "total loans"
        elif "aid" in name.lower():
            return "total aid"
        return "total cost"

    return category[0]
