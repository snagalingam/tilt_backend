
import os
import json
from json import JSONEncoder
import requests
from time import sleep
import datetime
import pytz

def scorecard_api(college_id, college_pk):
    endpoint = f"https://api.data.gov/ed/collegescorecard/v1/schools"
    key = os.environ.get('SCORECARD_KEY')

    url = f"{endpoint}?id={college_id}&api_key={key}"
    res = requests.get(url)
    scorecard = res.json()
    results = scorecard.get('results', None)
    bool_list = [False, True, None]

    try: 
        error = scorecard['error']
        print(f'   ERROR ===> : {error["code"]}')
        print(f'   MESSAGE ===> : {error["message"]}')
    
    except:
        pass

    if results is not None:
        data = results[0]
        school = data.get('school')
        latest = data.get('latest')
        student = latest.get('student')

        operating = bool_list[school.get('operating') or 2]
        undergraduate_students = student.get('size') or None
        degree_awarded_data = school.get('degrees_awarded')
        degree_awarded_num = degree_awarded_data.get('predominant')

        if operating and undergraduate_students and degree_awarded_data:
        
        # if operating == True
        # if undergraduate_students (population) is greater than zero
        # if degree_awarded is predominantly associate's or bachelor's
        # return seed data else return None 
            if undergraduate_students > 0 and degree_awarded_num < 4:
                degree_list = ["Not Classified",
                            "Predominantly certificate-degree granting",
                            "Predominantly associate's-degree granting",
                            "Predominantly bachelor's-degree granting",
                            "Entirely graduate-degree granting", 
                            None]
                predominant_degree_awarded_recoded = degree_list[degree_awarded_data[
                    'predominant_recoded'] or 5]
                predominant_degree_awarded = degree_list[degree_awarded_data[
                    'predominant'] or 5]
                highest_list = ["Non-degree-granting",
                                "Certificate degree",
                                "Associate degree",
                                "Bachelor's degree",
                                "Graduate degree",
                                None]
                highest_degree_awarded = highest_list[degree_awarded_data[
                            'highest'] or 5]
                # 1st level in results
                unit_id = data.get('id')
                ope_id = data.get('ope8_id')
                ope6_id = data.get('ope6_id')
                latitude = data.get('location')['lat']
                longitude = data.get('location')['lon']
                # 2nd level in results > school
                name = school.get('name')
                alias = school.get('alias')
                city = school.get('city')
                state = school.get('state')
                zipcode = school.get('zip')
                accreditor = school.get('accreditor')
                school_url = school.get('school_url')
                price_calculator_url = school.get('price_calculator_url')
                # boolean list on line 20
                under_investigation = bool_list[school.get('under_investigation') or 2]
                main_campus = bool_list[school.get('main_campus') or 2]
                branches = school.get('branches')
                ownership_list = [None,
                                  "Public",
                                  "Private Nonprofit",
                                  "Private For-Profit"]
                ownership = ownership_list[school.get('ownership') or 0]
                state_dict = {
                    "None": None,
                    "1": "Alabama",
                    "2": "Alaska",
                    "4": "Arizona",
                    "5": "Arkansas",
                    "6": "California",
                    "8": "Colorado",
                    "9": "Connecticut",
                    "10": "Delaware",
                    "11": "District of Columbia",
                    "12": "Florida",
                    "13": "Georgia",
                    "15": "Hawaii",
                    "16": "Idaho",
                    "17": "Illinois",
                    "18": "Indiana",
                    "19": "Iowa",
                    "20": "Kansas",
                    "21": "Kentucky",
                    "22": "Louisiana",
                    "23": "Maine",
                    "24": "Maryland",
                    "25": "Massachusetts",
                    "26": "Michigan",
                    "27": "Minnesota",
                    "28": "Mississippi",
                    "29": "Missouri",
                    "30": "Montana",
                    "31": "Nebraska",
                    "32": "Nevada",
                    "33": "New Hampshire",
                    "34": "New Jersey",
                    "35": "New Mexico",
                    "36": "New York",
                    "37": "North Carolina",
                    "38": "North Dakota",
                    "39": "Ohio",
                    "40": "Oklahoma",
                    "41": "Oregon",
                    "42": "Pennsylvania",
                    "44": "Rhode Island",
                    "45": "South Carolina",
                    "46": "South Dakota",
                    "47": "Tennessee",
                    "48": "Texas",
                    "49": "Utah",
                    "50": "Vermont",
                    "51": "Virginia",
                    "53": "Washington",
                    "54": "West Virginia",
                    "55": "Wisconsin",
                    "56": "Wyoming",
                    "60": "American Samoa",
                    "64": "Federated States of Micronesia",
                    "66": "Guam",
                    "69": "Northern Mariana Islands",
                    "70": "Palau",
                    "72": "Puerto Rico",
                    "78": "Virgin Islands"
                }

                state_fips = str(school.get('state_fips'))
                if state_fips in state_dict:
                    state_fips = state_dict[str(school.get('state_fips'))]
                else:
                    state_fips = None

                region_list = ["U.S. Service Schools",
                            "New England",
                            "Mid East",
                            "Great Lakes",
                            "Plains",
                            "Southeast",
                            "Southwest",
                            "Rocky Mountains",
                            "Far West",
                            "Outlying Areas",
                            None]
                region = region_list[school.get('region_id') or 10]
                locale_dict = {
                    "11": "City: Large(population of 250, 000 or more)",
                    "12": "City: Midsize(population of at least 100, 000 but less than 250, 000)",
                    "13": "City: Small(population less than 100, 000)",
                    "21": "Suburb: Large(outside principal city, in urbanized area with population of 250, 000 or more)",
                    "22": "Suburb: Midsize(outside principal city, in urbanized area with population of at least 100, 000 but less than 250, 000)",
                    "23": "Suburb: Small(outside principal city, in urbanized area with population less than 100, 000)",
                    "31": "Town: Fringe ( in urban cluster up to 10 miles from an urbanized area)",
                    "32": "Town: Distant ( in urban cluster more than 10 miles and up to 35 miles from an urbanized area)",
                    "33": "Town: Remote ( in urban cluster more than 35 miles from an urbanized area)",
                    "41": "Rural: Fringe(rural territory up to 5 miles from an urbanized area or up to 2.5 miles from an urban cluster)",
                    "42": "Rural: Distant(rural territory more than 5 miles but up to 25 miles from an urbanized area or more than 2.5 and up to 10 miles from an urban cluster)",
                    "43": "Rural: Remote(rural territory more than 25 miles from an urbanized area and more than 10 miles from an urban cluster)"
                }
                locale = school.get('locale')
                if locale is not None:
                    if locale < 11:
                        locale = None 
                    else: 
                        locale = locale_dict[str(locale)]
                carnegie_basic_dict = {
                    "None": None,
                    "-2": "Not Applicable",
                    "0": "Not Classified",
                    "1": "Associate's Colleges: High Transfer-High Traditional",
                    "2": "Associate's Colleges: High Transfer-Mixed Traditional/Nontraditional",
                    "3": "Associate's Colleges: High Transfer-High Nontraditional",
                    "4": "Associate's Colleges: Mixed Transfer/Career & Technical-High Traditional",
                    "5": "Associate's Colleges: Mixed Transfer/Career & Technical-Mixed Traditional/Nontraditional",
                    "6": "Associate's Colleges: Mixed Transfer/Career & Technical-High Nontraditional",
                    "7": "Associate's Colleges: High Career & Technical-High Traditional",
                    "8": "Associate's Colleges: High Career & Technical-Mixed Traditional/Nontraditional",
                    "9": "Associate's Colleges: High Career & Technical-High Nontraditional",
                    "10": "Special Focus Two-Year: Health Professions",
                    "11": "Special Focus Two-Year: Technical Professions",
                    "12": "Special Focus Two-Year: Arts & Design",
                    "13": "Special Focus Two-Year: Other Fields",
                    "14": "Baccalaureate/Associate's Colleges: Associate's Dominant",
                    "15": "Doctoral Universities: Very High Research Activity",
                    "16": "Doctoral Universities: High Research Activity",
                    "17": "Doctoral/Professional Universities",
                    "18": "Master's Colleges & Universities: Larger Programs",
                    "19": "Master's Colleges & Universities: Medium Programs",
                    "20": "Master's Colleges & Universities: Small Programs",
                    "21": "Baccalaureate Colleges: Arts & Sciences Focus",
                    "22": "Baccalaureate Colleges: Diverse Fields",
                    "23": "Baccalaureate/Associate's Colleges: Mixed Baccalaureate/Associate's",
                    "24": "Special Focus Four-Year: Faith-Related Institutions",
                    "25": "Special Focus Four-Year: Medical Schools & Centers",
                    "26": "Special Focus Four-Year: Other Health Professions Schools",
                    "27": "Special Focus Four-Year: Engineering Schools",
                    "28": "Special Focus Four-Year: Other Technology-Related Schools",
                    "29": "Special Focus Four-Year: Business & Management Schools",
                    "30": "Special Focus Four-Year: Arts, Music & Design Schools",
                    "31": "Special Focus Four-Year: Law Schools",
                    "32": "Special Focus Four-Year: Other Special Focus Institutions",
                    "33": "Tribal Colleges"
                }
                carnegie_basic = carnegie_basic_dict[str(school.get('carnegie_basic')) or "None"]
                carnegie_undergrad_dict = {
                    "None": None,
                    "-2": "Not Applicable",
                    "0": "Not Classified",
                    "1": "Two-year, higher part-time",
                    "2": "Two-year, mixed part/full-time",
                    "3": "Two-year, medium full-time",
                    "4": "Two-year, higher full-time",
                    "5": "Four-year, higher part-time",
                    "6": "Four-year, medium full-time, inclusive, lower transfer-in",
                    "7": "Four-year, medium full-time, inclusive, higher transfer-in",
                    "8": "Four-year, medium full-time, selective, lower transfer-in",
                    "9": "Four-year, medium full-time, selective, higher transfer-in",
                    "10": "Four-year, full-time, inclusive, lower transfer-in",
                    "11": "Four-year, full-time, inclusive, higher transfer-in",
                    "12": "Four-year, full-time, selective, lower transfer-in",
                    "13": "Four-year, full-time, selective, higher transfer-in",
                    "14": "Four-year, full-time, more selective, lower transfer-in",
                    "15": "Four-year, full-time, more selective, higher transfer-in",
                }
                carnegie_undergrad = carnegie_undergrad_dict[str(
                    school.get('carnegie_undergrad')) or "None"]
                carnegie_size_setting_dict = {
                    "None": None,
                    "-2": "Not Applicable",
                    "0": "Not Classified",
                    "1": "Two-year, very small",
                    "2": "Two-year, small",
                    "3": "Two-year, medium",
                    "4": "Two-year, large",
                    "5": "Two-year, very large",
                    "6": "Four-year, very small, primarily nonresidential",
                    "7": "Four-year, very small, primarily residential",
                    "8": "Four-year, very small, highly residential",
                    "9": "Four-year, small, primarily nonresidential",
                    "10": "Four-year, small, primarily residential",
                    "11": "Four-year, small, highly residential",
                    "12": "Four-year, medium, primarily nonresidential",
                    "13": "Four-year, medium, primarily residential",
                    "14": "Four-year, medium, highly residential",
                    "15": "Four-year, large, primarily nonresidential",
                    "16": "Four-year, large, primarily residential",
                    "17": "Four-year, large, highly residential",
                    "18": "Exclusively graduate/professional",
                }
                carnegie_size_setting = carnegie_size_setting_dict[str(
                    school.get('carnegie_size_setting')) or "None"]
                # 3rd level in results > school > minority_serving
                minority = school.get('minority_serving')
                minority_serving_historically_black = bool_list[minority.get(
                    'historically_black') or 2]
                minority_serving_predominantly_black = bool_list[minority.get(
                    'predominantly_black') or 2]
                minority_serving_annh = bool_list[minority.get('annh') or 2]
                minority_serving_tribal = bool_list[minority.get('tribal') or 2]
                minority_serving_aanipi = bool_list[minority.get('aanipi') or 2]
                minority_serving_hispanic = bool_list[minority.get('hispanic') or 2]
                minority_serving_nant = bool_list[minority.get('nant') or 2]
                
                # boolean list on line 20
                men_only = bool_list[school.get('men_only') or 2]
                women_only = bool_list[school.get('women_only') or 2]
                online_only = bool_list[school.get('online_only') or 2]

                institutional_list = [None,
                                    "4-year",
                                    "2-year",
                                    "Less-than-2-year"]
                institutional_level = institutional_list[school.get(
                    'institutional_characteristics')['level'] or 0]
                open_list = [None, True, False, False]
                open_admissions = open_list[school.get('open_admissions_policy') or 0]
                religious_dict = {
                    "-1": None,
                    "-2": None,
                    "22": "American Evangelical Lutheran Church",
                    "24": "African Methodist Episcopal Zion Church",
                    "27": "Assemblies of God Church",
                    "28": "Brethren Church",
                    "30": "Roman Catholic",
                    "33": "Wisconsin Evangelical Lutheran Synod",
                    "34": "Christ and Missionary Alliance Church",
                    "35": "Christian Reformed Church",
                    "36": "Evangelical Congregational Church",
                    "37": "Evangelical Covenant Church of America",
                    "38": "Evangelical Free Church of America",
                    "39": "Evangelical Lutheran Church",
                    "40": "International United Pentecostal Church",
                    "41": "Free Will Baptist Church",
                    "42": "Interdenominational",
                    "43": "Mennonite Brethren Church",
                    "44": "Moravian Church",
                    "45": "North American Baptist",
                    "47": "Pentecostal Holiness Church",
                    "48": "Christian Churches and Churches of Christ",
                    "49": "Reformed Church in America",
                    "50": "Episcopal Church, Reformed",
                    "51": "African Methodist Episcopal",
                    "52": "American Baptist",
                    "53": "American Lutheran",
                    "54": "Baptist",
                    "55": "Christian Methodist Episcopal",
                    "57": "Church of God",
                    "58": "Church of Brethren",
                    "59": "Church of the Nazarene",
                    "60": "Cumberland Presbyterian",
                    "61": "Christian Church(Disciples of Christ)",
                    "64": "Free Methodist",
                    "65": "Friends",
                    "66": "Presbyterian Church(USA)",
                    "67": "Lutheran Church in America",
                    "68": "Lutheran Church - Missouri Synod",
                    "69": "Mennonite Church",
                    "71": "United Methodist",
                    "73": "Protestant Episcopal",
                    "74": "Churches of Christ",
                    "75": "Southern Baptist",
                    "76": "United Church of Christ",
                    "77": "Protestant, not specified",
                    "78": "Multiple Protestant Denomination",
                    "79": "Other Protestant",
                    "80": "Jewish",
                    "81": "Reformed Presbyterian Church",
                    "84": "United Brethren Church",
                    "87": "Missionary Church Inc",
                    "88": "Undenominational",
                    "89": "Wesleyan",
                    "91": "Greek Orthodox",
                    "92": "Russian Orthodox",
                    "93": "Unitarian Universalist",
                    "94": "Latter Day Saints(Mormon Church)",
                    "95": "Seventh Day Adventists",
                    "97": "The Presbyterian Church in America",
                    "99": "Other(none of the above)",
                    "100": "Original Free Will Baptist",
                    "101": "Ecumenical Christian",
                    "102": "Evangelical Christian",
                    "103": "Presbyterian",
                    "105": "General Baptist",
                    "106": "Muslim",
                    "107": "Plymouth Brethren",
                }
                religious_affiliation = school.get('religious_affiliation')
                if religious_affiliation is not None:
                    if religious_affiliation > 107:
                        religious_affiliation = None
                    else: 
                        religious_affiliation = religious_dict.get(str(religious_affiliation))
                # 3rd level in results > latest > admissions
                admissions = latest.get('admissions')
                admissions_rate = admissions.get('admission_rate')['overall']
                # 4th level in results > latest > admissions > sat_scores
                sat_scores = latest.get('admissions')['sat_scores'] or None
                sat_average = sat_scores.get('average')['overall'] or None
                sat_reading_25th_percentile = sat_scores.get('25th_percentile')[
                    'critical_reading'] or None
                sat_math_25th_percentile = sat_scores.get('25th_percentile')['math'] or None
                sat_writing_25th_percentile = sat_scores.get('25th_percentile')[
                    'writing'] or None
                sat_reading_75th_percentile = sat_scores.get('75th_percentile')[
                    'critical_reading'] or None
                sat_math_75th_percentile = sat_scores.get('75th_percentile')['math'] or None
                sat_writing_75th_percentile = sat_scores.get('75th_percentile')[
                    'writing'] or None
                sat_reading_midpoint = sat_scores.get('midpoint')['critical_reading'] or None
                sat_math_midpoint = sat_scores.get('midpoint')['math'] or None
                sat_writing_midpoint = sat_scores.get('midpoint')['writing'] or None
                # 4th level in results > latest > admissions > act_scores
                act_scores = latest.get('admissions')['act_scores']
                act_cumulative_25th_percentile = act_scores.get('25th_percentile')[
                    'cumulative'] or None
                act_english_25th_percentile = act_scores.get('25th_percentile')[
                    'english'] or None
                act_math_25th_percentile = act_scores.get('25th_percentile')[
                    'math'] or None
                act_writing_25th_percentile = act_scores.get('25th_percentile')[
                    'writing'] or None
                act_cumulative_75th_percentile = act_scores.get('75th_percentile')[
                    'cumulative'] or None
                act_english_75th_percentile = act_scores.get('75th_percentile')[
                    'english'] or None
                act_math_75th_percentile = act_scores.get('75th_percentile')[
                    'math'] or None
                act_writing_75th_percentile = act_scores.get('75th_percentile')[
                    'writing'] or None
                act_cumulative_midpoint = act_scores.get('midpoint')[
                    'cumulative'] or None
                act_english_midpoint = act_scores.get('midpoint')[
                    'english'] or None
                act_math_midpoint = act_scores.get('midpoint')[
                    'math'] or None
                act_writing_midpoint = act_scores.get('midpoint')[
                    'writing'] or None
                # 3rd level in results > latest > student
                undergraduate_students_parttime = student.get(
                    'part_time_share') or None
                share_25_older = student.get('share_25_older')
                students_with_pell_grant = student.get(
                    'students_with_pell_grant') or None
                first_time_full_time = student.get(
                    'share_first')['time_full']['time'] or None
                first_time_full_time_num_students = student.get(
                    'ftft_undergrads_with_pell_grant_or_federal_student_loan') or None
                
                # 4th level in results > latest > students > retention_rate
                retention_rate = student.get('retention_rate')
                retention_rate_full_time = retention_rate.get(
                    'four_year')['full_time'] or retention_rate.get('lt_four_year')['full_time']
                retention_rate_part_time = retention_rate.get(
                    'four_year')['part_time'] or retention_rate.get('lt_four_year')['part_time']
                # 4th level in results > latest > students > demographics
                demographics = student.get('demographics')
                undergraduate_students_white = demographics.get('race_ethnicity')[
                    'white'] or None
                undergraduate_students_black = demographics.get('race_ethnicity')[
                    'black'] or None
                undergraduate_students_hispanic = demographics.get('race_ethnicity')[
                    'hispanic'] or None
                undergraduate_students_asian = demographics.get('race_ethnicity')[
                    'asian'] or None
                undergraduate_students_aian = demographics.get('race_ethnicity')[
                    'aian'] or None
                undergraduate_students_nhpi = demographics.get('race_ethnicity')[
                    'nhpi'] or None
                undergraduate_students_2ormore = demographics.get('race_ethnicity')[
                    'two_or_more'] or None
                undergraduate_students_nra = demographics.get('race_ethnicity')[
                    'non_resident_alien'] or None
                undergraduate_students_unknown = demographics.get('race_ethnicity')[
                    'unknown'] or None
                age_entry = demographics.get('age_entry') or None
                veteran = demographics.get('veteran') or None
                first_generation = demographics.get('first_generation') or None
                undergraduate_students_men = demographics.get('men') or None
                undergraduate_students_women = demographics.get('women') or None
                # 3rd level in results > latest > cost
                cost = latest.get('cost')
                avg_net_price = cost.get('avg_net_price')[
                    'public'] or cost.get('avg_net_price')['private']
                # 4th level in results > latest > cost > net_price
                net_price = cost.get('net_price')
                net_price_public = net_price.get('public')['by_income_level']
                net_price_private = net_price.get('private')['by_income_level']
                avg_net_price_lo = net_price_public.get(
                    '0-30000') or net_price_private.get('0-30000')
                avg_net_price_m1 = net_price_public.get(
                    '30001-48000') or net_price_private.get('30001-48000')
                avg_net_price_m2 = net_price_public.get(
                    '48001-75000') or net_price_private.get('48001-75000')
                avg_net_price_h1 = net_price_public.get(
                    '75001-110000') or net_price_private.get('75001-110000')
                avg_net_price_h2 = net_price_public.get(
                    '110001-plus') or net_price_private.get('110001-plus')
                # 4th level in results > latest > cost > attendance
                attendance = cost.get('attendance')
                cost_of_attendance = attendance.get(
                    'academic_year') or attendance.get('program_year')
                # 4th level in results > latest > cost > tuition
                tuition = cost.get('tuition')
                tuition_in_state = tuition.get('in_state') or None
                tuition_out_of_state = tuition.get('out_of_state') or None
                tuition_program_year = tuition.get('program_year') or None
                # 3rd level in results > latest > aid
                aid = latest.get('aid')
                pell_grant_rate = aid.get('pell_grant_rate') or None
                federal_loan_rate = aid.get('federal_loan_rate') or None
                median_debt = aid.get('loan_principal') or None
                first_time_full_time_pell_grant_rate = aid.get('ftft_pell_grant_rate') or None
                first_time_full_time_federal_loan_rate = aid.get(
                    'ftft_federal_loan_rate') or None
                # 4th level in results > latest > aid > median_debt
                mid_debt = aid.get('median_debt')
                median_debt_completers = mid_debt.get('completers')['overall'] or None
                monthly_loan_payments = mid_debt.get(
                    'completers')['monthly_payments'] or None
                median_debt_noncompleters = mid_debt.get('noncompleters') or None
                median_debt_num_students = mid_debt.get('number')[
                    'overall'] or None
                median_debt_completers_num_students = mid_debt.get('number')[
                    'completers'] or None
                median_debt_noncompleters_num_students = mid_debt.get('number')[
                    'noncompleters'] or None
                students_with_any_loan = mid_debt.get('students_with_any_loan') or None
                # 3rd level in results > latest > repayment
                repayment = latest.get('repayment')
                default_rate_2yr = repayment.get('2_yr_default_rate') or None
                default_rate_3yr = repayment.get('3_yr_default_rate') or None
                default_rate_2yr_num_students = repayment.get(
                    '2_yr_default_rate_denom') or None
                default_rate_3yr_num_students = repayment.get(
                    '3_yr_default_rate_denom') or None
                # 3rd level in results > latest > completion
                completion = latest.get('completion')
                graduation_rate_100 = completion.get(
                    'completion_rate_4yr_100nt') or completion.get(
                    'completion_rate_less_than_4yr_100nt')
                graduation_rate_100_num_students = completion.get(
                    'completion_cohort_4yr_100nt') or completion.get(
                    'completion_cohort_less_than_4yr_100nt')
                graduation_rate_150 = completion.get(
                    'completion_rate_4yr_150nt') or completion.get(
                    'completion_rate_less_than_4yr_150nt')
                graduation_rate_150_white = completion.get(
                    'completion_rate_4yr_150_white') or completion.get(
                    'completion_rate_l4yr_150_white')
                graduation_rate_150_black = completion.get(
                    'completion_rate_4yr_150_black') or completion.get(
                    'completion_rate_l4yr_150_black')
                graduation_rate_150_hispanic = completion.get(
                    'completion_rate_4yr_150_hispanic') or completion.get(
                    'completion_rate_l4yr_150_hispanic')
                graduation_rate_150_asian = completion.get(
                    'completion_rate_4yr_150_asian') or completion.get(
                    'completion_rate_l4yr_150_asian')
                graduation_rate_150_aian = completion.get(
                    'completion_rate_4yr_150_aian') or completion.get(
                    'completion_rate_l4yr_150_aian')
                graduation_rate_150_nhpi = completion.get(
                    'completion_rate_4yr_150_nhpi') or completion.get(
                    'completion_rate_l4yr_150_nhpi')
                graduate_rate_150_2ormore = completion.get(
                    'completion_rate_4yr_150_2ormore') or completion.get(
                    'completion_rate_l4yr_150_2ormore')
                graduate_rate_150_nra = completion.get(
                    'completion_rate_4yr_150_nonresident')['alien'] or completion.get(
                    'completion_rate_l4yr_150_nonresident')['alien']
                graduate_rate_150_unknown = completion.get(
                    'completion_rate_4yr_150_race')['unknown'] or completion.get(
                    'completion_rate_l4yr_150_race')['unknown']
                graduation_rate_150_white_num_students = completion.get(
                    'completion_cohort_4yr_150_white') or completion.get(
                    'completion_cohort_less_than_4yr_150_white')
                graduation_rate_150_black_num_students = completion.get(
                    'completion_cohort_4yr_150_black') or completion.get(
                    'completion_cohort_less_than_4yr_150_black')
                graduation_rate_150_hispanic_num_students = completion.get(
                    'completion_cohort_4yr_150_hispanic') or completion.get(
                    'completion_cohort_less_than_4yr_150_hispanic')
                graduation_rate_150_asian_num_students = completion.get(
                    'completion_cohort_4yr_150_asian') or completion.get(
                    'completion_cohort_less_than_4yr_150_asian')
                graduation_rate_150_aian_num_students = completion.get(
                    'completion_cohort_4yr_150_aian') or completion.get(
                    'completion_cohort_less_than_4yr_150_aian')
                graduation_rate_150_nhpi_num_students = completion.get(
                    'completion_cohort_4yr_150_nhpi') or completion.get(
                    'completion_cohort_less_than_4yr_150_nhpi')
                graduate_rate_150_2ormore_num_students = completion.get(
                    'completion_cohort_4yr_150_2ormore') or completion.get(
                    'completion_cohort_less_than_4yr_150_2ormore')
                graduate_rate_150_nra_num_students = completion.get(
                    'completion_cohort_4yr_150_nonresident')['alien'] or completion.get(
                    'completion_cohort_less_than_4yr_150_nonresident')['alien']
                graduate_rate_150_unknown_num_students = completion.get(
                    'completion_cohort_4yr_150_race')['unknown'] or completion.get(
                    'completion_cohort_less_than_4yr_150_race')['unknown']
                graduation_rate_200 = completion.get(
                    'completion_rate_4yr_200nt') or completion.get(
                    'completion_rate_less_than_4yr_200nt')

                # 4th level in results > latest > academics > program_percentage
                academics = latest.get('academics')
                program_percentage = academics.get('program_percentage')

                program_percentage_education = program_percentage.get(
                    'education')
                program_percentage_mathematics = program_percentage.get(
                    'mathematics')
                program_percentage_business_marketing = program_percentage.get(
                    'business_marketing')
                program_percentage_communications_technology = program_percentage.get(
                    'communications_technology')
                program_percentage_language = program_percentage.get(
                    'language')
                program_percentage_visual_performing = program_percentage.get(
                    'visual_performing')
                program_percentage_engineering_technology = program_percentage.get(
                    'engineering_technology')
                program_percentage_parks_recreation_fitness = program_percentage.get(
                    'parks_recreation_fitness')
                program_percentage_agriculture = program_percentage.get(
                    'agriculture')
                program_percentage_security_law_enforcement = program_percentage.get(
                    'security_law_enforcement')
                program_percentage_computer = program_percentage.get(
                    'computer')
                program_percentage_precision_production = program_percentage.get(
                    'precision_production')
                program_percentage_humanities = program_percentage.get(
                    'humanities')
                program_percentage_library = program_percentage.get(
                    'library')
                program_percentage_psychology = program_percentage.get(
                    'psychology')
                program_percentage_social_science = program_percentage.get(
                    'social_science')
                program_percentage_legal = program_percentage.get(
                    'legal')
                program_percentage_english = program_percentage.get(
                    'english')
                program_percentage_construction = program_percentage.get(
                    'construction')
                program_percentage_military = program_percentage.get(
                    'military')
                program_percentage_communication = program_percentage.get(
                    'communication')
                program_percentage_public_administration_social_service = program_percentage.get(
                    'public_administration_social_service')
                program_percentage_architecture = program_percentage.get(
                    'architecture')
                program_percentage_ethnic_cultural_gender = program_percentage.get(
                    'ethnic_cultural_gender')
                program_percentage_resources = program_percentage.get(
                    'resources')
                program_percentage_health = program_percentage.get(
                    'health')
                program_percentage_engineering = program_percentage.get(
                    'engineering')
                program_percentage_history = program_percentage.get(
                    'history')
                program_percentage_theology_religious_vocation = program_percentage.get(
                    'theology_religious_vocation')
                program_percentage_transportation = program_percentage.get(
                    'transportation')
                program_percentage_physical_science = program_percentage.get(
                    'physical_science')
                program_percentage_science_technology = program_percentage.get(
                    'science_technology')
                program_percentage_biological = program_percentage.get(
                    'biological')
                program_percentage_family_consumer_science = program_percentage.get(
                    'family_consumer_science')
                program_percentage_philosophy_religious = program_percentage.get(
                    'philosophy_religious')
                program_percentage_personal_culinary = program_percentage.get(
                    'personal_culinary')
                program_percentage_multidiscipline = program_percentage.get(
                    'multidiscipline')
                program_percentage_mechanic_repair_technology = program_percentage.get(
                    'mechanic_repair_technology')

                seed = {
                    "model": "colleges.Scorecard",
                    "pk": college_pk,
                    "fields": {
                        "unit_id": unit_id,
                        "ope_id": ope_id,
                        "ope6_id": ope6_id,
                        "name": name,
                        "city": city,
                        "state": state,
                        "zipcode": zipcode,
                        "accreditor": accreditor,
                        "school_url": school_url,
                        "price_calculator_url": price_calculator_url,
                        "predominant_degree_awarded_recoded": predominant_degree_awarded_recoded,
                        "under_investigation": under_investigation,
                        "main_campus": main_campus,
                        "branches": branches,
                        "predominant_degree_awarded": predominant_degree_awarded,
                        "highest_degree_awarded": highest_degree_awarded,
                        "ownership": ownership,
                        "state_fips": state_fips,
                        "region": region,
                        "locale": locale,
                        "latitude": latitude,
                        "longitude": longitude,
                        "carnegie_basic": carnegie_basic,
                        "carnegie_undergrad": carnegie_undergrad,
                        "carnegie_size_setting": carnegie_size_setting,
                        "minority_serving_historically_black": minority_serving_historically_black,
                        "minority_serving_predominantly_black": minority_serving_predominantly_black,
                        "minority_serving_annh": minority_serving_annh,
                        "minority_serving_tribal": minority_serving_tribal,
                        "minority_serving_aanipi": minority_serving_aanipi,
                        "minority_serving_hispanic": minority_serving_hispanic,
                        "minority_serving_nant": minority_serving_nant,
                        "men_only": men_only,
                        "women_only": women_only,
                        "religious_affiliation": religious_affiliation,
                        "admissions_rate": admissions_rate,
                        "sat_reading_25th_percentile": sat_reading_25th_percentile,
                        "sat_reading_75th_percentile": sat_reading_75th_percentile,
                        "sat_math_25th_percentile": sat_math_25th_percentile,
                        "sat_math_75th_percentile": sat_math_75th_percentile,
                        "sat_writing_25th_percentile": sat_writing_25th_percentile,
                        "sat_writing_75th_percentile": sat_writing_75th_percentile,
                        "sat_reading_midpoint": sat_reading_midpoint,
                        "sat_math_midpoint": sat_math_midpoint,
                        "sat_writing_midpoint": sat_writing_midpoint,
                        "act_cumulative_25th_percentile": act_cumulative_25th_percentile,
                        "act_cumulative_75th_percentile": act_cumulative_75th_percentile,
                        "act_english_25th_percentile": act_english_25th_percentile,
                        "act_english_75th_percentile": act_english_75th_percentile,
                        "act_math_25th_percentile": act_math_25th_percentile,
                        "act_math_75th_percentile": act_math_75th_percentile,
                        "act_writing_25th_percentile": act_writing_25th_percentile,
                        "act_writing_75th_percentile": act_writing_75th_percentile,
                        "act_cumulative_midpoint": act_cumulative_midpoint,
                        "act_english_midpoint": act_english_midpoint,
                        "act_math_midpoint": act_math_midpoint,
                        "act_writing_midpoint": act_writing_midpoint,
                        "sat_average": sat_average,
                        "online_only": online_only,
                        "undergraduate_students": undergraduate_students,
                        "undergraduate_students_white": undergraduate_students_white,
                        "undergraduate_students_black": undergraduate_students_black,
                        "undergraduate_students_hispanic": undergraduate_students_hispanic,
                        "undergraduate_students_asian": undergraduate_students_asian,
                        "undergraduate_students_aian": undergraduate_students_aian,
                        "undergraduate_students_nhpi": undergraduate_students_nhpi,
                        "undergraduate_students_2ormore": undergraduate_students_2ormore,
                        "undergraduate_students_nra": undergraduate_students_nra,
                        "undergraduate_students_unknown": undergraduate_students_unknown,
                        "undergraduate_students_parttime": undergraduate_students_parttime,
                        "operating": operating,
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
                        "pell_grant_rate": pell_grant_rate,
                        "federal_loan_rate": federal_loan_rate,
                        "share_25_older": share_25_older,
                        "default_rate_2yr": default_rate_2yr,
                        "default_rate_3yr": default_rate_3yr,
                        "median_debt": median_debt,
                        "median_debt_completers": median_debt_completers,
                        "median_debt_noncompleters": median_debt_noncompleters,
                        "median_debt_num_students": median_debt_num_students,
                        "median_debt_completers_num_students": median_debt_completers_num_students,
                        "median_debt_noncompleters_num_students": median_debt_noncompleters_num_students,
                        "monthly_loan_payments": monthly_loan_payments,
                        "students_with_any_loan": students_with_any_loan,
                        "students_with_pell_grant": students_with_pell_grant,
                        "age_entry": age_entry,
                        "veteran": veteran,
                        "first_generation": first_generation,
                        "alias": alias,
                        "graduation_rate_100": graduation_rate_100,
                        "graduation_rate_100_num_students": graduation_rate_100_num_students,
                        "institutional_level": institutional_level,
                        "undergraduate_students_men": undergraduate_students_men,
                        "undergraduate_students_women": undergraduate_students_women,
                        "default_rate_2yr_num_students": default_rate_2yr_num_students,
                        "default_rate_3yr_num_students": default_rate_3yr_num_students,
                        "open_admissions": open_admissions,
                        "graduation_rate_150": graduation_rate_150,
                        "first_time_full_time": first_time_full_time,
                        "graduation_rate_150_white": graduation_rate_150_white,
                        "graduation_rate_150_black": graduation_rate_150_black,
                        "graduation_rate_150_hispanic": graduation_rate_150_hispanic,
                        "graduation_rate_150_asian": graduation_rate_150_asian,
                        "graduation_rate_150_aian": graduation_rate_150_aian,
                        "graduation_rate_150_nhpi": graduation_rate_150_nhpi,
                        "graduate_rate_150_2ormore": graduate_rate_150_2ormore,
                        "graduate_rate_150_nra": graduate_rate_150_nra,
                        "graduate_rate_150_unknown": graduate_rate_150_unknown,
                        "graduation_rate_150_white_num_students": graduation_rate_150_white_num_students,
                        "graduation_rate_150_black_num_students": graduation_rate_150_black_num_students,
                        "graduation_rate_150_hispanic_num_students": graduation_rate_150_hispanic_num_students,
                        "graduation_rate_150_asian_num_students": graduation_rate_150_asian_num_students,
                        "graduation_rate_150_aian_num_students": graduation_rate_150_aian_num_students,
                        "graduation_rate_150_nhpi_num_students": graduation_rate_150_nhpi_num_students,
                        "graduate_rate_150_2ormore_num_students": graduate_rate_150_2ormore_num_students,
                        "graduate_rate_150_nra_num_students": graduate_rate_150_nra_num_students,
                        "graduate_rate_150_unknown_num_students": graduate_rate_150_unknown_num_students,
                        "first_time_full_time_pell_grant_rate": first_time_full_time_pell_grant_rate,
                        "first_time_full_time_federal_loan_rate": first_time_full_time_federal_loan_rate,
                        "first_time_full_time_num_students": first_time_full_time_num_students,
                        "graduation_rate_200": graduation_rate_200,
                        "retention_rate_full_time": retention_rate_full_time,
                        "retention_rate_part_time": retention_rate_part_time,
                        "program_percentage_education": program_percentage_education,
                        "program_percentage_mathematics": program_percentage_mathematics,
                        "program_percentage_business_marketing": program_percentage_business_marketing,
                        "program_percentage_communications_technology": program_percentage_communications_technology,
                        "program_percentage_language": program_percentage_language,
                        "program_percentage_visual_performing": program_percentage_visual_performing,
                        "program_percentage_engineering_technology": program_percentage_engineering_technology,
                        "program_percentage_parks_recreation_fitness": program_percentage_parks_recreation_fitness,
                        "program_percentage_agriculture": program_percentage_agriculture,
                        "program_percentage_security_law_enforcement": program_percentage_security_law_enforcement,
                        "program_percentage_computer": program_percentage_computer,
                        "program_percentage_precision_production": program_percentage_precision_production,
                        "program_percentage_humanities": program_percentage_humanities,
                        "program_percentage_library": program_percentage_library,
                        "program_percentage_psychology": program_percentage_psychology,
                        "program_percentage_social_science": program_percentage_social_science,
                        "program_percentage_legal": program_percentage_legal,
                        "program_percentage_english": program_percentage_english,
                        "program_percentage_construction": program_percentage_construction,
                        "program_percentage_military": program_percentage_military,
                        "program_percentage_communication": program_percentage_communication,
                        "program_percentage_public_administration_social_service": program_percentage_public_administration_social_service,
                        "program_percentage_architecture": program_percentage_architecture,
                        "program_percentage_ethnic_cultural_gender": program_percentage_ethnic_cultural_gender,
                        "program_percentage_resources": program_percentage_resources,
                        "program_percentage_health": program_percentage_health,
                        "program_percentage_engineering": program_percentage_engineering,
                        "program_percentage_history": program_percentage_history,
                        "program_percentage_theology_religious_vocation": program_percentage_theology_religious_vocation,
                        "program_percentage_transportation": program_percentage_transportation,
                        "program_percentage_physical_science": program_percentage_physical_science,
                        "program_percentage_science_technology": program_percentage_science_technology,
                        "program_percentage_biological": program_percentage_biological,
                        "program_percentage_family_consumer_science": program_percentage_family_consumer_science,
                        "program_percentage_philosophy_religious": program_percentage_philosophy_religious,
                        "program_percentage_personal_culinary": program_percentage_personal_culinary,
                        "program_percentage_multidiscipline": program_percentage_multidiscipline,
                        "program_percentage_mechanic_repair_technology": program_percentage_mechanic_repair_technology,
                        "college": college_pk
                        }
                }
                # grab scorecard data from api 
                # with open(f'scorecard_updates.json', 'a+') as f:
                #     scorecard_data = json.dumps(seed, indent=2, ensure_ascii=False)
                #     f.write(scorecard_data + ',')

                return [seed, data]

    return [False]


