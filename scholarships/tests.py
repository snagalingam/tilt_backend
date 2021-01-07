import datetime

from colleges.models import College
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from scholarships.models import (
    Association,
    Citizenship,
    Degree,
    Disability,
    EducationCategory,
    EducationDetail,
    EducationScholarship,
    FieldCategory,
    FieldDetail,
    FieldScholarship,
    Gender,
    Heritage,
    Interest,
    LocationDetail,
    LocationScholarship,
    Military,
    Provider,
    Scholarship,
    ScholarshipStatus,
    State
)


User = get_user_model()

class ScholarshipTests(TestCase):

    def setUp(self):
        # colleges
        college1 = College.objects.create(
            popularity_score=1,
            scorecard_unit_id=100654,
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

        # states - referenced by Providers
        state1 = State.objects.create(name="California", abbreviation="CA")
        state2 = State.objects.create(name="New York", abbreviation="NY")
        state3 = State.objects.create(name="Missouri", abbreviation="MO")

        # providers
        provider1 = Provider.objects.create(
            addressee="Tilt Scholarship Committee",
            city="Long Beach",
            email="scholarships@tiltaccess.com",
            organization="Tilt",
            phone_number="2243069466",
            phone_number_ext="1004",
            state=state1,
            street="65 Pine Ave Suite 103",
            zipcode="90802",
        )
        provider2 = Provider.objects.create(
            addressee="Strouthion Scholarship Committee",
            city="New York",
            email="scholarships@strouthion.com",
            organization="Strouthion",
            phone_number= "2127192141",
            phone_number_ext= "1004",
            state=state2,
            street= "172 Madison Ave",
            zipcode= "10016",
        )
        provider3 = Provider.objects.create(
            addressee="Provider Scholarship Committee",
            city="Kansas City",
            email="scholarships@fakeprovider.com",
            organization="Provider",
            phone_number= "8165554321",
            phone_number_ext= "4",
            state=state3,
            street= "100 Provider Lane Suite 555",
            zipcode= "64030",
        )

        # scholarships
        association1 = Association.objects.create(name="engineering association")
        citizenship1 = Citizenship.objects.create(category="citizen")
        degree1 = Degree.objects.create(category="Bachelor's")
        disability1 = Disability.objects.create(category="handicap")
        education_category1 = EducationCategory.objects.create(category="college student")
        education_detail1 = EducationDetail.objects.create(description="computer science class")
        field_category1 = FieldCategory.objects.create(category="healthcare")
        field_detail1 = FieldDetail.objects.create(description="nurse")
        gender1 = Gender.objects.create(category="man")
        heritage1 = Heritage.objects.create(category="asian")
        interest1 = Interest.objects.create(category="bicycling")
        location_detail1 = LocationDetail.objects.create(description="Great Plains")
        military1 = Military.objects.create(category="active_duty")
        scholarship1 = Scholarship.objects.create(
            name="Provider Scholarship",
            deadline= datetime.date.today(),
            description="Money for students who like barbeque.",
            max_amount=100000,
            number_awards=1,
            provider=provider1,
            renewable=True,
            website="https://fakeprovider.com/bbqscholarship",
            financial_need=True,
            first_generation=False,
            min_act=30,
            min_gpa=3.0,
            min_sat=1500,
            max_gpa=4.0,
            writing=True
        )
        scholarship1.association.add(association1)
        scholarship1.citizenship.add(citizenship1)
        scholarship1.college.add(college1)
        scholarship1.degree.add(degree1)
        scholarship1.disability.add(disability1)
        scholarship1.gender.add(gender1)
        scholarship1.heritage.add(heritage1)
        scholarship1.interest.add(interest1)
        scholarship1.military.add(military1)
        education_scholarship1 = EducationScholarship.objects.create(
            education_category=education_category1,
            education_detail=education_detail1,
            scholarship=scholarship1
        )
        field_scholarship1 = FieldScholarship.objects.create(
            field_category=field_category1,
            field_detail=field_detail1,
            scholarship=scholarship1
        )
        location_scholarship1 = LocationScholarship.objects.create(
            location_detail=location_detail1,
            scholarship=scholarship1,
            state=state3
        )

        # users
        user = User.objects.create_user(
            email="demouser@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo",
            last_name="Testuser"
        )

    def test_create_scholarship(self):
        association = Association.objects.get(name="engineering association")
        citizenship = Citizenship.objects.get(category="citizen")
        college = College.objects.get(name="Alabama A&M University")
        degree = Degree.objects.get(category="Bachelor's")
        disability = Disability.objects.get(category="handicap")
        education_category = EducationCategory.objects.get(category="college student")
        education_detail = EducationDetail.objects.get(description="computer science class")
        field_category = FieldCategory.objects.get(category="healthcare")
        field_detail = FieldDetail.objects.get(description="nurse")
        gender = Gender.objects.get(category="man")
        heritage = Heritage.objects.get(category="asian")
        interest = Interest.objects.get(category="bicycling")
        location_detail = LocationDetail.objects.get(description="Great Plains")
        military = Military.objects.get(category="active_duty")
        provider = Provider.objects.get(organization="Tilt")
        scholarship = Scholarship.objects.get(name="Provider Scholarship")

        self.assertEqual(scholarship.name, "Provider Scholarship")
        self.assertEqual(scholarship.deadline, datetime.date.today())
        self.assertEqual(scholarship.description, "Money for students who like barbeque.")
        self.assertEqual(scholarship.max_amount, 100000)
        self.assertEqual(scholarship.number_awards, 1)
        self.assertEqual(scholarship.provider, provider)
        self.assertEqual(scholarship.renewable, True)
        self.assertEqual(scholarship.association.get_queryset()[0], association)
        self.assertEqual(scholarship.citizenship.get_queryset()[0], citizenship)
        self.assertEqual(scholarship.college.get_queryset()[0], college)
        self.assertEqual(scholarship.degree.get_queryset()[0], degree)
        self.assertEqual(scholarship.disability.get_queryset()[0], disability)
        self.assertEqual(scholarship.financial_need, True)
        self.assertEqual(scholarship.first_generation, False)
        self.assertEqual(scholarship.gender.get_queryset()[0], gender)
        self.assertEqual(scholarship.heritage.get_queryset()[0], heritage)
        self.assertEqual(scholarship.interest.get_queryset()[0], interest)
        self.assertEqual(scholarship.military.get_queryset()[0], military)
        self.assertEqual(scholarship.min_act, 30)
        self.assertEqual(scholarship.min_gpa, 3.0)
        self.assertEqual(scholarship.min_sat, 1500)
        self.assertEqual(scholarship.max_gpa, 4.0)
        self.assertEqual(scholarship.writing, True)
        self.assertIsNotNone(scholarship.created)
        self.assertIsNotNone(scholarship.updated)

        # test college scholarship_status_set
        self.assertEqual(college.scholarship_set.get_queryset().filter(
            name="Provider Scholarship")[0],
            scholarship
        )

    def test_create_scholarship_status(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        scholarship = Scholarship.objects.get(name="Provider Scholarship")
        scholarship_status = ScholarshipStatus.objects.create(
            scholarship=scholarship,
            user=user,
            status="approved"
        )
        self.assertEqual(scholarship_status.user, user)
        self.assertEqual(scholarship_status.scholarship, scholarship)
        self.assertEqual(scholarship_status.status, "approved")
        self.assertIsNotNone(scholarship_status.created)
        self.assertIsNotNone(scholarship_status.updated)

        # test scholarship status_set
        self.assertEqual(user.scholarshipstatus_set.get_queryset()[0], scholarship_status)
