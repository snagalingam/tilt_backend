TOTAL_VALUES = {
    # total costs (unknown)
    "total cost": "total cost defined by school",
    "total estimated insitutional cost": "total cost defined by school",
    "total coa": "total cost defined by school",
    # total direct costs
    "direct cost": "total direct cost",
    "total estimated institutional costs": "total direct cost",
    # total indirect costs
    "total indirect cost": "total indirect cost",
    # total aid (grants and loans?)
    "total financial aid": "total aid",
    "total aid": "total aid",
    # net price
    "out of pocket": "net price defined by school",
    # total grants
    "total scholarship": "total grants",
    "total grant": "total grants",
    # total loans
    "total student loan": "total loans",
    "total federal loan": "total loans",
    # net price after grants
    "estimated cost to you after scholarhip": "net price after grants",
    # net price after grants and loans
    "estimated cost to you after student loan": "net price after grants and loans",

}

FIRST_LOOK_VALUES = {
    # tuition
    "tuition": "tuition",
    # room
    "room": "room",
    # pell grant
    "pell grant": "pell",
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
    "supp educ opport grant": "seog"
}

SECOND_LOOK_VALUES = {
    # fees
    "fees": "fees",
    # books and supplies
    "books": "books",
    # personal expenses
    "personal expense": "personal expenses",
    # subsidized loan
    "subsidized": "subsidized",
    "direct sub": "subsidized",
    # plus loan
    "plus loan": "plus",
    # other grant aid
    "aid": "other grant",
    "scholarship": "other grant",
    "grant": "other grant",
    "award": "other grant",
    # other loans
    "loan": "other loan",
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
                # remove any of these symbols
                for letter in "$,*=+-":
                    if letter in word:
                        word = word.replace(letter, "")

                text_money_list.append(int(float(word)))

    print(text_money_list)
    # create a list of all money in the tables
    for table_index, table_value in tables.items():
        for row_index, row_value in table_value.items():
            for column_index, cell in row_value.items():
                # splits the text in case multiple values
                text_values = cell.split(" ")

                for value in text_values:
                    if "$" in value:
                        for letter in "$,*=+-":
                            if letter in value:
                                value = value.replace(letter, "")

                        print(value)
                        if int(float(value)) in text_money_list:
                            text_money_list.remove(int(float(value)))

    if len(text_money_list) > 0:
        data = {
            "automated_review_succeeded": False,
            "comparison_missing_amounts" : text_money_list,
            "comparison_missing_num": len(text_money_list)
        }
    else:
        data = {
            "automated_review_succeeded": True,
            "comparison_missing_amounts" : None,
            "comparison_missing_num": 0
        }

    return data

################################################################################
# Categorize all aid data
################################################################################
def parse_data(tables):
    # if the report has three or more tables, delete the last two tables
    # from our sample of reports, these tables are repeated tables to show fall and spring data
    aid_data = []
    errors= []
    num_tables = len(tables.keys())
    if num_tables >= 3:
        del my_dict[num_tables]
        del my_dict[num_tables - 1]

    for table_num, table_value in tables.items():
        for row_num, row_value in table_value.items():
            row_text = []

            num_columns = len(row_value.keys())
            for key, value in row_value.items():
                row_text.append(value)

            row_max_amount = 0
            row_contains_money = False

            for text in row_text:

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
                        if int(float(value)) < 10:
                            if "." in value:
                                value = value.replace(".", ",")

                        # get the greatest dollar amount in each row
                        if int(float(value)) > row_max_amount:
                            row_max_amount = int(value)

            if row_contains_money:
                aid_category = None

                # lower case the entire string
                row_text_lower = [string.lower() for string in row_text]

                for key, value in TOTAL_VALUES.items():
                    # searches through lower case string for keys
                    result = [text for text in row_text_lower if key in text]
                    if result:
                        aid_category = value
                        text_position = row_text_lower.index(text) - 1
                        name = row_text[text_position]
                        break

                if aid_category is None:
                    for key, value in FIRST_LOOK_VALUES.items():
                        # searches through lower case string for keys
                        result = [text for text in row_text_lower if key in text]
                        if result:
                            aid_category = value
                            text_position = row_text_lower.index(text) - 1
                            name = row_text[text_position]
                            break

                if aid_category is None:
                    for key, value in SECOND_LOOK_VALUES.items():
                        # searches through lower case string for keys
                        result = [text for text in row_text_lower if key in text]
                        if result:
                            aid_category = value
                            text_position = row_text_lower.index(text) - 1
                            name = row_text[text_position]
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