def find_missing_colleges(file_name):
    colleges = json.load(open(f'{file_name}.json'))
    count = 6757
    for college in colleges: 
        count += 1
    
        data = scorecard_api(college, count)

        with open(f'scorecard_updates.json', 'a+') as f:
            scorecard_data = json.dumps(data[0], indent=2, ensure_ascii=False)
            f.write(scorecard_data + ',')
        print(f'  ==> COUNT: {count}')

# find_missing_colleges('missing')


def field_study_api(programs, college_pk):
    count = 1
    field_study_list = []

    for program in programs:
        cred_level = program.get('credential')['level']
        if cred_level < 4:
            cip_code = program.get('code')
            cip_title = program.get('title')
            credential_list = [None,
                               "Undergraduate Certificate or Diploma",
                               "Associate's Degree",
                               "Bachelor’s Degree",]
            credential_level = credential_list[cred_level or 0]
            credential_title = program.get('credential')['title'] or None
            num_students_debt = program.get('debt')['count'] or None
            median_debt = program.get('debt')['median_debt'] or None
            monthly_debt_payment = program.get(
                'debt')['monthly_debt_payment'] or None
            mean_debt = program.get('debt')['mean_debt'] or None
            num_students_titleiv = program.get('counts')['titleiv'] or None
            num_students_earnings = program.get(
                'earnings')['median_earnings']
            median_earnings = program.get(
                'earnings')['median_earnings'] or None
            num_students_ipeds_awards1 = program.get(
                'counts')['ipeds_awards1'] or None
            num_students_ipeds_awards2 = program.get(
                'counts')['ipeds_awards2'] or None
            seed = {
                "model": "colleges.FieldOfStudy",
                "pk": count,
                "fields": {
                    "cip_code": cip_code,
                    "cip_title": cip_title,
                    "credential_level": credential_level,
                    "credential_title": credential_title,
                    "num_students_debt": num_students_debt,
                    "median_debt": median_debt,
                    "monthly_debt_payment": monthly_debt_payment,
                    "mean_debt": mean_debt,
                    "num_students_titleiv": num_students_titleiv,
                    "num_students_earnings": num_students_earnings,
                    "median_earnings": median_earnings,
                    "num_students_ipeds_awards1": num_students_ipeds_awards1,
                    "num_students_ipeds_awards2": num_students_ipeds_awards2,
                    "college": college_pk
                }
            }
            field_study_list.append(seed)
            count += 1

    return field_study_list



