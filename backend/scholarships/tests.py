from django.test import TestCase

from .models import Scholarship


class ScholarshipTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Scholarship.objects.create(
            name='first scholarship',
            url='https://www.scholarship.com',
            amount='1000',
            amount_descriptor='exact',
            deadline='2020-03-31',
        )

    def test_scholarship_content(self):
        scholarship = Scholarship.objects.get(id=1)
        name = f'{scholarship.name}'
        url = f'{scholarship.url}'
        amount = f'{scholarship.amount}'
        amount_descriptor = f'{scholarship.amount_descriptor}'
        deadline = f'{scholarship.deadline}'
        self.assertEquals(name, 'first scholarship')
        self.assertEquals(url, 'https://www.scholarship.com')
        self.assertEquals(amount, '1000')
        self.assertEquals(amount_descriptor, 'exact')
        self.assertEquals(deadline, '2020-03-31')
