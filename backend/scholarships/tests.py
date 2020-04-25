from django.test import TestCase

from .models import Scholarship


class ScholarshipTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Scholarship.objects.create(
            name='first scholarship',
            organization='organization',
            url='https://www.scholarship.com',
            due_date='2020-03-31',
            max_amount='1000',
            renewable=True,
            area_of_study='Business',
            location='Chicago',
            state='IL',
            ethnicity='Asian',
            gender='Woman',
            gpa='4.00',
            us_citizen=True,
            daca_status=True,
            financial_need=True,
            hbcu=True,
        )

        Scholarship.objects.create(
            name='second scholarship',
            url='https://www.secondscholarship.com',
            due_date='2020-04-01',
            us_citizen=False,
            daca_status=False,
            financial_need=False,
            hbcu=False,
        )

    def test_scholarship_content_without_blanks(self):
        scholarship = Scholarship.objects.get(id=1)
        name = f'{scholarship.name}'
        organization = f'{scholarship.organization}'
        url = f'{scholarship.url}'
        due_date = f'{scholarship.due_date}'
        max_amount = f'{scholarship.max_amount}'
        renewable = scholarship.renewable
        area_of_study = f'{scholarship.area_of_study}'
        location = f'{scholarship.location}'
        state = f'{scholarship.state}'
        ethnicity = f'{scholarship.ethnicity}'
        gender = f'{scholarship.gender}'
        gpa = f'{scholarship.gpa}'
        us_citizen = scholarship.us_citizen
        daca_status = scholarship.daca_status
        financial_need = scholarship.financial_need
        hbcu = scholarship.hbcu

        self.assertEquals(name, 'first scholarship')
        self.assertEquals(organization, 'organization')
        self.assertEquals(url, 'https://www.scholarship.com')
        self.assertEquals(due_date, '2020-03-31')
        self.assertEquals(max_amount, '1000')
        self.assertTrue(renewable)
        self.assertEquals(area_of_study, 'Business')
        self.assertEquals(location, 'Chicago')
        self.assertEquals(state, 'IL')
        self.assertEquals(ethnicity, 'Asian')
        self.assertEquals(gender, 'Woman')
        self.assertEquals(gpa, '4.00')
        self.assertTrue(us_citizen)
        self.assertTrue(daca_status)
        self.assertTrue(financial_need)
        self.assertTrue(hbcu)

    def test_scholarship_content_with_blanks(self):
        scholarship = Scholarship.objects.get(id=2)
        name = f'{scholarship.name}'
        organization = scholarship.organization
        url = f'{scholarship.url}'
        due_date = f'{scholarship.due_date}'
        max_amount = scholarship.max_amount
        renewable = scholarship.renewable
        area_of_study = scholarship.area_of_study
        location = scholarship.location
        state = scholarship.state
        ethnicity = scholarship.ethnicity
        gender = scholarship.gender
        gpa = scholarship.gpa
        us_citizen = scholarship.us_citizen
        daca_status = scholarship.daca_status
        financial_need = scholarship.financial_need
        hbcu = scholarship.hbcu

        self.assertEquals(name, 'second scholarship')
        self.assertIsNone(organization)
        self.assertEquals(url, 'https://www.secondscholarship.com')
        self.assertEquals(due_date, '2020-04-01')
        self.assertIsNone(max_amount)
        self.assertIsNone(renewable)
        self.assertIsNone(area_of_study)
        self.assertIsNone(location)
        self.assertIsNone(state)
        self.assertIsNone(ethnicity)
        self.assertIsNone(gender)
        self.assertIsNone(gpa)
        self.assertFalse(us_citizen)
        self.assertFalse(daca_status)
        self.assertFalse(financial_need)
        self.assertFalse(hbcu)
