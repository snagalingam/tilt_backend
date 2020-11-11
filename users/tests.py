from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    
    User = get_user_model()
    def test_create_user_required_fields(self):
        user = User.objects.create_user(
            email = 'kevin@email.com',
            first_name = 'kevin',
            user_type = 'Student',
            password = 'testpass123'
        )
        self.assertEqual(user.email, 'kevin@email.com')
        self.assertEqual(user.first_name, 'kevin')
        self.assertEqual(user.last_name, None)
        self.assertEqual(user.preferred_name, None)
        self.assertEqual(user.gpa, None)
        self.assertEqual(user.act_score, None)
        self.assertEqual(user.sat_score, None)
        self.assertEqual(user.efc, None)
        self.assertFalse(user.terms_and_conditions)
        self.assertEqual(user.pronouns, None)
        self.assertEqual(user.pronouns_other_value, None)
        self.assertEqual(user.ethnicity, None)
        self.assertEqual(user.ethnicity_other_value, None)
        self.assertEqual(user.user_type, 'Student')
        self.assertEqual(user.highschool_graduation_year, '2020')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.password)

    def test_create_superuser_required_fields(self):
        admin_user = User.objects.create_superuser(
            email = 'superadmin@email.com',
            first_name = 'superadmin',
            user_type = 'Counselor',
            password = 'admintestuser123'
        )
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertEqual(admin_user.first_name, 'superadmin')
        self.assertEqual(admin_user.last_name, None)
        self.assertEqual(admin_user.preferred_name, None)
        self.assertEqual(admin_user.gpa, None)
        self.assertEqual(admin_user.act_score, None)
        self.assertEqual(admin_user.sat_score, None)
        self.assertEqual(admin_user.efc, None)
        self.assertFalse(admin_user.terms_and_conditions)
        self.assertEqual(admin_user.pronouns, None)
        self.assertEqual(admin_user.pronouns_other_value, None)
        self.assertEqual(admin_user.ethnicity, None)
        self.assertEqual(admin_user.ethnicity_other_value, None)
        self.assertEqual(admin_user.user_type, 'Counselor')
        self.assertEqual(admin_user.highschool_graduation_year, '2020')
        self.assertFalse(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNotNone(admin_user.password)

    def test_create_specify_all_fields(self):
        user = User.objects.create_user(
            email = 'lisa@email.com',
            first_name = 'lisa',
            user_type = 'Counselor',
            preferred_name = "liz",
            last_name = "wayne",
            gpa = 4.00,
            act_score = 5,
            sat_score = 30,
            efc = 5000,
            terms_and_conditions = True,
            pronouns = 'She/hers',
            pronouns_other_value = '',
            ethnicity = 'Hispanic/Latinx',
            ethnicity_other_value = 'Alien/Martian',
            highschool_graduation_year = '2022',
            is_staff = True,
            password = 'testing456'
        )
        self.assertEqual(user.email, 'lisa@email.com')
        self.assertEqual(user.first_name, 'lisa')
        self.assertEqual(user.user_type, 'Counselor')
        self.assertEqual(user.last_name, 'wayne')
        self.assertEqual(user.preferred_name, 'liz')
        self.assertEqual(user.gpa, 4.00)
        self.assertEqual(user.act_score, 5)
        self.assertEqual(user.sat_score, 30)
        self.assertEqual(user.efc, 5000)
        self.assertTrue(user.terms_and_conditions)
        self.assertEqual(user.pronouns, 'She/hers')
        self.assertEqual(user.pronouns_other_value, '')
        self.assertEqual(user.ethnicity, 'Hispanic/Latinx')
        self.assertEqual(user.ethnicity_other_value, 'Alien/Martian')
        self.assertEqual(user.highschool_graduation_year, '2022')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertIsNotNone(user.password)

    def test_create_superuser_specify_all_fields(self):
        admin_user = User.objects.create_superuser(
            email = 'superparent@example.com',
            first_name = 'superparent',
            user_type = 'Parent',
            preferred_name = "superduperparent",
            last_name = "guardian",
            act_score = 21,
            sat_score = 32,
            gpa = 3.22,
            efc = 9982,
            terms_and_conditions = False,
            pronouns = '',
            pronouns_other_value = 'him/himself',
            ethnicity = 'Black/African',
            ethnicity_other_value = 'otherethnicity',
            highschool_graduation_year = '2025',
            is_staff = True,
            password = 'testing987'
        )
        self.assertEqual(admin_user.email, 'superparent@example.com')
        self.assertEqual(admin_user.first_name, 'superparent')
        self.assertEqual(admin_user.user_type, 'Parent')
        self.assertEqual(admin_user.last_name, 'guardian')
        self.assertEqual(admin_user.preferred_name, 'superduperparent')
        self.assertEqual(admin_user.gpa, 3.22)
        self.assertEqual(admin_user.act_score, 21)
        self.assertEqual(admin_user.sat_score, 32)
        self.assertEqual(admin_user.efc, 9982)
        self.assertFalse(admin_user.terms_and_conditions)
        self.assertEqual(admin_user.pronouns, '')
        self.assertEqual(admin_user.pronouns_other_value, 'him/himself')
        self.assertEqual(admin_user.ethnicity, 'Black/African')
        self.assertEqual(admin_user.ethnicity_other_value, 'otherethnicity')
        self.assertEqual(admin_user.highschool_graduation_year, '2025')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNotNone(admin_user.password)