from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Scholarship, Provider, ScholarshipStatus
from colleges.models import College
User = get_user_model()

class ScholarshipTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email="demouser@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo",
            last_name="Testuser"
        )

        Provider.objects.create(
            organization="Tilt",
            reference="Tilt Scholarship Committee",
            address= "65 Pine Ave Suite 103",
            city= "Long Beach",
            state= "CA",
            zipcode= "90802",
            email= "scholarships@tiltaccess.com",
            phone_number= "224-306-9466",
            phone_number_ext= 'x1004'
        )

        Provider.objects.create(
            organization="Strouthion",
            reference="Strouthion Scholarship Committee",
            address= "172 Madison Ave",
            city= "New York",
            state= "NY",
            zipcode= "10016",
            email= "scholarships@strouthion.com",
            phone_number= "212-719-2141",
            phone_number_ext= "x1004"
        )

        provider = Provider.objects.create(
            organization="Provider",
            reference="Provider Scholarship Committee",
            address= "100 Provider Lane Suite 555",
            city= "Kansas City",
            state= "MO",
            zipcode= "64030",
            email= "scholarships@fakeprovider.com",
            phone_number= "816-555-4321",
            phone_number_ext= 'x4'
        )

        # create college
        College.objects.create(
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

        Scholarship.objects.create(
            name="Provider Scholarship",
            provider=provider,
            description="Money for students who like barbeque.",
            website="https://fakeprovider.com/bbqscholarship",
            deadline= datetime.date.today(),
            date_added=timezone.now(),
            max_amount=100_000,
            renewable=True,
            number_awards=1,
            education_level=["Highschool Seniors", "Highschool Juniors"],
            education_requirements="Only for highschool seniors and juniors.",
            area_of_study=["Culinary Arts"],
            area_of_study_description="Areas of culinary arts.",
            writing_competition=True,
            interest_description="Smoked Meats",
            association_requirement=["Provider"],
            location="Great Plains",
            state="MO",
            ethnicity=["All"],
            gender="",
            min_gpa=3.0,
            max_gpa=4.0,
            min_act=30,
            min_sat=1500,
            disability="None",
            military="None",
            citizenship=["USA", "Canada", "Mexico"],
            first_generation=False,
            financial_need=True
        )

    def test_create_scholarship(self):
        tilt = Provider.objects.get(organization="Tilt")
        strouthion = Provider.objects.get(organization="Strouthion")
        college = College.objects.get(name="Alabama A&M University")

        t_scholarship = Scholarship.objects.create(
            name="Tilt Scholarship",
            provider=tilt,
            description="Money for students who like purple.",
            website="https://tiltaccess.com/purplescholarship",
            deadline= datetime.date.today(),
            date_added=timezone.now(),
            max_amount=1_000_000,
            renewable=True,
            number_awards=1,
            education_level=["Highschool Seniors", "Highschool Juniors"],
            education_requirements="Only for highschool seniors and juniors.",
            area_of_study=["Finance"],
            area_of_study_description="Areas of financial education and bubble tea enthusiasts.",
            writing_competition=True,
            interest_description="Bubble Tea",
            association_requirement=["Tilt"],
            location="Southern California",
            state="CA",
            ethnicity=["All"],
            gender="Female",
            min_gpa=3.0,
            max_gpa=4.0,
            min_act=30,
            min_sat=1500,
            disability="None",
            military="None",
            citizenship=["USA", "Canada", "Mexico"],
            first_generation=False,
            financial_need=True)

        s_scholarship = Scholarship.objects.create(
            name="Strouthion Scholarship",
            provider=strouthion,
            description="Money for students who like sparrows.",
            website="https://strouthion.com/sparrowscholarship",
            deadline= datetime.date.today(),
            date_added=timezone.now(),
            max_amount=1_000_000,
            renewable=False,
            number_awards=2,
            education_level=["Highschool Seniors", "Highschool Juniors"],
            education_requirements="Only for highschool seniors and juniors.",
            area_of_study=["Ornithology"],
            area_of_study_description="Areas of sparrow research.",
            writing_competition=False,
            interest_description="Birdwatching",
            association_requirement=["Strouthion"],
            location="New York City",
            state="NY",
            ethnicity=["All"],
            gender="All",
            min_gpa=2.0,
            max_gpa=4.0,
            min_act=25,
            min_sat=1250,
            disability="None",
            military="None",
            citizenship=["USA", "Canada"],
            first_generation=False,
            financial_need=True)

        t_scholarship.college.add(college)
        s_scholarship.college.add(college)

        # tilt_scholoarship
        self.assertEqual(t_scholarship.name, "Tilt Scholarship")
        self.assertEqual(t_scholarship.provider, tilt)
        self.assertEqual(t_scholarship.description, "Money for students who like purple.")
        self.assertEqual(t_scholarship.website, "https://tiltaccess.com/purplescholarship")
        self.assertIsInstance(t_scholarship.deadline, datetime.date)
        self.assertIsInstance(s_scholarship.date_added, datetime.date)
        self.assertEqual(t_scholarship.max_amount, 1_000_000)
        self.assertEqual(t_scholarship.renewable, True)
        self.assertEqual(t_scholarship.number_awards, 1)
        self.assertEqual(t_scholarship.education_level, ["Highschool Seniors", "Highschool Juniors"])
        self.assertEqual(t_scholarship.education_requirements, "Only for highschool seniors and juniors.")
        self.assertEqual(t_scholarship.area_of_study, ["Finance"])
        self.assertEqual(t_scholarship.area_of_study_description, "Areas of financial education and bubble tea enthusiasts.")
        self.assertEqual(t_scholarship.writing_competition, True)
        self.assertEqual(t_scholarship.interest_description, "Bubble Tea")
        self.assertEqual(t_scholarship.college.get_queryset()[0], college)
        self.assertEqual(t_scholarship.association_requirement, ["Tilt"])
        self.assertEqual(t_scholarship.location, "Southern California")
        self.assertEqual(t_scholarship.state, "CA")
        self.assertEqual(t_scholarship.ethnicity, ["All"])
        self.assertEqual(t_scholarship.gender, "Female")
        self.assertEqual(t_scholarship.min_gpa, 3.0)
        self.assertEqual(t_scholarship.max_gpa, 4.0)
        self.assertEqual(t_scholarship.min_act, 30)
        self.assertEqual(t_scholarship.min_sat, 1500)
        self.assertEqual(t_scholarship.disability, "None")
        self.assertEqual(t_scholarship.military, "None")
        self.assertEqual(t_scholarship.citizenship, ["USA", "Canada", "Mexico"])
        self.assertEqual(t_scholarship.first_generation, False)
        self.assertEqual(t_scholarship.financial_need, True)
        self.assertIsNotNone(t_scholarship.created)
        self.assertIsNotNone(t_scholarship.updated)

        # strouthion_scholoarship
        self.assertEqual(s_scholarship.name, "Strouthion Scholarship")
        self.assertEqual(s_scholarship.provider, strouthion)
        self.assertEqual(s_scholarship.description, "Money for students who like sparrows.")
        self.assertEqual(s_scholarship.website, "https://strouthion.com/sparrowscholarship")
        self.assertIsInstance(s_scholarship.deadline, datetime.date)
        self.assertIsInstance(s_scholarship.date_added, datetime.date)
        self.assertEqual(s_scholarship.max_amount, 1_000_000)
        self.assertEqual(s_scholarship.renewable, False)
        self.assertEqual(s_scholarship.number_awards, 2)
        self.assertEqual(s_scholarship.education_level, ["Highschool Seniors", "Highschool Juniors"])
        self.assertEqual(s_scholarship.education_requirements, "Only for highschool seniors and juniors.")
        self.assertEqual(s_scholarship.area_of_study, ["Ornithology"])
        self.assertEqual(s_scholarship.area_of_study_description, "Areas of sparrow research.")
        self.assertEqual(s_scholarship.writing_competition, False)
        self.assertEqual(s_scholarship.interest_description, "Birdwatching")
        self.assertEqual(s_scholarship.college.get_queryset()[0], college)
        self.assertEqual(s_scholarship.association_requirement, ["Strouthion"])
        self.assertEqual(s_scholarship.location, "New York City")
        self.assertEqual(s_scholarship.state, "NY")
        self.assertEqual(s_scholarship.ethnicity, ["All"])
        self.assertEqual(s_scholarship.gender, "All")
        self.assertEqual(s_scholarship.min_gpa, 2.0)
        self.assertEqual(s_scholarship.max_gpa, 4.0)
        self.assertEqual(s_scholarship.min_act, 25)
        self.assertEqual(s_scholarship.min_sat, 1250)
        self.assertEqual(s_scholarship.disability, "None")
        self.assertEqual(s_scholarship.military, "None")
        self.assertEqual(s_scholarship.citizenship, ["USA", "Canada"])
        self.assertEqual(s_scholarship.first_generation, False)
        self.assertEqual(t_scholarship.financial_need, True)
        self.assertIsNotNone(s_scholarship.created)
        self.assertIsNotNone(s_scholarship.updated)

        # test college scholarship_status_set
        self.assertEqual(college.scholarship_set.get_queryset().filter(
            name="Tilt Scholarship")[0], t_scholarship)
        self.assertEqual(college.scholarship_set.get_queryset().filter(
            name="Strouthion Scholarship")[0], s_scholarship)

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