def get_scorecard_data(file_name):
    colleges = json.load(open(f'{file_name}.json'))
    college_nums = len(colleges)
    print(f'  NUMBER OF COLLEGES ===> : {college_nums}')

    for college in colleges[2111:]:
        unit_id = college.get('fields')['unit_id']
        name = college.get('fields')['name']
        pk = college.get('pk')
        # 1000 calls per hour limit 
        # sleep(3.7)
        data = scorecard_api(unit_id, pk)
        scorecard = data[0]

        if scorecard:
            # latest = data[1].get('latest')
            # programs = latest.get('programs', None)

            # if programs: 
                print(f'  ==> COUNT: {pk}')
                # field_studies = field_study_api(programs['cip_4_digit'], pk)
                # append seed data
                with open(f'scorecard_updates.json', 'a+') as f:
                    scorecard_data = json.dumps(scorecard, indent=2, ensure_ascii=False)
                    f.write(scorecard_data + ',')
                # append college data
                with open(f'colleges_updates.json', 'a+') as f:
                    college_data = json.dumps(college, indent=2, ensure_ascii=False)
                    f.write(college_data + ',')
                # append field of study data
                # with open(f'field_study.json', 'a+') as f:
                #     field_study_data = json.dumps(field_studies, indent=2, ensure_ascii=False)
                #     f.write(field_study_data + ',')
        else: 
            print(f' NO SCORECARD ==> {name}')

    return print(f'   ==> DATA ALL DONE')

