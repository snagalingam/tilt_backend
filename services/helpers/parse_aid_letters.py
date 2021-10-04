import re


################################################################################
# Categories for text
################################################################################
TOTAL_VALUES = {
    # total costs (unknown)
    "total cost": "total cost defined by school",
    "total estimated insitutional cost": "total cost defined by school",
    "total coa": "total cost defined by school",
    "cost of attendance": "total cost defined by school",
    # total direct costs
    "direct cost": "total direct cost",
    "total estimated institutional costs": "total direct cost",
    # total indirect costs
    "total indirect cost": "total indirect cost",
    # total aid (grants and loans?)
    "total financial aid": "total aid defined by school",
    "total aid": "total aid defined by school",
    "aid year total": "total aid defined by school",
    # net price
    "out of pocket": "net price defined by school",
    # total grants
    "total scholarship": "total grants",
    "total grant": "total grants",
    # total loans
    "total federal loan": "total loans",
    "total federal student loan": "total loans",
    "total student loan": "total loans",
    "total loan options": "total loans",
    # net price after grants
    "estimated cost to you after scholarhip": "net price after grants",
    # net price after grants and loans
    "estimated cost to you after student loan": "net price after grants and loans",
    # other totals
    "total": "total unknown",
    "cost after grants": "net price defined by school",
    # grants
    "tuition grant": "other grant",
    "housing grant": "other grant"
}

FIRST_LOOK_VALUES = {
    # tuition
    "tuition": "tuition",
    # room
    "room": "room",
    "housing": "room",
    "living allowance": "room",
    # pell grant
    "pell grant": "pell",
    "federal pell": "pell",
    # unsubsidized loan
    "unsubsidized": "unsubsidized",
    "direct unsub": "unsubsidized",
    "unsub": "unsubsidized",
    # il map grant
    "il map": "il map",
    # work study
    "work study": "work study",
    "work-study": "work study",
    "work/study": "work study",
    # seog grant
    "seog": "seog",
    "supp educ opport grant": "seog",
    "federal sup. ed. opp. grant": "seog",
    "federal suppl educ oppor grant": "seog",
    # loan fees
    "loan fees": "stafford loan fees"
}

SECOND_LOOK_VALUES = {
    # fees
    "fees": "fees",
    # books and supplies
    "books": "books",
    "book allowance": "books",
    # personal expenses
    "personal expense": "personal expenses",
    "personal": "personal expenses",
    "miscellaneous": "personal expenses",
    "misc. expenses": "personal expenses",
    # subsidized loan
    "subsidized": "subsidized",
    "direct sub": "subsidized",
    "(sub)": "subsidized",
    # plus loan
    "plus loan": "plus",
    # other grant aid
    "aid": "other grant",
    "scholarship": "other grant",
    "grant": "other grant",
    "award": "other grant",
    # other loans
    "loan": "other loan",
    # transportation
    "transportation": "transportation",
    "transporation": "transportation",
    # meals
    "meals": "meals",
    "board": "meals"
}


################################################################################
# Compare data received from Textract analysis for text and tables
################################################################################
def compare_tables_and_text(tables, text):
    # create a list of all money in the document
    text_money_list = []
    for line in text:
        # split the line into words
        for word in line.split(" "):
            # if there is a money sign in the word
            if "$" in word:

                # only keep numbers
                word = re.sub("[^0-9]", "", word)
                # strips spaces
                word = word.strip()
                # only looks at non-empty strings
                if word:
                    text_money_list.append(int(float(word)))

    # create a list of all money in the tables
    for table_index, table_value in tables.items():
        for row_index, row_value in table_value.items():
            for column_index, cell in row_value.items():
                # only looks at cells with values
                if cell:
                    # splits the text in case multiple values
                    text_values = cell.split(" ")

                    for value in text_values:
                        if "$" in value:
                            for letter in "$,*=+-":
                                if letter in value:
                                    value = value.replace(letter, "")

                            if int(float(value)) in text_money_list:
                                text_money_list.remove(int(float(value)))

    if len(text_money_list) > 0:
        data = {
            "comparison_succeeded": False,
            "comparison_missing_amounts" : text_money_list,
            "comparison_missing_num": len(text_money_list)
        }
    else:
        data = {
            "comparison_succeeded": True,
            "comparison_missing_amounts" : None,
            "comparison_missing_num": 0
        }

    return data

################################################################################
# Categorize all aid data
################################################################################
def parse_data(tables):
    aid_data = []
    errors= []
    num_tables = len(tables.keys())
    for table_num, table_value in tables.items():
        for row_num, row_value in table_value.items():
            row_text = []

            num_columns = len(row_value.keys())
            for key, value in row_value.items():
                row_text.append(value)

            row_max_amount = 0
            row_contains_money = False

            for text in row_text:

                # only looks at text when it isn't empty
                if text:
                    # splits the text in case multiple values
                    text_values = text.split(" ")

                    for value in text_values:
                        if "$" in value:
                            row_contains_money = True
                            # remove any additional formatting
                            for letter in "$,":
                                if letter in value:
                                    value = value.replace(letter, "")

                            # checks that the value isn't weirdly low
                            # if so, textract probably recognized a comma as a decimal
                            if int(float(value)) < 10 and int(float(value)) > 0:
                                if "." in value:
                                    value = value.replace(".", ",")

                            # get the greatest dollar amount in each row
                            if int(float(value)) > row_max_amount:
                                row_max_amount = int(float(value))

                        else:
                            try:
                                # remove any additional formatting
                                for letter in "'$, ":
                                    if letter in value:
                                        value = value.replace(letter, "")

                                money = int(float(value))
                                if money != 2020 and money != 2021 and money != 2022:
                                    row_contains_money = True

                                    # get the greatest dollar amount in each row
                                    if money > row_max_amount:
                                        row_max_amount = money

                            except:
                                pass

            if row_contains_money:
                aid_category = None

                # create list of text and remove empty strings
                # create the same list with only lower case values
                text_list_lower = []
                text_list = []
                for string in row_text:
                    if string:
                        text_list.append(string)
                        text_list_lower.append(string.lower())

                text_list_lower_sorted = sorted(text_list_lower, key=len, reverse=True)

                for key, value in TOTAL_VALUES.items():
                    # searches through lower case string for keys
                    result = [text for text in text_list_lower_sorted if key in text]
                    if result:
                        aid_category = value
                        text_position = text_list_lower.index(result[0])
                        name = text_list[text_position][0:254]
                        break

                if aid_category is None:
                    for key, value in FIRST_LOOK_VALUES.items():
                        # searches through lower case string for keys
                        result = [text for text in text_list_lower_sorted if key in text]
                        if result:
                            aid_category = value
                            text_position = text_list_lower.index(result[0])
                            name = text_list[text_position][0:254]
                            break

                if aid_category is None:
                    for key, value in SECOND_LOOK_VALUES.items():
                        # searches through lower case string for keys
                        result = [text for text in text_list_lower_sorted if key in text]
                        if result:
                            aid_category = value
                            text_position = text_list_lower.index(result[0])
                            name = text_list[text_position][0:254]
                            break

                if aid_category is None:
                    errors.append({
                        "type": "Row not categorized",
                        "message": row_text
                    })

                else:
                    aid = {
                        "aid_category": aid_category,
                        "name": name,
                        "amount": row_max_amount,
                        "table_num": table_num,
                        "row_num": row_num,
                        "row_text": row_text
                    }
                    aid_data.append(aid)
    return aid_data, errors
