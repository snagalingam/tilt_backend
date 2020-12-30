from django.test import TestCase
from organizations.models import Organization

class OrganizationTests(TestCase):

    def setUp(self):
        Organization.objects.create(
            place_id="ChIJ91htBQIXYogRtPsg4NGoNv0",
            business_status="OPERATIONAL",
            icon="",
            name="Alabama A&M University",
            lat=34.782719,
            lng=-86.568614,
            address="Huntsville, AL 35811, USA",
            phone_number="(256) 372-5000",
            url="https://maps.google.com/?cid=18245956559700032436",
            website="http://www.aamu.edu/",
            types=["school", "point_of_interest", "establishment"],
            partner=False,
        )

    def test_create_organization(self):
        organization = Organization.objects.get(place_id="ChIJ91htBQIXYogRtPsg4NGoNv0")

        self.assertEqual(organization.place_id, "ChIJ91htBQIXYogRtPsg4NGoNv0")
        self.assertEqual(organization.business_status, "OPERATIONAL")
        self.assertEqual(organization.icon, "")
        self.assertEqual(organization.name, "Alabama A&M University")
        self.assertEqual(organization.lat, 34.782719)
        self.assertEqual(organization.lng, -86.568614)
        self.assertEqual(organization.address, "Huntsville, AL 35811, USA")
        self.assertEqual(organization.phone_number, "(256) 372-5000")
        self.assertEqual(organization.url, "https://maps.google.com/?cid=18245956559700032436")
        self.assertEqual(organization.website, "http://www.aamu.edu/")
        self.assertEqual(organization.types, ["school", "point_of_interest", "establishment"])
        self.assertFalse(organization.partner)
        self.assertIsNotNone(organization.created)
        self.assertIsNotNone(organization.updated)
