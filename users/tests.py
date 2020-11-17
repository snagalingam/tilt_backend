from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from organizations.models import Organization
from users.models import DeletedAccount, Action
from services.helpers.actions import create_action, create_timestamp, create_date
User = get_user_model()

class CustomUserTests(TestCase):

    def setUp(self):
        # create superuser
        User.objects.create_superuser(
            email="admin@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Admin",
            last_name="Testuser"
        )
        # create user
        User.objects.create_user(
            email="demouser@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo",
            last_name="Testuser"
        )
        User.objects.create_user(
            email="demouser1@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo1",
            last_name="Testuser"
        )
        User.objects.create_user(
            email="demouser2@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo2",
            last_name="Testuser"
        )
        User.objects.create_user(
            email="demouser3@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Demo3",
            last_name="Testuser"
        )
        # create organization
        Organization.objects.create(
            place_id="ChIJ91htBQIXYogRtPsg4NGoNv0",
            business_status="OPERATIONAL",
            icon=None,
            name="Alabama A&M University",
            lat=34.7827196,
            lng=-86.568614,
            address="Huntsville, AL 35811, USA",
            phone_number="(256) 372-5000",
            url="https://maps.google.com/?cid=18245956559700032436",
            website="http://www.aamu.edu/",
            types=["school", "point_of_interest", "establishment"],
            tilt_partnership=False,
        )

    def test_create_superuser(self):
        superuser = User.objects.get(email="admin@tiltaccess.com")
        
        self.assertEqual(superuser.email, "admin@tiltaccess.com")
        self.assertEqual(superuser.first_name, "Admin")
        self.assertEqual(superuser.last_name, "Testuser")
        self.assertTrue(superuser.check_password("gWzupKiX5c"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertFalse(superuser.is_verified)
        self.assertFalse(superuser.is_onboarded)
        self.assertTrue(superuser.is_active)
        self.assertIsNotNone(superuser.date_joined)

    def test_create_user(self):
        user = User.objects.get(email="demouser@tiltaccess.com")

        self.assertEqual(user.email, "demouser@tiltaccess.com")
        self.assertEqual(user.first_name, "Demo")
        self.assertEqual(user.last_name, "Testuser")
        self.assertTrue(user.check_password("gWzupKiX5c"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)
        self.assertFalse(user.is_onboarded)
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.date_joined)

    def test_login_users(self):
        c = Client()
        superuser = User.objects.get(email="admin@tiltaccess.com")
        user = User.objects.get(email="demouser@tiltaccess.com")
        
        login_superuser = c.login(
            username="admin@tiltaccess.com", 
            password="gWzupKiX5c")
        login_superuser = c.login(
            username="demouser@tiltaccess.com", 
            password="gWzupKiX5c")
        
        self.assertTrue(login_superuser)
        self.assertTrue(login_superuser)

    def test_logout_users(self):
        c = Client()
        superuser = User.objects.get(email="admin@tiltaccess.com")
        user = User.objects.get(email="demouser@tiltaccess.com")

        login_superuser = c.login(
            username="admin@tiltaccess.com", 
            password="gWzupKiX5c")
        login_superuser = c.login(
            username="demouser@tiltaccess.com", 
            password="gWzupKiX5c")

        logout_superuser = c.login(
            username="admin@tiltaccess.com", 
            password="gWzupKiX5c")
        logout_superuser = c.login(
            username="demouser@tiltaccess.com", 
            password="gWzupKiX5c")
        
        self.assertTrue(logout_superuser)
        self.assertTrue(logout_superuser)

    def test_onboard_user(self):
        organization = Organization.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")
        onboard_user = User.objects.get(email="demouser@tiltaccess.com")

        onboard_user.preferred_name = "Preferred"
        onboard_user.gpa = 4.0
        onboard_user.act_score = 35
        onboard_user.sat_score = 1600
        onboard_user.efc = 1
        onboard_user.pronouns = "He/his"
        onboard_user.ethnicity = ["asian"]
        onboard_user.user_type = "student"
        onboard_user.high_school_grad_year = 2020
        onboard_user.income_quintile = "lo"
        onboard_user.found_from = ["instagram"]
        onboard_user.is_onboarded = True
        onboard_user.organization.add(organization)
        onboard_user.save()

        self.assertEqual(onboard_user.preferred_name, "Preferred")
        self.assertEqual(onboard_user.gpa, 4.0)
        self.assertEqual(onboard_user.act_score, 35)
        self.assertEqual(onboard_user.sat_score, 1600)
        self.assertEqual(onboard_user.efc, 1)
        self.assertEqual(onboard_user.pronouns, "He/his")
        self.assertEqual(onboard_user.ethnicity, ["asian"])
        self.assertEqual(onboard_user.user_type, "student")
        self.assertEqual(onboard_user.high_school_grad_year, 2020)
        self.assertEqual(onboard_user.income_quintile, "lo")
        self.assertEqual(onboard_user.found_from, ["instagram"])
        self.assertEqual(onboard_user.organization.get_queryset()[0], organization)
        self.assertTrue(onboard_user.is_onboarded)

    def test_deleted_accounts(self):
        organization = Organization.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")
        superuser = User.objects.get(email="admin@tiltaccess.com")
        user = User.objects.get(email="demouser@tiltaccess.com")
        onboard_user1 = User.objects.get(email="demouser1@tiltaccess.com")
        onboard_user2 = User.objects.get(email="demouser2@tiltaccess.com")
        onboard_user3 = User.objects.get(email="demouser3@tiltaccess.com")

        onboard_user1.preferred_name = "Preferred"
        onboard_user1.gpa = 4.0
        onboard_user1.act_score = 35
        onboard_user1.sat_score = 1600
        onboard_user1.efc = 1
        onboard_user1.pronouns = "He/his"
        onboard_user1.ethnicity = ["asian"]
        onboard_user1.user_type = "student"
        onboard_user1.high_school_grad_year = 2020
        onboard_user1.income_quintile = "lo"
        onboard_user1.found_from = ["instagram"]
        onboard_user1.is_onboarded = True
        onboard_user1.organization.add(organization)
        onboard_user1.save()

        self.assertEqual(User.objects.filter(is_onboarded=True).count(), 1)

        onboard_user2.preferred_name = "Preferred"
        onboard_user2.gpa = 4.0
        onboard_user2.act_score = 35
        onboard_user2.sat_score = 1600
        onboard_user2.efc = 1
        onboard_user2.pronouns = "He/his"
        onboard_user2.ethnicity = ["asian"]
        onboard_user2.user_type = "student"
        onboard_user2.high_school_grad_year = 2020
        onboard_user2.income_quintile = "lo"
        onboard_user2.found_from = ["instagram"]
        onboard_user2.is_onboarded = True
        onboard_user2.organization.add(organization)
        onboard_user2.save()

        self.assertEqual(User.objects.filter(is_onboarded=True).count(), 2)
  
        onboard_user3.preferred_name = "Preferred"
        onboard_user3.gpa = 4.0
        onboard_user3.act_score = 35
        onboard_user3.sat_score = 1600
        onboard_user3.efc = 1
        onboard_user3.pronouns = "He/his"
        onboard_user3.ethnicity = ["asian"]
        onboard_user3.user_type = "student"
        onboard_user3.high_school_grad_year = 2020
        onboard_user3.income_quintile = "lo"
        onboard_user3.found_from = ["instagram"]
        onboard_user3.is_onboarded = True
        onboard_user3.organization.add(organization)
        onboard_user3.save()

        self.assertEqual(User.objects.filter(is_onboarded=True).count(), 3)

        superuser.delete()
        date = create_date()
        get_count = DeletedAccount.objects.create(
            date=date,
            accounts=1
        )
        self.assertEqual(get_count.accounts, 1)
        self.assertEqual(User.objects.all().count(), 4)

        user.delete()
        get_count.accounts += 1
        onboard_user1.delete()
        get_count.accounts += 1
        onboard_user2.delete()
        get_count.accounts += 1
        onboard_user3.delete()
        get_count.accounts += 1

        self.assertEqual(get_count.accounts, 5)
        self.assertEqual(User.objects.all().count(), 0)


    def test_create_action(self):
        timestamp = create_timestamp()
        user = User.objects.get(email="demouser@tiltaccess.com")

        action = Action.objects.create(
            user=user, 
            description="Testing Actions", 
            timestamp=timestamp)

        self.assertEqual(action.user, user)
        self.assertEqual(action.description, "Testing Actions")
        self.assertEqual(action.timestamp, timestamp)

