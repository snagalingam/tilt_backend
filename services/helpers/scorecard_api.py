
import os
import json
import requests


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
        breakpoint()
    except:
        pass

    if results is not None:
        # 1st level in results
        data = results[0]
        unit_id = data.get('id')
        ope_id = data.get('ope8_id')
        ope6_id = data.get('ope6_id')
        latitude = data.get('location')['lat']
        longitude = data.get('location')['lon']
        # 2nd level in results > school
        school = data.get('school')
        name = school.get('name')
        alias = school.get('alias')
        city = school.get('city')
        state = school.get('state')
        zipcode = school.get('zip')
        accreditor = school.get('accreditor')
        school_url = school.get('school_url')
        price_calculator_url = school.get('price_calculator_url')
        degree_awarded_data = school.get('degrees_awarded')
        degree_list = ["Not classified",
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
        # boolean list on line 20
        under_investigation = bool_list[school.get('under_investigation') or 2]
        main_campus = bool_list[school.get('main_campus') or 2]
        branches = school.get('branches')
        ownership_list = [None,
                        "Public",
                        "Private nonprofit",
                        "Private for-profit"]
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
        state_fips = state_dict[str(school.get('state_fips')) or "None"]
        region_list = ["U.S. Service Schools",
                    "New England(CT, ME, MA, NH, RI, VT)",
                    "Mid East(DE, DC, MD, NJ, NY, PA)",
                    "Great Lakes(IL, IN, MI, OH, WI)",
                    "Plains(IA, KS, MN, MO, NE, ND, SD)",
                    "Southeast(AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)",
                    "Southwest(AZ, NM, OK, TX)",
                    "Rocky Mountains(CO, ID, MT, UT, WY)",
                    "Far West(AK, CA, HI, NV, OR, WA)",
                    "Outlying Areas(AS, FM, GU, MH, MP, PR, PW, VI)",
                    None]
        region = region_list[school.get('region_id') or 10]
        local_dict = {
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
                locale = local_dict[str(locale)]
        urban_list = [None,
                    "Large City(a central city of a CMSA or MSA, with the city having a population greater than or equal to 250, 000)",
                    "Mid-Size City(a central city of a CMSA or MSA, with the city having a population less than 250, 000)",
                    "Urban Fringe of a Large City(any territory within a CMSA or MSA of a Large City and defined as urban by the Census Bureau)",
                    "Urban Fringe of a Mid-Size City(any territory within a CMSA or MSA of a Mid-Size City and defined as urban by the Census Bureau)",
                    "Large Town(an incorporated place or Census-designated place with a population greater than or equal to 25, 000 and located outside a CMSA or MSA)",
                    "Small Town(an incorporated place or Census-designated place with a population less than 25, 000 and greater than or equal to 2, 500 and located outside a CMSA or MSA)",
                    "Rural, Outside MSA(any territory designated as rural by the Census Bureau that is outside a CMSA or MSA of a Large or Mid-Size City)",
                    "Rural, Inside MSA(any territory designated as rural by the Census Bureau that is within a CMSA or MSA of a Large or Mid-Size City)"]
        degree_urbanization = urban_list[school.get(
            'degree_urbanization') or 0]
        carnegie_basic_dict = {
            "None": None,
            "-2": "Not applicable",
            "0": "(Not classified)",
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
            "-2": "Not applicable",
            "0": "Not classified(Exclusively Graduate)",
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
            "-2": "Not applicable",
            "0": "(Not classified)",
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
        operating = bool_list[school.get('operating') or 2]
        institutional_list = [None,
                            "4-year",
                            "2-year",
                            "Less-than-2-year"]
        institutional_level = institutional_list[school.get(
            'institutional_characteristics')['level'] or 0]
        open_list = [None, True, False, False]
        open_admissions = open_list[school.get('open_admissions_policy') or 0]
        religious_dict = {
            "-1": "Not reported",
            "-2": "Not applicable",
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
        # 2nd level in results > latest
        latest = data.get('latest')
        # 3rd level in results > lastest > admissions
        admissions = latest.get('admissions')
        admissions_rate = admissions.get('admission_rate')['overall']
        # 4th level in results > lastest > admissions > sat_scores
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
        # 4th level in results > lastest > admissions > act_scores
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
        # 3rd level in results > lastest > student
        student = latest.get('student')
        undergraduate_students = student.get('size') or None
        undergraduate_students_parttime = student.get(
            'part_time_share') or None
        share_25_older = student.get('share_25_older')
        students_with_pell_grant = student.get(
            'students_with_pell_grant') or None
        first_time_full_time = student.get(
            'share_first')['time_full']['time'] or None
        first_time_full_time_num_students = student.get(
            'ftft_undergrads_with_pell_grant_or_federal_student_loan') or None
        
        # 4th level in results > lastest > students > retention_rate
        retention_rate = student.get('retention_rate')
        retention_rate_full_time = retention_rate.get(
            'four_year')['full_time'] or retention_rate.get('lt_four_year')['full_time']
        retention_rate_part_time = retention_rate.get(
            'four_year')['part_time'] or retention_rate.get('lt_four_year')['part_time']
        # 4th level in results > lastest > students > demographics
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
        # 3rd level in results > lastest > cost
        cost = latest.get('cost')
        avg_net_price = cost.get('avg_net_price')[
            'public'] or cost.get('avg_net_price')['private']
        # 4th level in results > lastest > cost > net_price
        net_price = cost.get('net_price')
        net_price_public = net_price.get('public')
        net_price_private = net_price.get('private')
        avg_net_price_lo = net_price_public.get(
            '0-3000') or net_price_private.get('0-3000')
        avg_net_price_m1 = net_price_public.get(
            '30001-48000') or net_price_private.get('30001-48000')
        avg_net_price_m2 = net_price_public.get(
            '48001-75000') or net_price_private.get('48001-75000')
        avg_net_price_h1 = net_price_public.get(
            '75001-110000') or net_price_private.get('75001-110000')
        avg_net_price_h2 = net_price_public.get(
            '110001-plus') or net_price_private.get('110001-plus')
        # 4th level in results > lastest > cost > attendance
        attendance = cost.get('attendance')
        cost_of_attendance = attendance.get(
            'academic_year') or attendance.get('program_year')
        # 4th level in results > lastest > cost > tuition
        tuition = cost.get('tuition')
        tuition_in_state = tuition.get('in_state') or None
        tuition_out_of_state = tuition.get('out_of_state') or None
        tuition_program_year = tuition.get('program_year') or None
        # 3rd level in results > lastest > aid
        aid = latest.get('aid')
        pell_grant_rate = aid.get('pell_grant_rate') or None
        federal_loan_rate = aid.get('federal_loan_rate') or None
        median_debt = aid.get('loan_principal') or None
        first_time_full_time_pell_grant_rate = aid.get('ftft_pell_grant_rate') or None
        first_time_full_time_federal_loan_rate = aid.get(
            'ftft_federal_loan_rate') or None
        # 4th level in results > lastest > aid > median_debt
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
        # 3rd level in results > lastest > repayment
        repayment = latest.get('repayment')
        default_rate_2yr = repayment.get('2_yr_default_rate') or None
        default_rate_3yr = repayment.get('3_yr_default_rate') or None
        default_rate_2yr_num_students = repayment.get(
            '2_yr_default_rate_denom') or None
        default_rate_3yr_num_students = repayment.get(
            '3_yr_default_rate_denom') or None
        # 3rd level in results > lastest > completion
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
                "degree_urbanization": degree_urbanization,
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
                "college": college_pk
                }
        }

    return seed


def get_scorecard_data(file_name):
    colleges = json.load(open(f'{file_name}.json'))
    college_nums = len(colleges)
    print(f'  NUMBER OF COLLEGES ===> : {college_nums}')
    scorecard_list = []

    for college in colleges[3909:]:
        unit_id = college.get('fields')['unit_id']
        name = college.get('fields')['name']
        pk = college.get('pk')
        print(f'  ==> COUNT: {pk}')
        print(f'  ==> NAME: {name}')

        seed = scorecard_api(unit_id, pk)
        scorecard_list.append(seed)

        # if count == 100: 
        #     with open(f'scorecard_seeds.json', 'w') as f:
        #         data = json.dumps(scorecard_list, indent=2)
        #         f.write(data)
        #     break

        with open(f'scorecard_seeds1.json', 'w') as f:
            data = json.dumps(scorecard_list, indent=2)
            f.write(data)

    return print(f'   ==> DATA ALL DONE')

# use colleges_seeds.json() file
# get_scorecard_data('colleges_seeds')

def merge_json(*args):
    a = json.load(open(f'{args[0]}.json'))
    b = json.load(open(f'{args[1]}.json'))
    c = json.load(open(f'{args[2]}.json'))
    d = json.load(open(f'{args[3]}.json'))
    e = json.load(open(f'{args[4]}.json'))
    f = json.load(open(f'{args[5]}.json'))
    g = json.load(open(f'{args[6]}.json'))
    merged = a + b + c + d + e + f + g

    with open(f'scorecard_seeds.json', 'w') as f:
        data = json.dumps(merged, indent=2)
        f.write(data)

    return print(f'   ==> MERGE COMPLETE')


# merge_json(
#     'scorecard_seeds0',
#     'scorecard_seeds1',
#     'scorecard_seeds2',
#     'scorecard_seeds3',
#     'scorecard_seeds4',
#     'scorecard_seeds5',
#     'scorecard_seeds6')
