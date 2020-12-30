from financial_aid.models import AidCategory, AidData, DocumentData, DocumentResult, AidSummary
from colleges.models import College, CollegeStatus
from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()

class AidTests(TestCase):

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
            photos=[
                "https://lh3.googleusercontent.com/places/ABKp1IqGVoROLCDDU3dwiyAzaDk4Ky6buHubwqLCNODTriSPwPVyYARWxVsQiqDqzrPt_ZvWzKc-rCrIWaNWRGrk4olZE5N1mwO-gug=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IqVV9NSRdkeVV4eDiGEySagrugrK2ryXcrzpzGN-IzNftQ37xqUx7OQcgUkjnsd32cPDQcfsO1RAbgfredazdmk9zyeZTuuutQ=s1600-w2560",
                "https://lh3.googleusercontent.com/places/ABKp1IqlYDobf55GX0Y6pPVnISOO6ZBfsCtM9Z_1_AL8VakFdHnoAcjU1cYT83Lzdoh-FjH0cBF43U_cCzSfjp28SwI1CjKXyYtTbEM=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IoWIutn-aNT33reyZv9QmvmHrSJ4V_BoC8paCJeEfXeOZcfKi3ZFgbRagHKxQhQOiNXJOI2bZLtMy9iWT8CxUWJk2L2ZHaRpdg=s1600-w1536",
                "https://lh3.googleusercontent.com/places/ABKp1IotKWni5j2Ac5ZZANdOqpmVagiwnvzO7mQy1C-KNURivHWF6Ui6SllbzTp8AOdiReqiFXZOJvscLVDSCgwqr6APEVDz7zUTguI=s1600-w3264",
                "https://lh3.googleusercontent.com/places/ABKp1IqRn6d9T0Dw2vsaP2b08DNLXrWUUz9VjuUTPOnPY7T1pzjFG4CjdsqZgrENLVya3zSBxGyjUdjjJFX5GesV3MA7nEbijf8DAfs=s1600-w1695",
                "https://lh3.googleusercontent.com/places/ABKp1IqBUtkqITPk0zKctRz6dwgWema8bvUjZGO-E3rtzRwBrvle-GIUvgRDeSMUwX8tJdG1fLLydYJ2bJuEFYNMjna9O0zk3GhsPfo=s1600-w6016",
                "https://lh3.googleusercontent.com/places/ABKp1IqvT48dPKMA5OsHpBdLElYVgGb_HDFoTXPqo_cM_mVCHFLvPWvjphwVSCbHw3tZdeQi5O67HT0-peLQiTOg29WYfHOVIuLEjVM=s1600-w4032",
                "https://lh3.googleusercontent.com/places/ABKp1IoPkQjJ1uvn9JvjougnKvWlUppDe6OZis_7rRSX2Z0EBfdRXN0iLu9B8WYAvnBke-wckEOY_V5xUnJs-FLm_8Gvo3fse54_Rag=s1600-w2048",
                "https://lh3.googleusercontent.com/places/ABKp1IpvJcp40b6PKpaNfkgc9jJu6NN8nneLkfSropV-N1DZmuNJBoAD3a9FM5grPGv9Qw_hw-PVDETm47ywkggYztJagMm44pxqNS0=s1600-w2048"
            ],
            types=["university", "point_of_interest", "establishment"]
        )

        college_status = CollegeStatus.objects.create(
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
        aid_category = AidCategory.objects.create(
            name="pell",
            primary="aid",
            secondary="grant",
            tertiary="federal"
        )
        AidData.objects.create(
            college_status=college_status,
            aid_category=aid_category,
            name="Pell Grant",
            amount=2000,
            row_text = "Pell Grant, $1,000, $1,000, $2,000",
            table=2,
            row_index=2,
            col_index=3
        )

    def test_create_aid_category(self):
        aid_category = AidCategory.objects.create(
            name="tuition",
            primary="cost",
            secondary="direct",
            tertiary=""
        )

        self.assertEqual(aid_category.name, "tuition")
        self.assertEqual(aid_category.primary, "cost")
        self.assertEqual(aid_category.secondary, "direct")
        self.assertEqual(aid_category.tertiary, "")
        self.assertIsNotNone(aid_category.created)
        self.assertIsNotNone(aid_category.updated)

    def test_create_aid_data(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        college_status = CollegeStatus.objects.get(user=user)
        aid_category = AidCategory.objects.get(name="pell")
        aid_data = AidData.objects.create(
            college_status=college_status,
            aid_category=aid_category,
            name="Pell Grant",
            amount=4000,
            row_text ="Pell Grant, $2,000, $2,000, $4,000",
            table=2,
            row_index=2,
            col_index=3
        )

        self.assertEqual(aid_data.college_status, college_status)
        self.assertEqual(aid_data.aid_category, aid_category)
        self.assertEqual(aid_data.name, "Pell Grant")
        self.assertEqual(aid_data.amount, 4000)
        self.assertEqual(aid_data.row_text, "Pell Grant, $2,000, $2,000, $4,000")
        self.assertEqual(aid_data.table, 2)
        self.assertEqual(aid_data.row_index, 2)
        self.assertEqual(aid_data.col_index, 3)
        self.assertIsNotNone(aid_data.created)
        self.assertIsNotNone(aid_data.updated)
        self.assertEqual(college_status.aiddata_set.get_queryset()[1], aid_data)

    def test_create_aid_summary(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        college_status = CollegeStatus.objects.get(user=user)
        aid_summary = AidSummary.objects.create(
            college_status=college_status,
            total_cost=25000,
            total_aid=12500,
            net_price=12500,
        )

        self.assertEqual(aid_summary.college_status, college_status)
        self.assertEqual(aid_summary.total_cost, 25000)
        self.assertEqual(aid_summary.total_aid, 12500)
        self.assertEqual(aid_summary.net_price, 12500)
        self.assertIsNotNone(aid_summary.created)
        self.assertIsNotNone(aid_summary.updated)
        self.assertEqual(college_status.aidsummary_set.get_queryset()[0], aid_summary)
