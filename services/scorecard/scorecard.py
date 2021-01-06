import json
import os
import pytz
import requests
import sys

from datetime import datetime
from django.conf import settings
from math import ceil
from scorecard_constants import (
    CARNEGIE_BASIC_DICT,
    CARNEGIE_SIZE_SETTING_DICT,
    CARNEGIE_SIZE_SETTING_SIZE_DICT,
    CARNEGIE_SIZE_SETTING_RESIDENTIAL_DICT,
    CARNEGIE_UNDERGRAD_DICT,
    CREDENTIAL_LEVEL_DICT,
    HIGHEST_DEGREE_AWARDED_DICT,
    INSTITUTIONAL_LEVEL_DICT,
    LOCALE_DICT,
    LOCALE_UPDATED_DICT,
    OPEN_ADMISSIONS_DICT,
    OWNERSHIP_DICT,
    PREDOMINANT_DEGREE_AWARDED_DICT,
    REGION_DICT,
    RELIGIOUS_AFFILIATION_DICT,
    STATE_FIPS_DICT,
)


FIXTURES_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")), "fixtures/")
SCORECARD_API = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
SCORECARD_KEY = "JTaStgE4XxpTtLtySKUihVrrhLKJuXgHYtvG180h"
SCRIPT_DIR = os.path.dirname(__file__)

################################################################################
# Scorecard API returns data as a set of pages. This function helps find the
# total number of pages given per_page constraints.
################################################################################
def find_total_number_of_scorecard_pages(per_page):
    # get the data
    fields = "id"
    url = f"{SCORECARD_API}?api_key={SCORECARD_KEY}&fields={fields}&per_page={per_page}"
    data = requests.get(url).json()

    # use the metadata to calculate the total number of pages
    total_records = data['metadata']['total']
    total_pages = ceil(total_records / per_page)
    return(total_pages)


################################################################################
# Returns a list of all the unit ids available through the Scorecard API
################################################################################
def list_all_scorecard_unit_ids():
    # find the total number of pages
    per_page = 100
    fields = "id"
    total_pages = find_total_number_of_scorecard_pages(per_page=per_page)
    print(f"STATUS => Total of {total_pages + 1} pages to retrieve")

    unit_ids = []

    # add ids to file
    for i in range(total_pages + 1):
        print(f"STATUS => Loading page {i + 1} from scorecard")
        url = f"{SCORECARD_API}?api_key={SCORECARD_KEY}&fields={fields}&per_page={per_page}&page={i}"
        data = requests.get(url).json()
        results = data['results']

        for item in results:
            unit_ids.append(item['id'])

    unit_ids.sort()
    print(f"STATUS => Retrieved a total of {len(unit_ids)} unit ids")

    with open('scorecard_unit_ids.json', 'w') as outfile:
         json.dump(unit_ids, outfile, indent=2, sort_keys=True)

    return(unit_ids)


################################################################################
# Pulls the raw scorecard data for one college
# Helps with debugging
################################################################################
def get_raw_college_data_by_scorecard_unit_id(unit_id):
    print(f"STATUS => Pulling scorecard data for {unit_id}")
    url = f"{SCORECARD_API}?api_key={SCORECARD_KEY}&id={unit_id}"
    request = requests.get(url).json()
    results = request.get('results')

    # print out any errors received during the request
    try:
        error = scorecard['error']
        print(f'ERROR CODE => {error["code"]}')
        print(f'ERROR MESSAGE => {error["message"]}')

    except:
        pass

    if results is None:
        sys.exit(f'ERROR => No results for college {unit_id}')

    else:
        data = results[0]
        raw_data_filename = os.path.join(SCRIPT_DIR, f'scorecard_{unit_id}.json')

        with open(raw_data_filename, mode='w') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
