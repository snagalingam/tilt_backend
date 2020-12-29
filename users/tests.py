from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from organizations.models import Organization
from services.helpers.actions import create_action, create_timestamp, create_date
from users.models import Action, DeletedAccount, Ethnicity, EthnicityUser,  Income, Pronoun, PronounUser, Source, SourceUser, UserCategory


User = get_user_model()

class UserTests(TestCase):

    def setUp(self):
        User.objects.create_superuser(
            email="admin@tiltaccess.com",
            password = "gWzupKiX5c",
            first_name="Admin",
            last_name="Testuser"
        )
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
        Organization.objects.create(
            place_id="ChIJ91htBQIXYogRtPsg4NGoNv0",
            business_status="OPERATIONAL",
            icon="",
            name="Alabama A&M University",
            lat=34.7827196,
            lng=-86.568614,
            address="Huntsville, AL 35811, USA",
            phone_number="(256) 372-5000",
            url="https://maps.google.com/?cid=18245956559700032436",
            website="http://www.aamu.edu/",
            types=["school", "point_of_interest", "establishment"],
            partner=False
        )
        Pronoun.objects.create(pronoun="she")
        Source.objects.create(source="instagram")
        UserCategory.objects.create(category="parent")
        Income.objects.create(category="h2", description="$110,000+")
        Ethnicity.objects.create(ethnicity="aian")

    def test_create_superuser(self):
        superuser = User.objects.get(email="admin@tiltaccess.com")

        self.assertEqual(superuser.email, "admin@tiltaccess.com")
        self.assertEqual(superuser.first_name, "Admin")
        self.assertEqual(superuser.last_name, "Testuser")
        self.assertEqual(superuser.check_password("gWzupKiX5c"), True)
        self.assertEqual(superuser.is_superuser, True)
        self.assertEqual(superuser.is_verified, False)
        self.assertEqual(superuser.is_onboarded, False)
        self.assertEqual(superuser.is_test, False)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_active, True)
        self.assertIsNotNone(superuser.created)

    def test_create_user(self):
        user = User.objects.get(email="demouser@tiltaccess.com")

        self.assertEqual(user.email, "demouser@tiltaccess.com")
        self.assertEqual(user.first_name, "Demo")
        self.assertEqual(user.last_name, "Testuser")
        self.assertEqual(user.check_password("gWzupKiX5c"), True)
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_verified, False)
        self.assertEqual(user.is_onboarded, False)
        self.assertEqual(user.is_test, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)
        self.assertIsNotNone(user.created)

    def test_login_users(self):
        client = Client()

        superuser = client.login(
            email="admin@tiltaccess.com",
            password="gWzupKiX5c"
        )
        user = client.login(
            email="demouser@tiltaccess.com",
            password="gWzupKiX5c"
        )
        self.assertEqual(superuser, True)
        self.assertEqual(user, True)

    def test_onboard_user(self):
        organization = Organization.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")
        onboard_user = User.objects.get(email="demouser@tiltaccess.com")
        pronoun = Pronoun.objects.get(pronoun="she")
        source = Source.objects.get(source="instagram")
        user_category = UserCategory.objects.get(category="parent")
        income = Income.objects.get(category="h2", description="$110,000+")
        ethnicity = Ethnicity.objects.get(ethnicity="aian")

        onboard_user.is_verified = True
        onboard_user.is_onboarded = True
        onboard_user.preferred_contact_method= "email"
        onboard_user.phone_number= "7185551234"
        onboard_user.preferred_name = "Preferred"
        onboard_user.gpa = 4.0
        onboard_user.act_score = 35
        onboard_user.sat_math = 800
        onboard_user.sat_verbal = 800
        onboard_user.efc = 1
        onboard_user.pronouns = pronoun
        onboard_user.ethnicity = ethnicity
        onboard_user.user_category = user_category
        onboard_user.high_school_grad_year = 2020
        onboard_user.income = income
        onboard_user.organization.add(organization)
        onboard_user.save()

        self.assertEqual(onboard_user.is_verified, True)
        self.assertEqual(onboard_user.is_onboarded, True)
        self.assertEqual(onboard_user.is_test, False)
        self.assertEqual(onboard_user.is_staff, False)
        self.assertEqual(onboard_user.is_superuser, False)
        self.assertEqual(onboard_user.preferred_contact_method, "email")
        self.assertEqual(onboard_user.phone_number, "7185551234")
        self.assertEqual(onboard_user.preferred_name, "Preferred")
        self.assertEqual(onboard_user.gpa, 4.0)
        self.assertEqual(onboard_user.act_score, 35)
        self.assertEqual(onboard_user.sat_math, 800)
        self.assertEqual(onboard_user.sat_verbal, 800)
        self.assertEqual(onboard_user.efc, 1)
        self.assertEqual(onboard_user.pronouns, pronoun)
        self.assertEqual(onboard_user.ethnicity, ethnicity)
        self.assertEqual(onboard_user.user_category, user_category)
        self.assertEqual(onboard_user.high_school_grad_year, 2020)
        self.assertEqual(onboard_user.income, income)
        self.assertEqual(onboard_user.organization.get_queryset()[0], organization)

    def test_deleted_accounts(self):
        organization = Organization.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")
        superuser = User.objects.get(email="admin@tiltaccess.com")
        user = User.objects.get(email="demouser@tiltaccess.com")
        onboard_user1 = User.objects.get(email="demouser1@tiltaccess.com")
        onboard_user2 = User.objects.get(email="demouser2@tiltaccess.com")
        onboard_user3 = User.objects.get(email="demouser3@tiltaccess.com")
        pronoun = Pronoun.objects.get(pronoun="she")
        source = Source.objects.get(source="instagram")
        user_category = UserCategory.objects.get(category="parent")
        income = Income.objects.get(category="h2", description="$110,000+")
        ethnicity = Ethnicity.objects.get(ethnicity="aian")

        onboard_user1.is_verified = True
        onboard_user1.is_onboarded = True
        onboard_user1.preferred_contact_method= "email"
        onboard_user1.phone_number= "7185559876"
        onboard_user1.preferred_name = "Preferred"
        onboard_user1.gpa = 4.0
        onboard_user1.act_score = 35
        onboard_user1.sat_math = 800
        onboard_user1.sat_verbal = 800
        onboard_user1.efc = 1
        onboard_user1.pronouns = income
        onboard_user1.ethnicity = ethnicity
        onboard_user1.user_category = user_category
        onboard_user1.high_school_grad_year = 2020
        onboard_user1.income = income
        onboard_user1.organization.add(organization)
        onboard_user1.save()

        self.assertEqual(User.objects.filter(is_onboarded=True).count(), 1)

        onboard_user2.is_verified = True
        onboard_user2.is_onboarded = True
        onboard_user2.preferred_contact_method= "email"
        onboard_user2.phone_number= "7185556543"
        onboard_user2.preferred_name = "Preferred"
        onboard_user2.gpa = 4.0
        onboard_user2.act_score = 35
        onboard_user2.sat_math = 800
        onboard_user2.sat_verbal = 800
        onboard_user2.efc = 1
        onboard_user2.pronouns = income
        onboard_user2.ethnicity = ethnicity
        onboard_user2.user_category = user_category
        onboard_user2.high_school_grad_year = 2020
        onboard_user2.income = income
        onboard_user2.organization.add(organization)
        onboard_user2.save()

        self.assertEqual(User.objects.filter(is_onboarded=True).count(), 2)

        onboard_user3.is_verified = True
        onboard_user3.is_onboarded = True
        onboard_user3.preferred_contact_method= "email"
        onboard_user3.phone_number= "7185553219"
        onboard_user3.preferred_name = "Preferred"
        onboard_user3.gpa = 4.0
        onboard_user3.act_score = 35
        onboard_user3.sat_math = 800
        onboard_user3.sat_verbal = 800
        onboard_user3.efc = 1
        onboard_user3.pronouns = income
        onboard_user3.ethnicity = ethnicity
        onboard_user3.user_category = user_category
        onboard_user3.high_school_grad_year = 2020
        onboard_user3.income = income
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
            timestamp=timestamp
        )
        self.assertEqual(action.user, user)
        self.assertEqual(action.description, "Testing Actions")
        self.assertEqual(action.timestamp, timestamp)

    def test_create_pronoun(self):
        pronoun = Pronoun.objects.create(pronoun="he")

        self.assertEqual(pronoun.pronoun, "he")
        self.assertIsNotNone(pronoun.created)
        self.assertIsNotNone(pronoun.updated)

    def test_create_pronoun_user(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        pronoun = Pronoun.objects.get(pronoun="she")

        pronoun_user =PronounUser.objects.create(
            user=user,
            pronoun=pronoun,
            other_value=""
        )
        self.assertEqual(pronoun_user.user, user)
        self.assertEqual(pronoun_user.pronoun, pronoun)
        self.assertEqual(pronoun_user.other_value, "")
        self.assertIsNotNone(pronoun_user.created)
        self.assertIsNotNone(pronoun_user.updated)
        self.assertEqual(user.pronounuser_set.get_queryset()[0], pronoun_user)

    def test_create_source(self):
        source = Source.objects.create(source="facebook")

        self.assertEqual(source.source, "facebook")
        self.assertIsNotNone(source.created)
        self.assertIsNotNone(source.updated)

    def test_create_source_user(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        source = Source.objects.get(source="instagram")

        source_user = SourceUser.objects.create(
            user=user,
            source=source,
            other_value=""
        )
        self.assertEqual(source_user.user, user)
        self.assertEqual(source_user.source, source)
        self.assertEqual(source_user.other_value, "")
        self.assertIsNotNone(source_user.created)
        self.assertIsNotNone(source_user.updated)
        self.assertEqual(user.sourceuser_set.get_queryset()[0], source_user)

    def test_create_user_category(self):
        user_category = UserCategory.objects.create(category="student")

        self.assertEqual(user_category.category, "student")
        self.assertIsNotNone(user_category.created)
        self.assertIsNotNone(user_category.updated)

    def test_create_income(self):
        income = Income.objects.create(category="lo", description="$0 - 30,000")

        self.assertEqual(income.category, "lo")
        self.assertEqual(income.description, "$0 - 30,000")
        self.assertIsNotNone(income.created)
        self.assertIsNotNone(income.updated)

    def test_create_ethnicity(self):
        ethnicity = Ethnicity.objects.create(ethnicity="asian")

        self.assertEqual(ethnicity.ethnicity, "asian")
        self.assertIsNotNone(ethnicity.created)
        self.assertIsNotNone(ethnicity.updated)

    def test_create_ethnicity_user(self):
        user = User.objects.get(email="demouser@tiltaccess.com")
        ethnicity = Ethnicity.objects.get(ethnicity="aian")

        ethnicity_user = EthnicityUser.objects.create(
            user=user,
            ethnicity=ethnicity,
            other_value=""
        )
        self.assertEqual(ethnicity_user.user, user)
        self.assertEqual(ethnicity_user.ethnicity, ethnicity)
        self.assertEqual(ethnicity_user.other_value, "")
        self.assertIsNotNone(ethnicity_user.created)
        self.assertIsNotNone(ethnicity_user.updated)
        self.assertEqual(user.ethnicityuser_set.get_queryset()[0], ethnicity_user)
