from colleges.models import Budget, College, CollegeStatus, FieldOfStudy, Scorecard
from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()

class CollegeTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email="demouser@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo",
            last_name="Testuser"
        )
        college = College.objects.create(
            popularity_score=1,
            unit_id=100654,
            ope_id="00100200",
            place_id="ChIJ91htBQIXYogRtPsg4NGoNv0",
            business_status= "OPERATIONAL",
            name="Alabama A&M University",
            address="Huntsville, AL 35811, USA",
            phone_number="(256) 372-5000",
            lat=34.7827196,
            lng=-86.568614,
            url="https://maps.google.com/?cid=18245956559700032436",
            website="http://www.aamu.edu/",
            favicon="https://www.aamu.edu/_resources/img/icons/favicon-196x196.png",
            description="Alabama A&M University is a top ranked public university offering associates, undergraduate, graduate and doctoral degrees.",
            main_photo="https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048",
            photos=["https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048",
            "https://lh3.googleusercontent.com/places/ABKp1IqVV9NSRdkeVV4eDiGEySagrugrK2ryXcrzpzGN-IzNftQ37xqUx7OQcgUkjnsd32cPDQcfsO1RAbgfredazdmk9zyeZTuuutQ=s1600-w2560",
            "https://lh3.googleusercontent.com/places/ABKp1IqlYDobf55GX0Y6pPVnISOO6ZBfsCtM9Z_1_AL8VakFdHnoAcjU1cYT83Lzdoh-FjH0cBF43U_cCzSfjp28SwI1CjKXyYtTbEM=s1600-w2048",
            "https://lh3.googleusercontent.com/places/ABKp1IoWIutn-aNT33reyZv9QmvmHrSJ4V_BoC8paCJeEfXeOZcfKi3ZFgbRagHKxQhQOiNXJOI2bZLtMy9iWT8CxUWJk2L2ZHaRpdg=s1600-w1536",
            "https://lh3.googleusercontent.com/places/ABKp1IotKWni5j2Ac5ZZANdOqpmVagiwnvzO7mQy1C-KNURivHWF6Ui6SllbzTp8AOdiReqiFXZOJvscLVDSCgwqr6APEVDz7zUTguI=s1600-w3264",
            "https://lh3.googleusercontent.com/places/ABKp1IqRn6d9T0Dw2vsaP2b08DNLXrWUUz9VjuUTPOnPY7T1pzjFG4CjdsqZgrENLVya3zSBxGyjUdjjJFX5GesV3MA7nEbijf8DAfs=s1600-w1695",
            "https://lh3.googleusercontent.com/places/ABKp1IqBUtkqITPk0zKctRz6dwgWema8bvUjZGO-E3rtzRwBrvle-GIUvgRDeSMUwX8tJdG1fLLydYJ2bJuEFYNMjna9O0zk3GhsPfo=s1600-w6016",
            "https://lh3.googleusercontent.com/places/ABKp1IqvT48dPKMA5OsHpBdLElYVgGb_HDFoTXPqo_cM_mVCHFLvPWvjphwVSCbHw3tZdeQi5O67HT0-peLQiTOg29WYfHOVIuLEjVM=s1600-w4032",
            "https://lh3.googleusercontent.com/places/ABKp1IoPkQjJ1uvn9JvjougnKvWlUppDe6OZis_7rRSX2Z0EBfdRXN0iLu9B8WYAvnBke-wckEOY_V5xUnJs-FLm_8Gvo3fse54_Rag=s1600-w2048",
            "https://lh3.googleusercontent.com/places/ABKp1IpvJcp40b6PKpaNfkgc9jJu6NN8nneLkfSropV-N1DZmuNJBoAD3a9FM5grPGv9Qw_hw-PVDETm47ywkggYztJagMm44pxqNS0=s1600-w2048"],
            types=["university", "point_of_interest", "establishment"]
        )
        CollegeStatus.objects.create(
            user=user,
            college=college,
            status="interested",
            net_price=25000,
            award_uploaded=True,
            award_reviewed=False,
            user_notified=False,
            residency="NY",
            in_state_tuition="NY"
        )

    def test_create_college(self):
        college = College.objects.create(
            popularity_score=2,
            unit_id=100663,
            ope_id="00105200",
            place_id="ChIJRxq4YekbiYgRS7BbCPlZxlE",
            business_status= "OPERATIONAL",
            name="University of Alabama at Birmingham",
            address="1720 University Blvd, Birmingham, AL 35294, USA",
            phone_number="(205) 934-4011",
            lat=33.5019893,
            lng=-86.8064433,
            url="https://maps.google.com/?cid=5892496088582828107",
            website="http://www.uab.edu/",
            favicon="https://www.uab.edu/styles/5.0/images/favicons/favicon-196x196.png",
            description="University of Alabama at Birmingham is a top ranked public university offering associates, undergraduate, graduate and doctoral degrees.",
            main_photo="https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048",
            photos=["https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IqVV9NSRdkeVV4eDiGEySagrugrK2ryXcrzpzGN-IzNftQ37xqUx7OQcgUkjnsd32cPDQcfsO1RAbgfredazdmk9zyeZTuuutQ=s1600-w2560",
                "https://lh3.googleusercontent.com/places/ABKp1IqlYDobf55GX0Y6pPVnISOO6ZBfsCtM9Z_1_AL8VakFdHnoAcjU1cYT83Lzdoh-FjH0cBF43U_cCzSfjp28SwI1CjKXyYtTbEM=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IoWIutn-aNT33reyZv9QmvmHrSJ4V_BoC8paCJeEfXeOZcfKi3ZFgbRagHKxQhQOiNXJOI2bZLtMy9iWT8CxUWJk2L2ZHaRpdg=s1600-w1536",
                "https://lh3.googleusercontent.com/places/ABKp1IotKWni5j2Ac5ZZANdOqpmVagiwnvzO7mQy1C-KNURivHWF6Ui6SllbzTp8AOdiReqiFXZOJvscLVDSCgwqr6APEVDz7zUTguI=s1600-w3264",
                "https://lh3.googleusercontent.com/places/ABKp1IqRn6d9T0Dw2vsaP2b08DNLXrWUUz9VjuUTPOnPY7T1pzjFG4CjdsqZgrENLVya3zSBxGyjUdjjJFX5GesV3MA7nEbijf8DAfs=s1600-w1695",
                "https://lh3.googleusercontent.com/places/ABKp1IqBUtkqITPk0zKctRz6dwgWema8bvUjZGO-E3rtzRwBrvle-GIUvgRDeSMUwX8tJdG1fLLydYJ2bJuEFYNMjna9O0zk3GhsPfo=s1600-w6016",
                "https://lh3.googleusercontent.com/places/ABKp1IqvT48dPKMA5OsHpBdLElYVgGb_HDFoTXPqo_cM_mVCHFLvPWvjphwVSCbHw3tZdeQi5O67HT0-peLQiTOg29WYfHOVIuLEjVM=s1600-w4032",
                "https://lh3.googleusercontent.com/places/ABKp1IoPkQjJ1uvn9JvjougnKvWlUppDe6OZis_7rRSX2Z0EBfdRXN0iLu9B8WYAvnBke-wckEOY_V5xUnJs-FLm_8Gvo3fse54_Rag=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IpvJcp40b6PKpaNfkgc9jJu6NN8nneLkfSropV-N1DZmuNJBoAD3a9FM5grPGv9Qw_hw-PVDETm47ywkggYztJagMm44pxqNS0=s1600-w2048"],
            types=["university", "point_of_interest", "establishment"]
        )
        self.assertEqual(college.popularity_score, 2)
        self.assertEqual(college.unit_id, 100663)
        self.assertEqual(college.ope_id, "00105200")
        self.assertEqual(college.place_id, "ChIJRxq4YekbiYgRS7BbCPlZxlE")
        self.assertEqual(college.business_status, "OPERATIONAL")
        self.assertEqual(college.name, "University of Alabama at Birmingham")
        self.assertEqual(college.address, "1720 University Blvd, Birmingham, AL 35294, USA")
        self.assertEqual(college.phone_number, "(205) 934-4011")
        self.assertEqual(college.lat, 33.5019893)
        self.assertEqual(college.lng,  -86.8064433)
        self.assertEqual(college.url, "https://maps.google.com/?cid=5892496088582828107")
        self.assertEqual(college.website, "http://www.uab.edu/")
        self.assertEqual(college.favicon, "https://www.uab.edu/styles/5.0/images/favicons/favicon-196x196.png")
        self.assertEqual(college.description, "University of Alabama at Birmingham is a top ranked public university offering associates, undergraduate, graduate and doctoral degrees.")
        self.assertEqual(college.main_photo, "https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048")
        self.assertEqual(college.photos, ["https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IqVV9NSRdkeVV4eDiGEySagrugrK2ryXcrzpzGN-IzNftQ37xqUx7OQcgUkjnsd32cPDQcfsO1RAbgfredazdmk9zyeZTuuutQ=s1600-w2560",
                "https://lh3.googleusercontent.com/places/ABKp1IqlYDobf55GX0Y6pPVnISOO6ZBfsCtM9Z_1_AL8VakFdHnoAcjU1cYT83Lzdoh-FjH0cBF43U_cCzSfjp28SwI1CjKXyYtTbEM=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IoWIutn-aNT33reyZv9QmvmHrSJ4V_BoC8paCJeEfXeOZcfKi3ZFgbRagHKxQhQOiNXJOI2bZLtMy9iWT8CxUWJk2L2ZHaRpdg=s1600-w1536",
                "https://lh3.googleusercontent.com/places/ABKp1IotKWni5j2Ac5ZZANdOqpmVagiwnvzO7mQy1C-KNURivHWF6Ui6SllbzTp8AOdiReqiFXZOJvscLVDSCgwqr6APEVDz7zUTguI=s1600-w3264",
                "https://lh3.googleusercontent.com/places/ABKp1IqRn6d9T0Dw2vsaP2b08DNLXrWUUz9VjuUTPOnPY7T1pzjFG4CjdsqZgrENLVya3zSBxGyjUdjjJFX5GesV3MA7nEbijf8DAfs=s1600-w1695",
                "https://lh3.googleusercontent.com/places/ABKp1IqBUtkqITPk0zKctRz6dwgWema8bvUjZGO-E3rtzRwBrvle-GIUvgRDeSMUwX8tJdG1fLLydYJ2bJuEFYNMjna9O0zk3GhsPfo=s1600-w6016",
                "https://lh3.googleusercontent.com/places/ABKp1IqvT48dPKMA5OsHpBdLElYVgGb_HDFoTXPqo_cM_mVCHFLvPWvjphwVSCbHw3tZdeQi5O67HT0-peLQiTOg29WYfHOVIuLEjVM=s1600-w4032",
                "https://lh3.googleusercontent.com/places/ABKp1IoPkQjJ1uvn9JvjougnKvWlUppDe6OZis_7rRSX2Z0EBfdRXN0iLu9B8WYAvnBke-wckEOY_V5xUnJs-FLm_8Gvo3fse54_Rag=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IpvJcp40b6PKpaNfkgc9jJu6NN8nneLkfSropV-N1DZmuNJBoAD3a9FM5grPGv9Qw_hw-PVDETm47ywkggYztJagMm44pxqNS0=s1600-w2048"])
        self.assertEqual(college.types, ["university", "point_of_interest", "establishment"])
        self.assertIsNotNone(college.created)
        self.assertIsNotNone(college.updated)

    def test_create_scorecard(self):
        college = College.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")
        scorecard = Scorecard.objects.create(
            college=college,
            unit_id=100654,
            ope_id="00100200",
            ope6_id="001002",
            name="Alabama A & M University",
            city="Normal",
            state="AL",
            zipcode="35762",
            accreditor="Southern Association of Colleges and Schools Commission on Colleges",
            school_url="www.aamu.edu/",
            price_calculator_url="www.aamu.edu/admissions-aid/tuition-fees/net-price-calculator.html",
            predominant_degree_awarded_recoded="Predominantly bachelor's-degree granting",
            under_investigation=False,
            main_campus=True,
            branches=1,
            predominant_degree_awarded="Predominantly bachelor's-degree granting",
            highest_degree_awarded="Graduate degree",
            ownership="Public",
            state_fips="Alabama",
            region="Southeast",
            locale="City: Midsize(population of at least 100, 000 but less than 250, 000)",
            locale_updated="Midsize City",
            latitude=34.783368,
            longitude=-86.568502,
            carnegie_basic="Master's Colleges & Universities: Larger Programs",
            carnegie_undergrad="Four-year, full-time, inclusive, lower transfer-in",
            carnegie_size_setting="Four-year, medium, highly residential",
            carnegie_size_setting_size="Medium",
            carnegie_size_setting_residential="Highly Residential",
            minority_serving_historically_black=True,
            minority_serving_predominantly_black=False,
            minority_serving_annh=False,
            minority_serving_tribal=False,
            minority_serving_aanipi=False,
            minority_serving_hispanic=False,
            minority_serving_nant=False,
            men_only=False,
            women_only=False,
            religious_affiliation=None,
            admissions_rate=0.8986,
            sat_reading_25th_percentile=430.0,
            sat_reading_75th_percentile=520.0,
            sat_math_25th_percentile=420.0,
            sat_math_75th_percentile=510.0,
            sat_writing_25th_percentile=370.0,
            sat_writing_75th_percentile=457.0,
            sat_reading_midpoint=475.0,
            sat_math_midpoint=465.0,
            sat_writing_midpoint=414.0,
            act_cumulative_25th_percentile=16.0,
            act_cumulative_75th_percentile=19.0,
            act_english_25th_percentile=14.0,
            act_english_75th_percentile=20.0,
            act_math_25th_percentile=15.0,
            act_math_75th_percentile=18.0,
            act_writing_25th_percentile=None,
            act_writing_75th_percentile=None,
            act_cumulative_midpoint=18.0,
            act_english_midpoint=17.0,
            act_math_midpoint=17.0,
            act_writing_midpoint=None,
            sat_average=957.0,
            online_only=False,
            undergraduate_students=4990,
            undergraduate_students_white=0.0186,
            undergraduate_students_black=0.912,
            undergraduate_students_hispanic=0.0088,
            undergraduate_students_asian=0.0018,
            undergraduate_students_aian=0.0022,
            undergraduate_students_nhpi=0.0016,
            undergraduate_students_2ormore=0.0118,
            undergraduate_students_nra=0.007,
            undergraduate_students_unknown=0.0361,
            undergraduate_students_parttime=0.0587,
            operating=True,
            avg_net_price=14444,
            avg_net_price_lo=13893,
            avg_net_price_m1=13976,
            avg_net_price_m2=15995,
            avg_net_price_h1=18957,
            avg_net_price_h2=17140,
            cost_of_attendance=22489,
            tuition_in_state=9744,
            tuition_out_of_state=18354,
            tuition_program_year=None,
            pell_grant_rate=0.7067,
            federal_loan_rate=0.7503,
            share_25_older=0.0758,
            default_rate_2yr=0.114,
            default_rate_3yr=0.182,
            median_debt=15000.0,
            median_debt_completers=34500.0,
            median_debt_noncompleters=9500.0,
            median_debt_num_students=3338,
            median_debt_completers_num_students=1068,
            median_debt_noncompleters_num_students=2270,
            monthly_loan_payments=358.0516353,
            students_with_any_loan=None,
            students_with_pell_grant=0.852793471,
            age_entry=20,
            veteran=0.003138732,
            first_generation=0.365828092,
            alias="AAMU",
            graduation_rate_100=0.0556,
            graduation_rate_100_num_students=756,
            institutional_level="4-year",
            undergraduate_students_men=0.4076,
            undergraduate_students_women=0.5924,
            default_rate_2yr_num_students=1574,
            default_rate_3yr_num_students=1875,
            open_admissions=False,
            graduation_rate_150=0.2685,
            first_time_full_time=0.8987,
            graduation_rate_150_white=0.25,
            graduation_rate_150_black=0.2681,
            graduation_rate_150_hispanic=0.25,
            graduation_rate_150_asian=None,
            graduation_rate_150_aian=None,
            graduation_rate_150_nhpi=None,
            graduate_rate_150_2ormore=0.25,
            graduate_rate_150_nra=None,
            graduate_rate_150_unknown=0.375,
            graduation_rate_150_white_num_students=8,
            graduation_rate_150_black_num_students=731,
            graduation_rate_150_hispanic_num_students=4,
            graduation_rate_150_asian_num_students=None,
            graduation_rate_150_aian_num_students=None,
            graduation_rate_150_nhpi_num_students=1,
            graduate_rate_150_2ormore_num_students=4,
            graduate_rate_150_nra_num_students=None,
            graduate_rate_150_unknown_num_students=8,
            first_time_full_time_pell_grant_rate=0.7057,
            first_time_full_time_federal_loan_rate=0.7143,
            first_time_full_time_num_students=1288,
            graduation_rate_200=0.35,
            retention_rate_full_time=0.6087,
            retention_rate_part_time=1.0,
            program_percentage_education=0.071,
            program_percentage_mathematics=0.0059,
            program_percentage_business_marketing=0.1578,
            program_percentage_communications_technology=0.0394,
            program_percentage_language=0.0,
            program_percentage_visual_performing=0.0237,
            program_percentage_engineering_technology=0.0197,
            program_percentage_parks_recreation_fitness=0.002,
            program_percentage_agriculture=0.0394,
            program_percentage_security_law_enforcement=0.0572,
            program_percentage_computer=0.0592,
            program_percentage_precision_production=0.0,
            program_percentage_humanities=0.0473,
            program_percentage_library=0.0,
            program_percentage_psychology=0.0631,
            program_percentage_social_science=0.0355,
            program_percentage_legal=0.0,
            program_percentage_english=0.0158,
            program_percentage_construction=0.0,
            program_percentage_military=0.0,
            program_percentage_communication=0.0,
            program_percentage_public_administration_social_service=0.0493,
            program_percentage_architecture=0.0039,
            program_percentage_ethnic_cultural_gender=0.0,
            program_percentage_resources=0.0237,
            program_percentage_health=0.0,
            program_percentage_engineering=0.1183,
            program_percentage_history=0.0,
            program_percentage_theology_religious_vocation=0.0,
            program_percentage_transportation=0.0,
            program_percentage_physical_science=0.0355,
            program_percentage_science_technology=0.0,
            program_percentage_biological=0.0927,
            program_percentage_family_consumer_science=0.0394,
            program_percentage_philosophy_religious=0.0,
            program_percentage_personal_culinary=0.0,
            program_percentage_multidiscipline=0.0,
            program_percentage_mechanic_repair_technology=0.0
        )

        self.assertEqual(scorecard.college, college)
        self.assertEqual(scorecard.unit_id, 100654)
        self.assertEqual(scorecard.ope_id, "00100200")
        self.assertEqual(scorecard.ope6_id, "001002")
        self.assertEqual(scorecard.name, "Alabama A & M University")
        self.assertEqual(scorecard.city, "Normal")
        self.assertEqual(scorecard.state, "AL")
        self.assertEqual(scorecard.zipcode, "35762")
        self.assertEqual(scorecard.accreditor, "Southern Association of Colleges and Schools Commission on Colleges")
        self.assertEqual(scorecard.school_url, "www.aamu.edu/")
        self.assertEqual(scorecard.price_calculator_url, "www.aamu.edu/admissions-aid/tuition-fees/net-price-calculator.html")
        self.assertEqual(scorecard.predominant_degree_awarded_recoded, "Predominantly bachelor's-degree granting")
        self.assertEqual(scorecard.under_investigation, False)
        self.assertEqual(scorecard.main_campus, True)
        self.assertEqual(scorecard.branches, 1)
        self.assertEqual(scorecard.predominant_degree_awarded, "Predominantly bachelor's-degree granting")
        self.assertEqual(scorecard.highest_degree_awarded, "Graduate degree")
        self.assertEqual(scorecard.ownership, "Public")
        self.assertEqual(scorecard.state_fips, "Alabama")
        self.assertEqual(scorecard.region, "Southeast")
        self.assertEqual(scorecard.locale, "City: Midsize(population of at least 100, 000 but less than 250, 000)")
        self.assertEqual(scorecard.locale_updated, "Midsize City")
        self.assertEqual(scorecard.latitude, 34.783368)
        self.assertEqual(scorecard.longitude, -86.568502)
        self.assertEqual(scorecard.carnegie_basic, "Master's Colleges & Universities: Larger Programs")
        self.assertEqual(scorecard.carnegie_undergrad, "Four-year, full-time, inclusive, lower transfer-in")
        self.assertEqual(scorecard.carnegie_size_setting, "Four-year, medium, highly residential")
        self.assertEqual(scorecard.carnegie_size_setting_size, "Medium")
        self.assertEqual(scorecard.carnegie_size_setting_residential, "Highly Residential")
        self.assertEqual(scorecard.minority_serving_historically_black, True)
        self.assertEqual(scorecard.minority_serving_predominantly_black, False)
        self.assertEqual(scorecard.minority_serving_annh, False)
        self.assertEqual(scorecard.minority_serving_tribal, False)
        self.assertEqual(scorecard.minority_serving_aanipi, False)
        self.assertEqual(scorecard.minority_serving_hispanic, False)
        self.assertEqual(scorecard.minority_serving_nant, False)
        self.assertEqual(scorecard.men_only, False)
        self.assertEqual(scorecard.women_only, False)
        self.assertEqual(scorecard.religious_affiliation, None)
        self.assertEqual(scorecard.admissions_rate, 0.8986)
        self.assertEqual(scorecard.sat_reading_25th_percentile, 430.0)
        self.assertEqual(scorecard.sat_reading_75th_percentile, 520.0)
        self.assertEqual(scorecard.sat_math_25th_percentile, 420.0)
        self.assertEqual(scorecard.sat_math_75th_percentile, 510.0)
        self.assertEqual(scorecard.sat_writing_25th_percentile, 370.0)
        self.assertEqual(scorecard.sat_writing_75th_percentile, 457.0)
        self.assertEqual(scorecard.sat_reading_midpoint, 475.0)
        self.assertEqual(scorecard.sat_math_midpoint, 465.0)
        self.assertEqual(scorecard.sat_writing_midpoint, 414.0)
        self.assertEqual(scorecard.act_cumulative_25th_percentile, 16.0)
        self.assertEqual(scorecard.act_cumulative_75th_percentile, 19.0)
        self.assertEqual(scorecard.act_english_25th_percentile, 14.0)
        self.assertEqual(scorecard.act_english_75th_percentile, 20.0)
        self.assertEqual(scorecard.act_math_25th_percentile, 15.0)
        self.assertEqual(scorecard.act_math_75th_percentile, 18.0)
        self.assertEqual(scorecard.act_writing_25th_percentile, None)
        self.assertEqual(scorecard.act_writing_75th_percentile, None)
        self.assertEqual(scorecard.act_cumulative_midpoint, 18.0)
        self.assertEqual(scorecard.act_english_midpoint, 17.0)
        self.assertEqual(scorecard.act_math_midpoint, 17.0)
        self.assertEqual(scorecard.act_writing_midpoint, None)
        self.assertEqual(scorecard.sat_average, 957.0)
        self.assertEqual(scorecard.online_only, False)
        self.assertEqual(scorecard.undergraduate_students, 4990)
        self.assertEqual(scorecard.undergraduate_students_white, 0.0186)
        self.assertEqual(scorecard.undergraduate_students_black, 0.912)
        self.assertEqual(scorecard.undergraduate_students_hispanic, 0.0088)
        self.assertEqual(scorecard.undergraduate_students_asian, 0.0018)
        self.assertEqual(scorecard.undergraduate_students_aian, 0.0022)
        self.assertEqual(scorecard.undergraduate_students_nhpi, 0.0016)
        self.assertEqual(scorecard.undergraduate_students_2ormore, 0.0118)
        self.assertEqual(scorecard.undergraduate_students_nra, 0.007)
        self.assertEqual(scorecard.undergraduate_students_unknown, 0.0361)
        self.assertEqual(scorecard.undergraduate_students_parttime, 0.0587)
        self.assertEqual(scorecard.operating, True)
        self.assertEqual(scorecard.avg_net_price, 14444)
        self.assertEqual(scorecard.avg_net_price_lo, 13893)
        self.assertEqual(scorecard.avg_net_price_m1, 13976)
        self.assertEqual(scorecard.avg_net_price_m2, 15995)
        self.assertEqual(scorecard.avg_net_price_h1, 18957)
        self.assertEqual(scorecard.avg_net_price_h2, 17140)
        self.assertEqual(scorecard.cost_of_attendance, 22489)
        self.assertEqual(scorecard.tuition_in_state, 9744)
        self.assertEqual(scorecard.tuition_out_of_state, 18354)
        self.assertEqual(scorecard.tuition_program_year, None)
        self.assertEqual(scorecard.pell_grant_rate, 0.7067)
        self.assertEqual(scorecard.federal_loan_rate, 0.7503)
        self.assertEqual(scorecard.share_25_older, 0.0758)
        self.assertEqual(scorecard.default_rate_2yr, 0.114)
        self.assertEqual(scorecard.default_rate_3yr, 0.182)
        self.assertEqual(scorecard.median_debt, 15000.0)
        self.assertEqual(scorecard.median_debt_completers, 34500.0)
        self.assertEqual(scorecard.median_debt_noncompleters, 9500.0)
        self.assertEqual(scorecard.median_debt_num_students, 3338)
        self.assertEqual(scorecard.median_debt_completers_num_students, 1068)
        self.assertEqual(scorecard.median_debt_noncompleters_num_students, 2270)
        self.assertEqual(scorecard.monthly_loan_payments, 358.0516353)
        self.assertEqual(scorecard.students_with_any_loan, None)
        self.assertEqual(scorecard.students_with_pell_grant, 0.852793471)
        self.assertEqual(scorecard.age_entry, 20)
        self.assertEqual(scorecard.veteran, 0.003138732)
        self.assertEqual(scorecard.first_generation, 0.365828092)
        self.assertEqual(scorecard.alias, "AAMU")
        self.assertEqual(scorecard.graduation_rate_100, 0.0556)
        self.assertEqual(scorecard.graduation_rate_100_num_students, 756)
        self.assertEqual(scorecard.institutional_level, "4-year")
        self.assertEqual(scorecard.undergraduate_students_men, 0.4076)
        self.assertEqual(scorecard.undergraduate_students_women, 0.5924)
        self.assertEqual(scorecard.default_rate_2yr_num_students, 1574)
        self.assertEqual(scorecard.default_rate_3yr_num_students, 1875)
        self.assertEqual(scorecard.open_admissions, False)
        self.assertEqual(scorecard.graduation_rate_150, 0.2685)
        self.assertEqual(scorecard.first_time_full_time, 0.8987)
        self.assertEqual(scorecard.graduation_rate_150_white, 0.25)
        self.assertEqual(scorecard.graduation_rate_150_black, 0.2681)
        self.assertEqual(scorecard.graduation_rate_150_hispanic, 0.25)
        self.assertEqual(scorecard.graduation_rate_150_asian, None)
        self.assertEqual(scorecard.graduation_rate_150_aian, None)
        self.assertEqual(scorecard.graduation_rate_150_nhpi, None)
        self.assertEqual(scorecard.graduate_rate_150_2ormore, 0.25)
        self.assertEqual(scorecard.graduate_rate_150_nra, None)
        self.assertEqual(scorecard.graduate_rate_150_unknown, 0.375)
        self.assertEqual(scorecard.graduation_rate_150_white_num_students, 8)
        self.assertEqual(scorecard.graduation_rate_150_black_num_students, 731)
        self.assertEqual(scorecard.graduation_rate_150_hispanic_num_students, 4)
        self.assertEqual(scorecard.graduation_rate_150_asian_num_students, None)
        self.assertEqual(scorecard.graduation_rate_150_aian_num_students, None)
        self.assertEqual(scorecard.graduation_rate_150_nhpi_num_students, 1)
        self.assertEqual(scorecard.graduate_rate_150_2ormore_num_students, 4)
        self.assertEqual(scorecard.graduate_rate_150_nra_num_students, None)
        self.assertEqual(scorecard.graduate_rate_150_unknown_num_students, 8)
        self.assertEqual(scorecard.first_time_full_time_pell_grant_rate, 0.7057)
        self.assertEqual(scorecard.first_time_full_time_federal_loan_rate, 0.7143)
        self.assertEqual(scorecard.first_time_full_time_num_students, 1288)
        self.assertEqual(scorecard.graduation_rate_200, 0.35)
        self.assertEqual(scorecard.retention_rate_full_time, 0.6087)
        self.assertEqual(scorecard.retention_rate_part_time, 1.0)
        self.assertEqual(scorecard.program_percentage_education, 0.071)
        self.assertEqual(scorecard.program_percentage_mathematics, 0.0059)
        self.assertEqual(scorecard.program_percentage_business_marketing, 0.1578)
        self.assertEqual(scorecard.program_percentage_communications_technology, 0.0394)
        self.assertEqual(scorecard.program_percentage_language, 0.0)
        self.assertEqual(scorecard.program_percentage_visual_performing, 0.0237)
        self.assertEqual(scorecard.program_percentage_engineering_technology, 0.0197)
        self.assertEqual(scorecard.program_percentage_parks_recreation_fitness, 0.002)
        self.assertEqual(scorecard.program_percentage_agriculture, 0.0394)
        self.assertEqual(scorecard.program_percentage_security_law_enforcement, 0.0572)
        self.assertEqual(scorecard.program_percentage_computer, 0.0592)
        self.assertEqual(scorecard.program_percentage_precision_production, 0.0)
        self.assertEqual(scorecard.program_percentage_humanities, 0.0473)
        self.assertEqual(scorecard.program_percentage_library, 0.0)
        self.assertEqual(scorecard.program_percentage_psychology, 0.0631)
        self.assertEqual(scorecard.program_percentage_social_science, 0.0355)
        self.assertEqual(scorecard.program_percentage_legal, 0.0)
        self.assertEqual(scorecard.program_percentage_english, 0.0158)
        self.assertEqual(scorecard.program_percentage_construction, 0.0)
        self.assertEqual(scorecard.program_percentage_military, 0.0)
        self.assertEqual(scorecard.program_percentage_communication, 0.0)
        self.assertEqual(scorecard.program_percentage_public_administration_social_service, 0.0493)
        self.assertEqual(scorecard.program_percentage_architecture, 0.0039)
        self.assertEqual(scorecard.program_percentage_ethnic_cultural_gender, 0.0)
        self.assertEqual(scorecard.program_percentage_resources, 0.0237)
        self.assertEqual(scorecard.program_percentage_health, 0.0)
        self.assertEqual(scorecard.program_percentage_engineering, 0.1183)
        self.assertEqual(scorecard.program_percentage_history, 0.0)
        self.assertEqual(scorecard.program_percentage_theology_religious_vocation, 0.0)
        self.assertEqual(scorecard.program_percentage_transportation, 0.0)
        self.assertEqual(scorecard.program_percentage_physical_science, 0.0355)
        self.assertEqual(scorecard.program_percentage_science_technology, 0.0)
        self.assertEqual(scorecard.program_percentage_biological, 0.0927)
        self.assertEqual(scorecard.program_percentage_family_consumer_science, 0.0394)
        self.assertEqual(scorecard.program_percentage_philosophy_religious, 0.0)
        self.assertEqual(scorecard.program_percentage_personal_culinary, 0.0)
        self.assertEqual(scorecard.program_percentage_multidiscipline, 0.0)
        self.assertEqual(scorecard.program_percentage_mechanic_repair_technology, 0.0)
        self.assertIsNotNone(scorecard.created)
        self.assertIsNotNone(scorecard.updated)

    def test_create_field_of_study(self):
        college = College.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")
        field_of_study = FieldOfStudy.objects.create(
            college=college,
            cip_code="1313",
            cip_title="Teacher Education and Professional Development, Specific Subject Areas.",
            credential_level="Bachelor’s Degree",
            credential_title="Bachelors Degree",
            num_students_debt=46,
            median_debt=31505,
            monthly_debt_payment=327,
            mean_debt=33085,
            num_students_titleiv=32,
            num_students_earnings=25400,
            median_earnings=25400,
            num_students_ipeds_awards1=24,
            num_students_ipeds_awards2=33
        )
        self.assertEqual(field_of_study.college, college)
        self.assertEqual(field_of_study.cip_code, "1313")
        self.assertEqual(field_of_study.cip_title, "Teacher Education and Professional Development, Specific Subject Areas.")
        self.assertEqual(field_of_study.credential_level, "Bachelor’s Degree")
        self.assertEqual(field_of_study.credential_title, "Bachelors Degree")
        self.assertEqual(field_of_study.num_students_debt, 46)
        self.assertEqual(field_of_study.median_debt, 31505)
        self.assertEqual(field_of_study.monthly_debt_payment, 327)
        self.assertEqual(field_of_study.mean_debt, 33085)
        self.assertEqual(field_of_study.num_students_titleiv, 32)
        self.assertEqual(field_of_study.num_students_earnings,  25400)
        self.assertEqual(field_of_study.median_earnings, 25400)
        self.assertEqual(field_of_study.num_students_ipeds_awards1, 24)
        self.assertEqual(field_of_study.num_students_ipeds_awards2, 33)
        self.assertIsNotNone(college.created)
        self.assertIsNotNone(college.updated)

    def test_create_college_status(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        college = College.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")

        college_status = CollegeStatus.objects.create(
            user=user,
            college=college,
            status="interested",
            net_price=25000,
            award_uploaded=True,
            award_reviewed=False,
            user_notified=False,
            residency="NY",
            in_state_tuition="NY")

        self.assertEqual(college_status.user, user)
        self.assertEqual(college_status.college, college)
        self.assertEqual(college_status.status, "interested")
        self.assertEqual(college_status.net_price, 25000)
        self.assertEqual(college_status.award_uploaded, True)
        self.assertEqual(college_status.award_reviewed, False)
        self.assertEqual(college_status.user_notified, False)
        self.assertEqual(college_status.residency, "NY")
        self.assertEqual(college_status.in_state_tuition, "NY")
        self.assertIsNotNone(college_status.created)
        self.assertIsNotNone(college_status.updated)

        # test user college_status_set
        self.assertEqual(user.collegestatus_set.get_queryset()[1], college_status)

    def test_create_budget(self):
        college_status = CollegeStatus.objects.get(user__email="demouser@tiltaccess.com")

        college_budget = Budget.objects.create(
            college_status=college_status,
            work_study=10000,
            job=10000,
            savings=10000,
            family=10000,
            other_scholarships=10000,
            loan_subsidized=10000,
            loan_unsubsidized=10000,
            loan_plus=10000,
            loan_private=10000,
            loan_school=10000
        )
        self.assertEqual(college_budget.college_status, college_status)
        self.assertEqual(college_budget.work_study, 10000)
        self.assertEqual(college_budget.job, 10000)
        self.assertEqual(college_budget.savings, 10000)
        self.assertEqual(college_budget.family, 10000)
        self.assertEqual(college_budget.other_scholarships, 10000)
        self.assertEqual(college_budget.loan_subsidized, 10000)
        self.assertEqual(college_budget.loan_unsubsidized, 10000)
        self.assertEqual(college_budget.loan_plus, 10000)
        self.assertEqual(college_budget.loan_private, 10000)
        self.assertEqual(college_budget.loan_school, 10000)
        self.assertIsNotNone(college_budget.created)
        self.assertIsNotNone(college_budget.updated)

        # test user budget_set
        self.assertEqual(college_status.budget_set.get_queryset()[0], college_budget)