# use colleges_seeds.json() file
# get_scorecard_data('colleges')


def renumber_field_study_pk(file_name):
    field_studys = json.load(open(f'{file_name}.json'))
    print(f'  NUMBER OF COLLEGES ===> : {len(field_studys)}')

    count = 1
    field_study_list = []

    for field_study in field_studys[0:]:
        field_study['pk'] = count 
        field_study_list.append(field_study)
        count += 1

    with open(f'field_study_seeds.json', 'a+') as f:
        data = json.dumps(field_study_list, indent=2, ensure_ascii=False)
        f.write(data)

    return print(f'   ==> RENUMBERING ALL DONE')

# renumber_field_study_pk('field_study')


def update_scorecards(file_name):
    scorecards = json.load(open(f'{file_name}.json'))
    print(f'  NUMBER OF COLLEGES ===> : {len(scorecards)}')

    count = 1
    scorecard_list = []

    locale_list = [
        "null",
        "City: Large(population of 250, 000 or more)",
        "City: Midsize(population of at least 100, 000 but less than 250, 000)",
        "City: Small(population less than 100, 000)",
        "Suburb: Large(outside principal city, in urbanized area with population of 250, 000 or more)",
        "Suburb: Midsize(outside principal city, in urbanized area with population of at least 100, 000 but less than 250, 000)",
        "Suburb: Small(outside principal city, in urbanized area with population less than 100, 000)",
        "Town: Fringe ( in urban cluster up to 10 miles from an urbanized area)",
        "Town: Distant ( in urban cluster more than 10 miles and up to 35 miles from an urbanized area)",
        "Town: Remote ( in urban cluster more than 35 miles from an urbanized area)",
        "Rural: Fringe(rural territory up to 5 miles from an urbanized area or up to 2.5 miles from an urban cluster)",
        "Rural: Distant(rural territory more than 5 miles but up to 25 miles from an urbanized area or more than 2.5 and up to 10 miles from an urban cluster)",
        "Rural: Remote(rural territory more than 25 miles from an urbanized area and more than 10 miles from an urban cluster)"
    ]

    locale_new = [None,
                  "Large City", "Midsize City", "Small City",
                  "Large Suburb", "Midsize Suburb", "Small Suburb",
                  "Town", "Town", "Town",
                  "Rural", "Rural", "Rural"]

    carnegie_list = [
        None,
        "Not Applicable",
        "Not Classified",
        "Two-year, very small",
        "Two-year, small",
        "Two-year, medium",
        "Two-year, large",
        "Two-year, very large",
        "Four-year, very small, primarily nonresidential",
        "Four-year, very small, primarily residential",
        "Four-year, very small, highly residential",
        "Four-year, small, primarily nonresidential",
        "Four-year, small, primarily residential",
        "Four-year, small, highly residential",
        "Four-year, medium, primarily nonresidential",
        "Four-year, medium, primarily residential",
        "Four-year, medium, highly residential",
        "Four-year, large, primarily nonresidential",
        "Four-year, large, primarily residential",
        "Four-year, large, highly residential",
        "Exclusively graduate/professional"
    ]

    carnegie_new = [None, None, None,
                    "Very Small", "Small", "Medium", "Large", "Very Large",
                    "Very Small", "Very Small", "Very Small",
                    "Small", "Small", "Small",
                    "Medium", "Medium", "Medium",
                    "Large", "Large", "Large",
                    None]

    residental_new = [None, None, None,
                      "Commuter", "Commuter", "Commuter", "Commuter", "Commuter",
                      "Primarily Commuter", "Primarily Residential", "Highly Residential",
                      "Primarily Commuter", "Primarily Residential", "Highly Residential",
                      "Primarily Commuter", "Primarily Residential", "Highly Residential",
                      "Primarily Commuter", "Primarily Residential", "Highly Residential",
                      None]

    for scorecard in scorecards[0:]:
        # find index
        locale_index = locale_list.index(scorecard['fields']['locale'])
        carnegie_index = carnegie_list.index(scorecard['fields']['carnegie_size_setting'])

        # set new key with index of new list 
        scorecard['fields']['locale_updated'] = locale_new[locale_index]
        scorecard['fields']['carnegie_size_setting_size'] = carnegie_new[carnegie_index]
        scorecard['fields']['carnegie_size_setting_residential'] = residental_new[carnegie_index]

        # append updated scorecard to scorecard list
        scorecard_list.append(scorecard)
        print(f'  COUNT ===> : {count}')
        count += 1

    with open(f'scorecard_new.json', 'w') as f:
        data = json.dumps(scorecard_list, indent=2, ensure_ascii=False)
        f.write(data)

    return print(f'   ==> RENUMBERING ALL DONE')

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

def add_dates(file_name):
    collection = json.load(open(f'{file_name}.json'))
    d = datetime.datetime.now()
    timezone = pytz.timezone("America/Los_Angeles")
    d_aware = timezone.localize(d)
    count = 1

    for each in collection: 
        each['fields']['created'] = d_aware
        each['fields']['updated'] = d_aware

        with open(f'scorecard_seeds.json', 'a+') as f:
            data = json.dumps(each, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
            f.write(data + ',')

        print(f'  COUNT ===> : {count}')
        count += 1

    return print(f'   ==> DATES ADDED TO ALL DONE')

add_dates('seeds/scorecard_seeds')

def find(file_name):
    collection = json.load(open(f'{file_name}.json'))
    count = 1

    for each in collection: 
        unit_id = each['fields']['unit_id']
        each['fields']['unit_id'] = int(unit_id)

        with open(f'colleges_seedsINT.json', 'a+') as f:
            data = json.dumps(each, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
            f.write(data + ',')

        print(f'  COUNT ===> : {count}')
        count += 1

    return print(f'   ==> INT CHANGED TO ALL DONE')

# find('colleges_seeds')
