from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import DocumentResult, DocumentData, Category, Data, Summary
from colleges.models import College, Status
User = get_user_model()

class ScholarshipTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email="demouser@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo",
            last_name="Testuser")

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
            types=["university", "point_of_interest", "establishment"])

        status = Status.objects.create(
            user=user,
            college=college,
            status="interested",
            net_price=25000,
            award_uploaded=True,
            award_reviewed=False,
            user_notified=False,
            residency="NY",
            in_state_tuition="NY")

        net_total = Category.objects.create(
            name="net price after grants and loans",
            main_category="net price",
            sub_category="scholarships",
            sub_sub_category="loans",
            year= 2021)

    def test_create_document_result(self):
        passed_document_result = DocumentResult.objects.create(
            name="id_2_file_1.pdf",
            words_id="b8e7cc3080ee5840ce0a532abf44b59d3c1c90dc41b64ebb4eee634f5c341780",
            tables_id="90032220e57ad0b3ce89fe27956724bde54f5dc3f1d6dd3f7c9d29167d308ae3",
            sent=True,
            processed=True,
            pass_fail="Passed",
            number_of_missing=None,
            missing_amounts=[None])

        failed_document_result = DocumentResult.objects.create(
            name="id_3_file_1.pdf",
            words_id="702badb7870e8ff50327b67ff1f9d93d6914d2a38030afd7d5c50d2fb07f85c1",
            tables_id="8c71e41aedab71d48eac733032df87e6b940e08ff877456876899da718340ed4",
            sent=True,
            processed=True,
            pass_fail="Failed",
            number_of_missing=5,
            missing_amounts=["$13,190", "$12,090", "$11,245", "$6,345", "$400"])

        # passed document_result
        self.assertEqual(passed_document_result.name, "id_2_file_1.pdf")
        self.assertEqual(passed_document_result.words_id, "b8e7cc3080ee5840ce0a532abf44b59d3c1c90dc41b64ebb4eee634f5c341780")
        self.assertEqual(passed_document_result.tables_id, "90032220e57ad0b3ce89fe27956724bde54f5dc3f1d6dd3f7c9d29167d308ae3")
        self.assertEqual(passed_document_result.sent, True)
        self.assertEqual(passed_document_result.processed, True)
        self.assertEqual(passed_document_result.pass_fail, "Passed")
        self.assertEqual(passed_document_result.number_of_missing, None)
        self.assertEqual(passed_document_result.missing_amounts, [None])
        self.assertIsNotNone(passed_document_result.created)
        self.assertIsNotNone(passed_document_result.updated)

        # failed document_result
        self.assertEqual(failed_document_result.name, "id_3_file_1.pdf")
        self.assertEqual(failed_document_result.words_id, "702badb7870e8ff50327b67ff1f9d93d6914d2a38030afd7d5c50d2fb07f85c1")
        self.assertEqual(failed_document_result.tables_id, "8c71e41aedab71d48eac733032df87e6b940e08ff877456876899da718340ed4")
        self.assertEqual(failed_document_result.sent, True)
        self.assertEqual(failed_document_result.processed, True)
        self.assertEqual(failed_document_result.pass_fail, "Failed")
        self.assertEqual(failed_document_result.number_of_missing, 5)
        self.assertEqual(failed_document_result.missing_amounts, ["$13,190", "$12,090", "$11,245", "$6,345", "$400"])
        self.assertIsNotNone(failed_document_result.created)
        self.assertIsNotNone(failed_document_result.updated)

    def test_create_document_data(self):
        document_data = DocumentData.objects.create(
            name="id_2_file_1.pdf",
            words=["Loyola",
                "Marymount",
                "University",
                "January 27,2020",
                "Dear Aaryanna,",
                "Congratulations on your admission to Loyola Marymount University (LMU)! I am delighted to welcome you as a member",
                "of the Class of 2024. By considering LMU, you have already taken the first step toward an extraordinary next chapter of",
                "your life; we look forward to joining you on this journey."],
            tables='''
Table: Table_1

"YOUR 2020-2021 ESTIMATED COST OF ATTENDANCE","","",
"Your direct costs represent those items that are charged directly by","Tuition and Fees","$52,553",
"Loyola Marymount University, such as tuition, fees, and room and","Room and Board","$15,550",
"board (if you choose to live on campus). Indirect costs are other education-related expenses, such as books and personal expenses,","LMU Direct Costs","$68,103",
"which may vary based on your needs.","Estimated Books and Supplies","$1,080",
"","Estimated Personal Expenses","$3,003",
"","Estimated Total COA","$72,186",
"ESTIMATED REMAINING COST OF ATTENDANCE","","",
"Your remaining net cost is the amount for which you are responsible. This is determined by subtracting all of your grant and scholarship awards from your estimated total cost of attendance.","Estimated Net Cost","$42,841",
"YOUR ELIGIBILITY FOR STUDENT LOANS","","",
"A portion of your net cost can be funded through federal or institutional loan programs. You may also visit the Financial Aid Office online to explore other options.","Federal Direct Subsidized Loan Federal Direct Unsubsidized Loan LMU Burns Student Loan","$3,500 $2,000 $2,000",
"","Total Student Loans","$7,500",
"ESTIMATED REMAINING COST AFTER FINANCIAL AID","","",
"Your remaining costs can be funded using a variety of sources, including personal savings, private loans, part-time employment, or Federal Parent PLUS Loans (if you are a dependent student).","Remaining Cost","$35,341",
"ADDITIONAL SOURCES OF AID","","",
"You have the opportunity to obtain employment on campus and earn up to the amount indicated. If you are a dependent student, your parent(s) may apply for a Federal Parent PLUS Loan up to the remaining cost listed above, subject to credit approval, but we recommend borrowing no more than is necessary to cover your direct costs.","Federal College Work Study","$3,200",

Table: Table_2

"LMU Grant","$14,200",
"LMU Achievement Award","$6,000",
"LMU Early Action Award","$2,000",
"Federal Pell Grant","$6,145",
"Federal SEOG Grant","$1,000",
"Total Grants and Scholarships","$29,345",
''')

        # passed document_result
        self.assertEqual(document_data.name, "id_2_file_1.pdf")
        self.assertEqual(document_data.words, ["Loyola",
                "Marymount",
                "University",
                "January 27,2020",
                "Dear Aaryanna,",
                "Congratulations on your admission to Loyola Marymount University (LMU)! I am delighted to welcome you as a member",
                "of the Class of 2024. By considering LMU, you have already taken the first step toward an extraordinary next chapter of",
                "your life; we look forward to joining you on this journey."])
        self.assertEqual(document_data.tables, '''
Table: Table_1

"YOUR 2020-2021 ESTIMATED COST OF ATTENDANCE","","",
"Your direct costs represent those items that are charged directly by","Tuition and Fees","$52,553",
"Loyola Marymount University, such as tuition, fees, and room and","Room and Board","$15,550",
"board (if you choose to live on campus). Indirect costs are other education-related expenses, such as books and personal expenses,","LMU Direct Costs","$68,103",
"which may vary based on your needs.","Estimated Books and Supplies","$1,080",
"","Estimated Personal Expenses","$3,003",
"","Estimated Total COA","$72,186",
"ESTIMATED REMAINING COST OF ATTENDANCE","","",
"Your remaining net cost is the amount for which you are responsible. This is determined by subtracting all of your grant and scholarship awards from your estimated total cost of attendance.","Estimated Net Cost","$42,841",
"YOUR ELIGIBILITY FOR STUDENT LOANS","","",
"A portion of your net cost can be funded through federal or institutional loan programs. You may also visit the Financial Aid Office online to explore other options.","Federal Direct Subsidized Loan Federal Direct Unsubsidized Loan LMU Burns Student Loan","$3,500 $2,000 $2,000",
"","Total Student Loans","$7,500",
"ESTIMATED REMAINING COST AFTER FINANCIAL AID","","",
"Your remaining costs can be funded using a variety of sources, including personal savings, private loans, part-time employment, or Federal Parent PLUS Loans (if you are a dependent student).","Remaining Cost","$35,341",
"ADDITIONAL SOURCES OF AID","","",
"You have the opportunity to obtain employment on campus and earn up to the amount indicated. If you are a dependent student, your parent(s) may apply for a Federal Parent PLUS Loan up to the remaining cost listed above, subject to credit approval, but we recommend borrowing no more than is necessary to cover your direct costs.","Federal College Work Study","$3,200",

Table: Table_2

"LMU Grant","$14,200",
"LMU Achievement Award","$6,000",
"LMU Early Action Award","$2,000",
"Federal Pell Grant","$6,145",
"Federal SEOG Grant","$1,000",
"Total Grants and Scholarships","$29,345",
''')
        self.assertIsNotNone(document_data.created)
        self.assertIsNotNone(document_data.updated)

    def test_create_category(self):
        tuition = Category.objects.create(
            name="tuition",
            main_category= "cost",
            sub_category="direct",
            sub_sub_category=None,
            year= 2021)

        pell = Category.objects.create(
            name="pell",
            main_category="aid",
            sub_category="grant",
            sub_sub_category="federal",
            year= 2021)

        net_total = Category.objects.create(
            name="net price after grants and loans",
            main_category="net price",
            sub_category="scholarships",
            sub_sub_category="loans",
            year= 2021)

        # tuition
        self.assertEqual(tuition.name, "tuition")
        self.assertEqual(tuition.main_category, "cost")
        self.assertEqual(tuition.sub_category, "direct")
        self.assertEqual(tuition.sub_sub_category, None)
        self.assertEqual(tuition.year, 2021)
        self.assertIsNotNone(tuition.created)
        self.assertIsNotNone(tuition.updated)

        # pell
        self.assertEqual(pell.name, "pell")
        self.assertEqual(pell.main_category, "aid")
        self.assertEqual(pell.sub_category, "grant")
        self.assertEqual(pell.sub_sub_category, "federal")
        self.assertEqual(pell.year, 2021)
        self.assertIsNotNone(pell.created)
        self.assertIsNotNone(pell.updated)

        # net_total
        self.assertEqual(net_total.name, "net price after grants and loans")
        self.assertEqual(net_total.main_category, "net price")
        self.assertEqual(net_total.sub_category, "scholarships")
        self.assertEqual(net_total.sub_sub_category, "loans")
        self.assertEqual(net_total.year, 2021)
        self.assertIsNotNone(net_total.created)
        self.assertIsNotNone(net_total.updated)

    def test_create_data(self):
        college_status = Status.objects.get(status="interested")
        net_total = Category.objects.get(name="net price after grants and loans")

        data_1 = Data.objects.create(
            name="Direct Subsidized Staffrd Loan",
            amount=3500,
            table_number= 1,
            row_index= 3,
            col_index= 2,
            row_data = ["Direct Subsidized Staffrd Loan", "$1,750", "$3,500", "STAF"],
            status=college_status,
            category=net_total)

        self.assertEqual(data_1.name, "Direct Subsidized Staffrd Loan")
        self.assertEqual(data_1.amount, 3500)
        self.assertEqual(data_1.table_number, 1)
        self.assertEqual(data_1.row_index, 3)
        self.assertEqual(data_1.col_index, 2)
        self.assertEqual(data_1.row_data,["Direct Subsidized Staffrd Loan", "$1,750", "$3,500", "STAF"])
        self.assertEqual(data_1.status, college_status)
        self.assertEqual(data_1.category, net_total)
        self.assertIsNotNone(data_1.created)
        self.assertIsNotNone(data_1.updated)

        # test college_status data_set
        self.assertEqual(college_status.data_set.get_queryset()[0], data_1)

    def test_create_summary(self):
        college_status = Status.objects.get(status="interested")

        summary = Summary.objects.create(
            status=college_status,
            total_cost=50000,
            total_aid=30000,
            net_price= 20000)

        self.assertEqual(summary.status, college_status)
        self.assertEqual(summary.total_cost, 50000)
        self.assertEqual(summary.total_aid, 30000)
        self.assertEqual(summary.net_price, 20000)
        self.assertIsNotNone(summary.created)
        self.assertIsNotNone(summary.updated)

        # test college_status summary_set
        self.assertEqual(college_status.summary_set.get_queryset()[0], summary)