################################################################################
# Pulls the scorecard data for one college and saves it formatted
################################################################################
def get_formatted_college_data_by_scorecard_unit_id(file_num, pk, unit_id):
    print(f"STATUS => pulling the scorecard data for {unit_id}")
    url = f"{SCORECARD_API}?api_key={SCORECARD_KEY}&id={unit_id}"
    request = requests.get(url).json()
    results = request.get('results')

    # print out any errors received during the request
    try:
        error = scorecard['error']
        print(f'ERROR CODE => {error["code"]}')
        print(f'ERROR MESSAGE => {error["message"]}')

    except:
        pass

    if results is None:
        sys.exit(f'ERROR => No results for college {unit_id}')

    else:
        ########################################################################
        # Pulls the dictionaries we will be using
        ########################################################################
        data = results[0]
        ## school
        school = data.get('school')
        minority = school.get('minority_serving')

        ## latest
        latest = data.get('latest')
        # academics
        academics = latest.get('academics')
        program_percentage = academics.get('program_percentage')
        # admissions
        admissions = latest.get('admissions')
        act_scores = latest.get('admissions')['act_scores']
        sat_scores = latest.get('admissions')['sat_scores']
        # aid
        aid = latest.get('aid')
        mid_debt = aid.get('median_debt')
        # completion
        completion = latest.get('completion')
        # cost
        cost = latest.get('cost')
        attendance = cost.get('attendance')
        net_price = cost.get('net_price')
        net_price_public = net_price.get('public')['by_income_level']
        net_price_private = net_price.get('private')['by_income_level']
        tuition = cost.get('tuition')
        # earnings
        earnings = latest.get('earnings')
        # repayment
        repayment = latest.get('repayment')
        # student
        student = latest.get('student')
        demographics = student.get('demographics')
        retention_rate = student.get('retention_rate')

        ########################################################################
        # Saves each field we will be using
        ########################################################################
        ### basic info
        name = school.get('name')
        unit_id = data.get('id')
        ope_id = data.get('ope8_id')
        ope6_id = data.get('ope6_id')

        ### location
        city = school.get('city')
        latitude = data.get('location')['lat']
        longitude = data.get('location')['lon']
        state = school.get('state')

        state_fips_data = school.get('state_fips')
        if state_fips_data in STATE_FIPS_DICT:
            state_fips = STATE_FIPS_DICT[state_fips_data]
        else:
            sys.exit(f'ERROR => state_fips code of {state_fips_data} not in STATE_FIPS_DICT')

        zipcode = school.get('zip')

        ### general information
        alias = school.get('alias')
        if alias is None:
            alias = ""

        accreditor = school.get('accreditor')
        branches = school.get('branches')

        carnegie_basic_data = school.get('carnegie_basic')
        if carnegie_basic_data in CARNEGIE_BASIC_DICT:
            carnegie_basic = CARNEGIE_BASIC_DICT[carnegie_basic_data]
        else:
            sys.exit(f'ERROR => carnegie_basic code of {carnegie_basic_data} not in CARGENIE_BASIC_DICT')

        carnegie_size_setting_data = school.get('carnegie_size_setting')
        if carnegie_size_setting_data in CARNEGIE_SIZE_SETTING_DICT:
            carnegie_size_setting = CARNEGIE_SIZE_SETTING_DICT[carnegie_size_setting_data]
        else:
            sys.exit(f'ERROR => carnegie_size_setting code of {carnegie_size_setting_data} not in CARGENIE_SIZE_SETTING_DICT')

        carnegie_undergrad_data = school.get('carnegie_undergrad')
        if carnegie_undergrad_data in CARNEGIE_UNDERGRAD_DICT:
            carnegie_undergrad = CARNEGIE_UNDERGRAD_DICT[carnegie_undergrad_data]
        else:
            sys.exit(f'ERROR => carnegie_undergrad code of {carnegie_undergrad_data} not in CARGENIE_UNDERGRAD_DICT')


        highest_degree_awarded_data = school.get('degrees_awarded')['highest']
        if highest_degree_awarded_data in HIGHEST_DEGREE_AWARDED_DICT:
            highest_degree_awarded = HIGHEST_DEGREE_AWARDED_DICT[highest_degree_awarded_data]
        else:
            sys.exit(f'ERROR => highest_degree_awarded code of {highest_degree_awarded_data} not in HIGHEST_DEGREE_AWARDED_DICT')

        institutional_level_data = school.get('institutional_characteristics')['level']
        if institutional_level_data in INSTITUTIONAL_LEVEL_DICT:
            institutional_level = INSTITUTIONAL_LEVEL_DICT[institutional_level_data]
        else:
            sys.exit(f'ERROR => institutional_level code of {institutional_level_data} not in INSTITUTIONAL_LEVEL_DICT')

        locale_data = school.get('locale')
        if locale_data in LOCALE_DICT:
            locale = LOCALE_DICT[locale_data]
        else:
            sys.exit(f'ERROR => locale code of {locale_data} not in LOCALE_DICT')

        main_campus = bool(school.get('main_campus'))
        online_only = bool(school.get('online_only'))
        operating = bool(school.get('operating'))

        ownership_data = school.get('ownership')
        if ownership_data in OWNERSHIP_DICT:
            ownership = OWNERSHIP_DICT[ownership_data]
        else:
            sys.exit(f'ERROR => ownership code of {ownership_data} not in OWNERSHIP_DICT')

        predominant_degree_awarded_data = school.get('degrees_awarded')['predominant']
        if predominant_degree_awarded_data in PREDOMINANT_DEGREE_AWARDED_DICT:
            predominant_degree_awarded = PREDOMINANT_DEGREE_AWARDED_DICT[predominant_degree_awarded_data]
        else:
            sys.exit(f'ERROR => predominant_degree_awarded code of {predominant_degree_awarded_data} not in PREDOMINANT_DEGREE_AWARDED_DICT')

        predominant_degree_awarded_recoded_data = school.get('degrees_awarded')['predominant_recoded']
        if predominant_degree_awarded_recoded_data in PREDOMINANT_DEGREE_AWARDED_DICT:
            predominant_degree_awarded_recoded = PREDOMINANT_DEGREE_AWARDED_DICT[predominant_degree_awarded_recoded_data]
        else:
            sys.exit(f'ERROR => predominant_degree_awarded_recoded code of {predominant_degree_awarded_recoded_data} not in PREDOMINANT_DEGREE_AWARDED_DICT')

        price_calculator_url = school.get('price_calculator_url')

        region_data = school.get('region_id')
        if region_data in REGION_DICT:
            region = REGION_DICT[region_data]
        else:
            sys.exit(f'ERROR => region code of {region_data} not in REGION_DICT')

        school_url = school.get('school_url')
        under_investigation = bool(school.get('under_investigation'))

        # institution types
        minority_serving_aanipi = bool(minority.get('aanipi'))
        minority_serving_annh = bool(minority.get('annh'))
        minority_serving_hispanic = bool(minority.get('hispanic'))
        minority_serving_historically_black = bool(minority.get('historically_black'))
        minority_serving_nant = bool(minority.get('nant'))
        minority_serving_predominantly_black = bool(minority.get('predominantly_black'))
        minority_serving_tribal = bool(minority.get('tribal'))
        men_only = bool(school.get('men_only'))
        women_only = bool(school.get('women_only'))

        religious_affiliation_data = school.get('religious_affiliation')
        if religious_affiliation_data in RELIGIOUS_AFFILIATION_DICT:
            religious_affiliation = RELIGIOUS_AFFILIATION_DICT[religious_affiliation_data]
        else:
            sys.exit(f'ERROR => religious_affiliation code of {religious_affiliation_data} not in RELIGIOUS_AFFILIATION_DICT')

        ### admissions
        admissions_rate = admissions.get('admission_rate')['overall']

        open_admissions_data = school.get('open_admissions_policy')
        if open_admissions_data in OPEN_ADMISSIONS_DICT:
            open_admissions = OPEN_ADMISSIONS_DICT[open_admissions_data]
        else:
            sys.exit(f'ERROR => open_admissions code of {open_admissions_data} not in OPEN_ADMISSIONS_DICT')

        act_cumulative_25th_percentile = act_scores.get('25th_percentile')['cumulative']
        act_cumulative_75th_percentile = act_scores.get('75th_percentile')['cumulative']
        act_cumulative_midpoint = act_scores.get('midpoint')['cumulative']
        act_english_25th_percentile = act_scores.get('25th_percentile')['english']
        act_english_75th_percentile = act_scores.get('75th_percentile')['english']
        act_english_midpoint = act_scores.get('midpoint')['english']
        act_math_25th_percentile = act_scores.get('25th_percentile')['math']
        act_math_75th_percentile = act_scores.get('75th_percentile')['math']
        act_math_midpoint = act_scores.get('midpoint')['math']
        act_writing_25th_percentile = act_scores.get('25th_percentile')['writing']
        act_writing_75th_percentile = act_scores.get('75th_percentile')['writing']
        act_writing_midpoint = act_scores.get('midpoint')['writing']
        sat_average = sat_scores.get('average')['overall']
        sat_math_25th_percentile = sat_scores.get('25th_percentile')['math']
        sat_math_75th_percentile = sat_scores.get('75th_percentile')['math']
        sat_math_midpoint = sat_scores.get('midpoint')['math']
        sat_reading_25th_percentile = sat_scores.get('25th_percentile')['critical_reading']
        sat_reading_75th_percentile = sat_scores.get('75th_percentile')['critical_reading']
        sat_reading_midpoint = sat_scores.get('midpoint')['critical_reading']
        sat_writing_25th_percentile = sat_scores.get('25th_percentile')['writing']
        sat_writing_75th_percentile = sat_scores.get('75th_percentile')['writing']
        sat_writing_midpoint = sat_scores.get('midpoint')['writing']

        # undergraduate students description
        undergraduate_students = student.get('size')
        undergraduate_students_2ormore = demographics.get('race_ethnicity')['two_or_more']
        undergraduate_students_aian = demographics.get('race_ethnicity')['aian']
        undergraduate_students_asian = demographics.get('race_ethnicity')['asian']
        undergraduate_students_black = demographics.get('race_ethnicity')['black']
        undergraduate_students_hispanic = demographics.get('race_ethnicity')['hispanic']
        undergraduate_students_nhpi = demographics.get('race_ethnicity')['nhpi']
        undergraduate_students_nra = demographics.get('race_ethnicity')['non_resident_alien']
        undergraduate_students_unknown = demographics.get('race_ethnicity')['unknown']
        undergraduate_students_white = demographics.get('race_ethnicity')['white']
        undergraduate_students_parttime = student.get('part_time_share')
        undergraduate_students_men = demographics.get('men')
        undergraduate_students_women = demographics.get('women')
        age_entry = demographics.get('age_entry')
        first_generation = demographics.get('first_generation')
        share_25_older = student.get('share_25_older')
        veteran = demographics.get('veteran')

        # cost and net price fields
        avg_net_price = cost.get('avg_net_price')['public'] or cost.get('avg_net_price')['private']
        avg_net_price_lo = net_price_public.get('0-30000') or net_price_private.get('0-30000')
        avg_net_price_m1 = net_price_public.get('30001-48000') or net_price_private.get('30001-48000')
        avg_net_price_m2 = net_price_public.get('48001-75000') or net_price_private.get('48001-75000')
        avg_net_price_h1 = net_price_public.get('75001-110000') or net_price_private.get('75001-110000')
        avg_net_price_h2 = net_price_public.get('110001-plus') or net_price_private.get('110001-plus')
        cost_of_attendance = attendance.get('academic_year') or attendance.get('program_year')
        tuition_in_state = tuition.get('in_state')
        tuition_out_of_state = tuition.get('out_of_state')
        tuition_program_year = tuition.get('program_year')

        # loan and grant fields
        default_rate_2yr = repayment.get('2_yr_default_rate')
        default_rate_2yr_num_students = repayment.get('2_yr_default_rate_denom')
        default_rate_3yr = repayment.get('3_yr_default_rate')
        default_rate_3yr_num_students = repayment.get('3_yr_default_rate_denom')
        federal_loan_rate = aid.get('federal_loan_rate')
        median_debt = aid.get('loan_principal')
        median_debt_num_students = mid_debt.get('number')['overall']
        median_debt_completers = mid_debt.get('completers')['overall']
        median_debt_completers_num_students = mid_debt.get('number')['completers']
        median_debt_noncompleters = mid_debt.get('noncompleters')
        median_debt_noncompleters_num_students = mid_debt.get('number')['noncompleters']
        monthly_loan_payments = mid_debt.get('completers')['monthly_payments']
        plus_loan_median_debt = aid.get('plus_debt')['all']['all_inst']['median']
        plus_loan_median_debt_num_students =  aid.get('plus_debt')['all']['all_inst']['count']
        plus_loan_pct_lower = aid.get('plus_loan_pct_lower')
        plus_loan_pct_upper = aid.get('plus_loan_pct_upper')
        pell_grant_rate = aid.get('pell_grant_rate')
        students_with_any_loan = aid.get('students_with_any_loan')
        students_with_pell_grant = student.get('students_with_pell_grant')

        ### earnings
        not_working_not_enrolled_3yr_num_students = earnings.get('3_yrs_after_completion')['not_working_not_enrolled']['overall_count']
        working_not_enrolled_3yr_num_students = earnings.get('3_yrs_after_completion')['working_not_enrolled']['overall_count']
        over_poverty_line_3yr_num_students = earnings.get('3_yrs_after_completion')['overall_count_over_poverty_line']

        ### graduation rate fields
        graduation_rate_100 = (
            completion.get('completion_rate_4yr_100nt') or
            completion.get('completion_rate_less_than_4yr_100nt')
        )
        graduation_rate_100_num_students = (
            completion.get('completion_cohort_4yr_100nt') or
            completion.get('completion_cohort_less_than_4yr_100nt')
        )
        graduation_rate_150 = (
            completion.get('completion_rate_4yr_150nt') or
            completion.get('completion_rate_less_than_4yr_150nt')
        )
        graduation_rate_150_num_students = (
            completion.get('completion_cohort_4yr_150nt') or
            completion.get('completion_cohort_less_than_4yr_150nt')
        )
        graduation_rate_150_2ormore = (
            completion.get('completion_rate_4yr_150_2ormore') or
            completion.get('completion_rate_l4yr_150_2ormore')
        )
        graduation_rate_150_2ormore_num_students = (
            completion.get('completion_cohort_4yr_150_2ormore') or
            completion.get('completion_cohort_less_than_4yr_150_2ormore')
        )
        graduation_rate_150_aian = (
            completion.get('completion_rate_4yr_150_aian') or
            completion.get('completion_rate_l4yr_150_aian')
        )
        graduation_rate_150_aian_num_students = (
            completion.get('completion_cohort_4yr_150_aian') or
            completion.get('completion_cohort_less_than_4yr_150_aian')
        )
        graduation_rate_150_asian = (
            completion.get('completion_rate_4yr_150_asian') or
            completion.get('completion_rate_l4yr_150_asian')
        )
        graduation_rate_150_asian_num_students = (
            completion.get('completion_cohort_4yr_150_asian') or
            completion.get('completion_cohort_less_than_4yr_150_asian')
        )
        graduation_rate_150_black = (
            completion.get('completion_rate_4yr_150_black') or
            completion.get('completion_rate_l4yr_150_black')
        )
        graduation_rate_150_black_num_students = (
            completion.get('completion_cohort_4yr_150_black') or
            completion.get('completion_cohort_less_than_4yr_150_black')
        )
        graduation_rate_150_hispanic = (
            completion.get('completion_rate_4yr_150_hispanic') or
            completion.get('completion_rate_l4yr_150_hispanic')
        )
        graduation_rate_150_hispanic_num_students = (
            completion.get('completion_cohort_4yr_150_hispanic') or
            completion.get('completion_cohort_less_than_4yr_150_hispanic')
        )
        graduation_rate_150_nhpi = (
            completion.get('completion_rate_4yr_150_nhpi') or
            completion.get('completion_rate_l4yr_150_nhpi')
        )
        graduation_rate_150_nhpi_num_students = (
            completion.get('completion_cohort_4yr_150_nhpi') or
            completion.get('completion_cohort_less_than_4yr_150_nhpi')
        )
        graduation_rate_150_nra = (
            completion.get('completion_rate_4yr_150_nonresident')['alien'] or
            completion.get('completion_rate_l4yr_150_nonresident')['alien']
        )
        graduation_rate_150_nra_num_students = (
            completion.get('completion_cohort_4yr_150_nonresident')['alien'] or
            completion.get('completion_cohort_less_than_4yr_150_nonresident')['alien']
        )
        graduation_rate_150_unknown = (
            completion.get('completion_rate_4yr_150_race')['unknown'] or
            completion.get('completion_rate_l4yr_150_race')['unknown']
        )
        graduation_rate_150_unknown_num_students = (
            completion.get('completion_cohort_4yr_150_race')['unknown'] or
            completion.get('completion_cohort_less_than_4yr_150_race')['unknown']
        )
        graduation_rate_150_white = (
            completion.get('completion_rate_4yr_150_white') or
            completion.get('completion_rate_l4yr_150_white')
        )
        graduation_rate_150_white_num_students = (
            completion.get('completion_cohort_4yr_150_white') or
            completion.get('completion_cohort_less_than_4yr_150_white')
        )
        graduation_rate_150_white = (
            completion.get('completion_rate_4yr_150_white') or
            completion.get('completion_rate_l4yr_150_white')
        )

        graduation_rate_200 = (
            completion.get('completion_rate_4yr_200nt') or
            completion.get('completion_rate_less_than_4yr_200nt')
        )
        graduation_rate_200_num_students = (
            completion.get('completion_cohort_4yr_200nt') or
            completion.get('completion_cohort_less_than_4yr_200nt')
        )

        ### first time full time
        first_time_full_time = student.get('share_first')['time_full']['time']
        first_time_full_time_federal_loan_rate = aid.get('ftft_federal_loan_rate')
        first_time_full_time_pell_grant_rate = aid.get('ftft_pell_grant_rate')
        first_time_full_time_num_students = student.get('ftft_undergrads_with_pell_grant_or_federal_student_loan')

        ### retention rate
        retention_rate_full_time = (
            retention_rate.get('four_year')['full_time'] or
            retention_rate.get('lt_four_year')['full_time']
        )
        retention_rate_part_time = (
            retention_rate.get('four_year')['part_time'] or
            retention_rate.get('lt_four_year')['part_time']
        )

        ### program percentages
        program_percentage_agriculture = program_percentage.get('agriculture')
        program_percentage_architecture = program_percentage.get('architecture')
        program_percentage_biological = program_percentage.get('biological')
        program_percentage_business_marketing = program_percentage.get('business_marketing')
        program_percentage_communication = program_percentage.get('communication')
        program_percentage_communications_technology = program_percentage.get('communications_technology')
        program_percentage_computer = program_percentage.get('computer')
        program_percentage_construction = program_percentage.get('construction')
        program_percentage_education = program_percentage.get('education')
        program_percentage_engineering = program_percentage.get('engineering')
        program_percentage_engineering_technology = program_percentage.get('engineering_technology')
        program_percentage_english = program_percentage.get('english')
        program_percentage_ethnic_cultural_gender = program_percentage.get('ethnic_cultural_gender')
        program_percentage_family_consumer_science = program_percentage.get('family_consumer_science')
        program_percentage_health = program_percentage.get('health')
        program_percentage_history = program_percentage.get('history')
        program_percentage_humanities = program_percentage.get('humanities')
        program_percentage_language = program_percentage.get('language')
        program_percentage_legal = program_percentage.get('legal')
        program_percentage_library = program_percentage.get('library')
        program_percentage_mathematics = program_percentage.get('mathematics')
        program_percentage_mechanic_repair_technology = program_percentage.get('mechanic_repair_technology')
        program_percentage_military = program_percentage.get('military')
        program_percentage_multidiscipline = program_percentage.get('multidiscipline')
        program_percentage_parks_recreation_fitness = program_percentage.get('parks_recreation_fitness')
        program_percentage_personal_culinary = program_percentage.get('personal_culinary')
        program_percentage_philosophy_religious = program_percentage.get('philosophy_religious')
        program_percentage_physical_science = program_percentage.get('physical_science')
        program_percentage_precision_production = program_percentage.get('precision_production')
        program_percentage_psychology = program_percentage.get('psychology')
        program_percentage_public_administration_social_service = program_percentage.get('public_administration_social_service')
        program_percentage_resources = program_percentage.get('resources')
        program_percentage_science_technology = program_percentage.get('science_technology')
        program_percentage_security_law_enforcement = program_percentage.get('security_law_enforcement')
        program_percentage_social_science = program_percentage.get('social_science')
        program_percentage_theology_religious_vocation = program_percentage.get('theology_religious_vocation')
        program_percentage_transportation = program_percentage.get('transportation')
        program_percentage_visual_performing = program_percentage.get('visual_performing')

        ########################################################################
        # Adds fields that we created
        ########################################################################
        if carnegie_size_setting_data in CARNEGIE_SIZE_SETTING_SIZE_DICT:
            carnegie_size_setting_size = CARNEGIE_SIZE_SETTING_SIZE_DICT[carnegie_size_setting_data]
        else:
            sys.exit(f'ERROR => carnegie_size_setting code of {carnegie_size_setting_data} not in CARNEGIE_SIZE_SETTING_SIZE_DICT')

        if carnegie_size_setting_data in CARNEGIE_SIZE_SETTING_RESIDENTIAL_DICT:
            carnegie_size_setting_residential = CARNEGIE_SIZE_SETTING_RESIDENTIAL_DICT[carnegie_size_setting_data]
        else:
            sys.exit(f'ERROR => carnegie_size_setting code of {carnegie_size_setting_data} not in CARNEGIE_SIZE_SETTING_RESIDENTIAL_DICT')

        if locale_data in LOCALE_UPDATED_DICT:
            locale_updated = LOCALE_UPDATED_DICT[locale_data]
        else:
            sys.exit(f'ERROR => locale code of {locale_data} not in LOCALE_UPDATED_DICT')

        ########################################################################
        # Calculate date for created and updated fields
        ########################################################################
        date = datetime.now(pytz.timezone('America/Los_Angeles')).isoformat()

        ########################################################################
        # Calculate whether we should show college or not
        # College must be operating, have more than 0 undergrad students, and award
        # predominantly associate or bachelor's degrees
        ########################################################################
        if operating is None or undergraduate_students is None or predominant_degree_awarded is None:
            show_scorecard = False

        elif operating and undergraduate_students > 0 and predominant_degree_awarded_data < 4:
            show_scorecard = True

        else:
            show_scorecard = False

        ########################################################################
        # Saves the data
        ########################################################################
        scorecard_seed = {
            "model": "colleges.Scorecard",
            "pk": pk,
            "fields": {
                # college model
                "college": pk,

                # basic info
                "name": name,
                "unit_id": unit_id,
                "show": show_scorecard,
                "ope_id": ope_id,
                "ope6_id": ope6_id,

                # location
                "city": city,
                "latitude": latitude,
                "longitude": longitude,
                "state": state,
                "state_fips": state_fips,
                "zipcode": zipcode,

                # general information
                "alias": alias,
                "accreditor": accreditor,
                "branches": branches,
                "carnegie_basic": carnegie_basic,
                "carnegie_undergrad": carnegie_undergrad,
                "carnegie_size_setting": carnegie_size_setting,
                "carnegie_size_setting_size": carnegie_size_setting_size,
                "carnegie_size_setting_residential": carnegie_size_setting_residential,
                "highest_degree_awarded": highest_degree_awarded,
                "institutional_level": institutional_level,
                "locale": locale,
                "locale_updated": locale_updated,
                "main_campus": main_campus,
                "online_only": online_only,
                "operating": operating,
                "ownership": ownership,
                "predominant_degree_awarded": predominant_degree_awarded,
                "predominant_degree_awarded_recoded": predominant_degree_awarded_recoded,
                "price_calculator_url": price_calculator_url,
                "region": region,
                "school_url": school_url,
                "under_investigation": under_investigation,

                # institution types
                "minority_serving_aanipi": minority_serving_aanipi,
                "minority_serving_annh": minority_serving_annh,
                "minority_serving_hispanic": minority_serving_hispanic,
                "minority_serving_historically_black": minority_serving_historically_black,
                "minority_serving_nant": minority_serving_nant,
                "minority_serving_predominantly_black": minority_serving_predominantly_black,
                "minority_serving_tribal": minority_serving_tribal,
                "men_only": men_only,
                "women_only": women_only,
                "religious_affiliation": religious_affiliation,

                # admissions
                "admissions_rate": admissions_rate,
                "open_admissions": open_admissions,
                "act_cumulative_25th_percentile": act_cumulative_25th_percentile,
                "act_cumulative_75th_percentile": act_cumulative_75th_percentile,
                "act_cumulative_midpoint": act_cumulative_midpoint,
                "act_english_25th_percentile": act_english_25th_percentile,
                "act_english_75th_percentile": act_english_75th_percentile,
                "act_english_midpoint": act_english_midpoint,
                "act_math_25th_percentile": act_math_25th_percentile,
                "act_math_75th_percentile": act_math_75th_percentile,
                "act_math_midpoint": act_math_midpoint,
                "act_writing_25th_percentile": act_writing_25th_percentile,
                "act_writing_75th_percentile": act_writing_75th_percentile,
                "act_writing_midpoint": act_writing_midpoint,

                "sat_average": sat_average,
                "sat_math_25th_percentile": sat_math_25th_percentile,
                "sat_math_75th_percentile": sat_math_75th_percentile,
                "sat_math_midpoint": sat_math_midpoint,
                "sat_reading_25th_percentile": sat_reading_25th_percentile,
                "sat_reading_75th_percentile": sat_reading_75th_percentile,
                "sat_reading_midpoint": sat_reading_midpoint,
                "sat_writing_25th_percentile": sat_writing_25th_percentile,
                "sat_writing_75th_percentile": sat_writing_75th_percentile,
                "sat_writing_midpoint": sat_writing_midpoint,

                # undergraduate students description
                "undergraduate_students": undergraduate_students,
                "undergraduate_students_2ormore": undergraduate_students_2ormore,
                "undergraduate_students_aian": undergraduate_students_aian,
                "undergraduate_students_asian": undergraduate_students_asian,
                "undergraduate_students_black": undergraduate_students_black,
                "undergraduate_students_hispanic": undergraduate_students_hispanic,
                "undergraduate_students_nhpi": undergraduate_students_nhpi,
                "undergraduate_students_nra": undergraduate_students_nra,
                "undergraduate_students_unknown": undergraduate_students_unknown,
                "undergraduate_students_white": undergraduate_students_white,
                "undergraduate_students_parttime": undergraduate_students_parttime,
                "undergraduate_students_men": undergraduate_students_men,
                "undergraduate_students_women": undergraduate_students_women,
                "age_entry": age_entry,
                "first_generation": first_generation,
                "share_25_older": share_25_older,
                "veteran": veteran,

                # cost and net price fields
                "avg_net_price": avg_net_price,
                "avg_net_price_lo": avg_net_price_lo,
                "avg_net_price_m1": avg_net_price_m1,
                "avg_net_price_m2": avg_net_price_m2,
                "avg_net_price_h1": avg_net_price_h1,
                "avg_net_price_h2": avg_net_price_h2,
                "cost_of_attendance": cost_of_attendance,
                "tuition_in_state": tuition_in_state,
                "tuition_out_of_state": tuition_out_of_state,
                "tuition_program_year": tuition_program_year,

                # loan and grant fields
                "default_rate_2yr": default_rate_2yr,
                "default_rate_2yr_num_students": default_rate_2yr_num_students,
                "default_rate_3yr": default_rate_3yr,
                "default_rate_3yr_num_students": default_rate_3yr_num_students,
                "federal_loan_rate": federal_loan_rate,
                "median_debt": median_debt,
                "median_debt_num_students": median_debt_num_students,
                "median_debt_completers": median_debt_completers,
                "median_debt_completers_num_students": median_debt_completers_num_students,
                "median_debt_noncompleters": median_debt_noncompleters,
                "median_debt_noncompleters_num_students": median_debt_noncompleters_num_students,
                "monthly_loan_payments": monthly_loan_payments,
                "plus_loan_median_debt": plus_loan_median_debt,
                "plus_loan_median_debt_num_students": plus_loan_median_debt_num_students,
                "plus_loan_pct_lower": plus_loan_pct_lower,
                "plus_loan_pct_upper": plus_loan_pct_upper,
                "pell_grant_rate": pell_grant_rate,
                "students_with_any_loan": students_with_any_loan,
                "students_with_pell_grant": students_with_pell_grant,

                # earnings
                "not_working_not_enrolled_3yr_num_students": not_working_not_enrolled_3yr_num_students,
                "working_not_enrolled_3yr_num_students": working_not_enrolled_3yr_num_students,
                "over_poverty_line_3yr_num_students":over_poverty_line_3yr_num_students,

                # graduation rate fields
                "graduation_rate_100": graduation_rate_100,
                "graduation_rate_100_num_students": graduation_rate_100_num_students,
                "graduation_rate_150": graduation_rate_150,
                "graduation_rate_150_num_students": graduation_rate_150_num_students,
                "graduation_rate_150_2ormore": graduation_rate_150_2ormore,
                "graduation_rate_150_2ormore_num_students": graduation_rate_150_2ormore_num_students,
                "graduation_rate_150_aian": graduation_rate_150_aian,
                "graduation_rate_150_aian_num_students": graduation_rate_150_aian_num_students,
                "graduation_rate_150_asian": graduation_rate_150_asian,
                "graduation_rate_150_asian_num_students": graduation_rate_150_asian_num_students,
                "graduation_rate_150_black": graduation_rate_150_black,
                "graduation_rate_150_black_num_students": graduation_rate_150_black_num_students,
                "graduation_rate_150_hispanic": graduation_rate_150_hispanic,
                "graduation_rate_150_hispanic_num_students": graduation_rate_150_hispanic_num_students,
                "graduation_rate_150_nhpi": graduation_rate_150_nhpi,
                "graduation_rate_150_nhpi_num_students": graduation_rate_150_nhpi_num_students,
                "graduation_rate_150_nra": graduation_rate_150_nra,
                "graduation_rate_150_nra_num_students": graduation_rate_150_nra_num_students,
                "graduation_rate_150_unknown": graduation_rate_150_unknown,
                "graduation_rate_150_unknown_num_students": graduation_rate_150_unknown_num_students,
                "graduation_rate_150_white": graduation_rate_150_white,
                "graduation_rate_150_white_num_students": graduation_rate_150_white_num_students,
                "graduation_rate_200": graduation_rate_200,
                "graduation_rate_200_num_students": graduation_rate_200_num_students,

                # first time full time
                "first_time_full_time": first_time_full_time,
                "first_time_full_time_federal_loan_rate": first_time_full_time_federal_loan_rate,
                "first_time_full_time_pell_grant_rate": first_time_full_time_pell_grant_rate,
                "first_time_full_time_num_students": first_time_full_time_num_students,

                # retention rate
                "retention_rate_full_time": retention_rate_full_time,
                "retention_rate_part_time": retention_rate_part_time,

                # program percentages
                "program_percentage_agriculture": program_percentage_agriculture,
                "program_percentage_architecture": program_percentage_architecture,
                "program_percentage_biological": program_percentage_biological,
                "program_percentage_business_marketing": program_percentage_business_marketing,
                "program_percentage_communication": program_percentage_communication,
                "program_percentage_communications_technology": program_percentage_communications_technology,
                "program_percentage_computer": program_percentage_computer,
                "program_percentage_construction": program_percentage_construction,
                "program_percentage_education": program_percentage_education,
                "program_percentage_engineering": program_percentage_engineering,
                "program_percentage_engineering_technology": program_percentage_engineering_technology,
                "program_percentage_english": program_percentage_english,
                "program_percentage_ethnic_cultural_gender": program_percentage_ethnic_cultural_gender,
                "program_percentage_family_consumer_science": program_percentage_family_consumer_science,
                "program_percentage_health": program_percentage_health,
                "program_percentage_history": program_percentage_history,
                "program_percentage_humanities": program_percentage_humanities,
                "program_percentage_language": program_percentage_language,
                "program_percentage_legal": program_percentage_legal,
                "program_percentage_library": program_percentage_library,
                "program_percentage_mathematics": program_percentage_mathematics,
                "program_percentage_mechanic_repair_technology": program_percentage_mechanic_repair_technology,
                "program_percentage_military": program_percentage_military,
                "program_percentage_multidiscipline": program_percentage_multidiscipline,
                "program_percentage_parks_recreation_fitness": program_percentage_parks_recreation_fitness,
                "program_percentage_personal_culinary": program_percentage_personal_culinary,
                "program_percentage_philosophy_religious": program_percentage_philosophy_religious,
                "program_percentage_physical_science": program_percentage_physical_science,
                "program_percentage_precision_production": program_percentage_precision_production,
                "program_percentage_psychology": program_percentage_psychology,
                "program_percentage_public_administration_social_service": program_percentage_public_administration_social_service,
                "program_percentage_resources": program_percentage_resources,
                "program_percentage_science_technology": program_percentage_science_technology,
                "program_percentage_security_law_enforcement": program_percentage_security_law_enforcement,
                "program_percentage_social_science": program_percentage_social_science,
                "program_percentage_theology_religious_vocation": program_percentage_theology_religious_vocation,
                "program_percentage_transportation": program_percentage_transportation,
                "program_percentage_visual_performing": program_percentage_visual_performing,

                "created": date,
                "updated": date,
                }
        }

    scorecard_filename = os.path.join(FIXTURES_DIR, f'scorecard_{file_num}.json')

    if not os.path.isfile(scorecard_filename):
        scorecard_list = []
        scorecard_list.append(scorecard_seed)

        with open(scorecard_filename, mode='w') as outfile:
            json.dump(scorecard_list, outfile, ensure_ascii=False, indent=2)

    else:
        # open original file
        with open(scorecard_filename) as file:
            scorecard_data = json.load(file)

        # append additional data
        scorecard_data.append(scorecard_seed)

        # dump all the data back in the file
        with open(scorecard_filename, mode='w') as outfile:
            json.dump(scorecard_data, outfile, ensure_ascii=False, indent=2)

    ########################################################################
    # Save a list of primary keys used for field of study data
    ########################################################################
    field_of_study_max_pk_filename = os.path.join(SCRIPT_DIR, f'field_of_study_max_pk.txt')

    if not os.path.isfile(field_of_study_max_pk_filename):
        field_of_study_pk = 1

    else:
        # open file
        with open(field_of_study_max_pk_filename, 'r') as file:
            field_of_study_pk = int(file.read())


    ########################################################################
    # Get and save field of study data
    ########################################################################
    field_of_study_list = []
    try:
        programs = latest.get('programs')['cip_4_digit']
    except:
        programs = None

    if programs is not None:
        for program in programs:
            # basic information
            cip_code = program.get('code')
            cip_title = program.get('title')

            credential_level_data = program.get('credential')['level']
            if credential_level_data in CREDENTIAL_LEVEL_DICT:
                credential_level = CREDENTIAL_LEVEL_DICT[credential_level_data]
            else:
                sys.exit(f'ERROR => credential_level code of {credential_level_data} not in CREDENTIAL_LEVEL_DICT')

            credential_title = program.get('credential')['title']

            # debt
            debt_num_students = program.get('debt')['staff_grad_plus']['all']['all_inst']['count']
            debt_mean = program.get('debt')['staff_grad_plus']['all']['all_inst']['average']
            debt_median = program.get('debt')['staff_grad_plus']['all']['all_inst']['median']
            debt_monthly_payment = program.get('debt')['staff_grad_plus']['all']['all_inst']['median_payment']
            plus_debt_num_students = program.get('debt')['parent_plus']['all']['all_inst']['count']
            plus_debt_mean = program.get('debt')['parent_plus']['all']['all_inst']['average']
            plus_debt_median = program.get('debt')['parent_plus']['all']['all_inst']['median']
            plus_debt_monthly_payment = program.get('debt')['parent_plus']['all']['all_inst']['median_payment']

            # earnings
            earnings_1yr_median_earnings = program.get('earnings')['highest']['1_yr']['overall_median_earnings']
            earnings_1yr_not_working_not_enrolled_num_students = program.get('earnings')['highest']['1_yr']['not_working_not_enrolled']['overall_count']
            earnings_1yr_over_poverty_line_num_students = program.get('earnings')['highest']['1_yr']['overall_count_over_poverty_line']
            earnings_1yr_working_not_enrolled_num_students = program.get('earnings')['highest']['1_yr']['working_not_enrolled']['overall_count']
            earnings_2yr_median_earnings = program.get('earnings')['highest']['2_yr']['overall_median_earnings']
            earnings_2yr_not_working_not_enrolled_num_students = program.get('earnings')['highest']['2_yr']['not_working_not_enrolled']['overall_count']
            earnings_2yr_over_poverty_line_num_students = program.get('earnings')['highest']['2_yr']['overall_count_over_poverty_line']
            earnings_2yr_working_not_enrolled_num_students = program.get('earnings')['highest']['2_yr']['working_not_enrolled']['overall_count']

            # ipeds awards
            ipeds_awards1_num_students = program.get('counts')['ipeds_awards1']
            ipeds_awards2_num_students = program.get('counts')['ipeds_awards2']

            ########################################################################
            # Calculate whether we should show field of study or note
            # shows anything less than post-baccalaureate
            ########################################################################
            if credential_level_data < 4 and ipeds_awards2_num_students is not None:
                show_field_of_study = True

            else:
                show_field_of_study = False

            ########################################################################
            # Saves the data
            ########################################################################
            field_of_study_seed = {
                "model": "colleges.FieldOfStudy",
                "pk": field_of_study_pk,
                "fields": {
                    # standard fields
                    "college": pk,
                    "scorecard": pk,
                    "show": show_field_of_study,
                    "created": date,
                    "updated": date,

                    # fields from dataset
                    "cip_code": cip_code,
                    "cip_title": cip_title,
                    "credential_level": credential_level,
                    "credential_title": credential_title,

                    # debt
                    "debt_num_students": debt_num_students,
                    "debt_mean": debt_mean,
                    "debt_median": debt_median,
                    "debt_monthly_payment": debt_monthly_payment,
                    "plus_debt_num_students": plus_debt_num_students,
                    "plus_debt_mean": plus_debt_mean,
                    "plus_debt_median": plus_debt_median,
                    "plus_debt_monthly_payment": plus_debt_monthly_payment,

                    # earnings
                    "earnings_1yr_median_earnings": earnings_1yr_median_earnings,
                    "earnings_1yr_not_working_not_enrolled_num_students": earnings_1yr_not_working_not_enrolled_num_students,
                    "earnings_1yr_over_poverty_line_num_students": earnings_1yr_over_poverty_line_num_students,
                    "earnings_1yr_working_not_enrolled_num_students": earnings_1yr_working_not_enrolled_num_students,
                    "earnings_2yr_median_earnings": earnings_2yr_median_earnings,
                    "earnings_2yr_not_working_not_enrolled_num_students": earnings_2yr_not_working_not_enrolled_num_students,
                    "earnings_2yr_over_poverty_line_num_students": earnings_2yr_over_poverty_line_num_students,
                    "earnings_2yr_working_not_enrolled_num_students": earnings_2yr_working_not_enrolled_num_students,

                    # ipeds awards
                    "ipeds_awards1_num_students": ipeds_awards1_num_students,
                    "ipeds_awards2_num_students": ipeds_awards2_num_students,
                }
            }
            field_of_study_list.append(field_of_study_seed)
            field_of_study_pk += 1

    field_of_study_filename = os.path.join(FIXTURES_DIR, f'field_of_study_{file_num}.json')

    if not os.path.isfile(field_of_study_filename):
        with open(field_of_study_filename, mode='w') as outfile:
            json.dump(field_of_study_list, outfile, ensure_ascii=False, indent=2)

    else:
        # open original file
        with open(field_of_study_filename) as file:
            field_of_study_data = json.load(file)

        # append additional data
        for seed in field_of_study_list:
            field_of_study_data.append(seed)

        # dump all the data back in the file
        with open(field_of_study_filename, mode='w') as outfile:
            json.dump(field_of_study_data, outfile, ensure_ascii=False, indent=2)

    ############################################################################
    # Saves the field of study primary keys
    ############################################################################
    with open(field_of_study_max_pk_filename, mode='w') as outfile:
        outfile.write(str(field_of_study_pk))


################################################################################
# Finds the colleges to pull and stores in the given file number
################################################################################
def get_scorecard_data(file_num, starting_unit_id):
    with open(os.path.join(SCRIPT_DIR, "scorecard_unit_ids.json")) as file:
        data = json.load(file)

    counter = 1
    start = data.index(starting_unit_id)
    end = start + 500
    total_colleges = len(data) - 1
    remaining_colleges = total_colleges - start + 1
    print(f'STATUS => There are {remaining_colleges} remaining colleges')

    pk = start + 1
    for i in data[start:end]:
        get_formatted_college_data_by_scorecard_unit_id(file_num=file_num, pk=pk, unit_id=i)
        print(f'STATUS => Finished pulling data for number {counter}')
        pk += 1
        counter += 1

    print(f'STATUS => Finished with file {file_num}!')


################################################################################
# Functions to run
################################################################################
get_scorecard_data(file_num=7, starting_unit_id=214795)
