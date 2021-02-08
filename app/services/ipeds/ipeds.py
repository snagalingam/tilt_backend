import json
import os
import pandas as pd
import pytz

from datetime import datetime


ACCEPTABLE_OPTIONS = ["R", "P"]
FIXTURES_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")), "fixtures/")
SCRIPT_DIR = os.path.dirname(__file__)
FIELDS = {
    "fees_in_state": "CHG2AF3",
    "fees_out_of_state": "CHG3AF3",
    "other_expenses_off_campus_not_with_family": "CHG8AY3",
    "other_expenses_off_campus_with_family": "CHG9AY3",
    "other_expenses_on_campus": "CHG6AY3",
    "room_on_campus": "CHG5AY3",
    "room_off_campus_not_with_family": "CHG7AY3",
    "tuition_in_state": "CHG2AT3",
    "tuition_out_of_state": "CHG3AT3"
}

################################################################################
# This function loads the colleges file and spits out a json with
# the key as the unit id and the pk as the value.
################################################################################
def get_colleges_pk_based_on_unit_id():
    unit_id_college_pk = {}

    # load the json files for colleges
    with open(os.path.join(FIXTURES_DIR, 'colleges_1.json')) as f:
        colleges1 = json.load(f)

    with open(os.path.join(FIXTURES_DIR, 'colleges_2.json')) as f:
        colleges2 = json.load(f)

    # combine the second file into the first
    for college in colleges2:
        colleges1.append(college)

    # goes through and adds it to the dictionary
    for college in colleges1:
        unit_id_college_pk[college["fields"]["scorecard_unit_id"]] = college["pk"]

    # Saves the data
    filename = os.path.join(SCRIPT_DIR, 'unit_id_college_pk.json')

    if os.path.isfile(filename):
        os.remove(filename)

    with open(filename, mode='w') as outfile:
        json.dump(unit_id_college_pk, outfile, ensure_ascii=False, indent=2)


################################################################################
# This function analyzes raw data pulled from IPEDS and formats it in a way to
# add to our database.
# Website: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?goToReportId=7
################################################################################
def format_ipeds_data(file):
    data = pd.read_csv(os.path.join(SCRIPT_DIR, file))
    ipeds_list = []

    # get dictionary of unit ide with college pk value
    get_colleges_pk_based_on_unit_id()
    with open(os.path.join(SCRIPT_DIR, 'unit_id_college_pk.json')) as file:
        pks = json.load(file)

    for index, row in data.iterrows():
        fees_in_state = None
        fees_out_of_state = None
        tuition_in_state = None
        tuition_out_of_state = None

        # fees
        if (row[f'X{FIELDS["fees_in_state"]}'] in ACCEPTABLE_OPTIONS):
            fees_in_state = int(row[f'{FIELDS["fees_in_state"]}'])

        if (row[f'X{FIELDS["fees_out_of_state"]}'] in ACCEPTABLE_OPTIONS):
            fees_out_of_state = int(row[f'{FIELDS["fees_out_of_state"]}'])

        # other expenses
        if (row[f'X{FIELDS["other_expenses_off_campus_not_with_family"]}'] in ACCEPTABLE_OPTIONS):
            other_expenses_off_campus_not_with_family = int(row[f'{FIELDS["other_expenses_off_campus_not_with_family"]}'])

        # add an extra space because last column
        if (row[f'X{FIELDS["other_expenses_off_campus_with_family"]}'] in ACCEPTABLE_OPTIONS):
            other_expenses_off_campus_with_family = int(row[f'{FIELDS["other_expenses_off_campus_with_family"]} '])

        if (row[f'X{FIELDS["other_expenses_on_campus"]}'] in ACCEPTABLE_OPTIONS):
            other_expenses_on_campus = int(row[f'{FIELDS["other_expenses_on_campus"]}'])

        # room
        if (row[f'X{FIELDS["room_on_campus"]}'] in ACCEPTABLE_OPTIONS):
            room_on_campus = int(row[f'{FIELDS["room_on_campus"]}'])

        if (row[f'X{FIELDS["room_off_campus_not_with_family"]}'] in ACCEPTABLE_OPTIONS):
            room_off_campus_not_with_family = int(row[f'{FIELDS["room_off_campus_not_with_family"]}'])

        # tuition
        if (row[f'X{FIELDS["tuition_in_state"]}'] in ACCEPTABLE_OPTIONS):
            tuition_in_state = int(row[f'{FIELDS["tuition_in_state"]}'])

        if (row[f'X{FIELDS["tuition_out_of_state"]}'] in ACCEPTABLE_OPTIONS):
            tuition_out_of_state = int(row[f'{FIELDS["tuition_out_of_state"]}'])

        # unit id
        unit_id = row["UNITID"]

        # date
        date = datetime.now(pytz.timezone('America/Los_Angeles')).isoformat()

        # short term fix to only pull colleges we have in our database from scorecard
        try:
            pk = pks[f"{unit_id}"]
            ipeds_seed = {
                "model": "colleges.Ipeds",
                "pk": index + 1,
                "fields": {
                    "college": pks[f"{unit_id}"],
                    "unit_id": unit_id,
                    "fees_in_state": fees_in_state,
                    "fees_out_of_state": fees_out_of_state,
                    "other_expenses_off_campus_with_family": other_expenses_off_campus_with_family,
                    "other_expenses_off_campus_not_with_family": other_expenses_off_campus_not_with_family,
                    "other_expenses_on_campus": other_expenses_on_campus,
                    "room_on_campus": room_on_campus,
                    "room_off_campus_not_with_family": room_off_campus_not_with_family,
                    "tuition_in_state": tuition_in_state,
                    "tuition_out_of_state": tuition_out_of_state,
                    "created": date,
                    "updated": date
                }
            }
            ipeds_list.append(ipeds_seed)
        except:
            pass

    ########################################################################
    # Replaces any fixtures files that already exists with new data
    ########################################################################
    ipeds_filename = os.path.join(FIXTURES_DIR, f'ipeds.json')

    if os.path.isfile(ipeds_filename):
        os.remove(ipeds_filename)

    with open(ipeds_filename, mode='w') as outfile:
        json.dump(ipeds_list, outfile, ensure_ascii=False, indent=2)


format_ipeds_data(file="ic2019_ay.csv")
