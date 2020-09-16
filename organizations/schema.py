import graphene
from graphene_django import DjangoObjectType

from .models import Organization
from services.google_api.google_places import GooglePlacesAPI


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"


class Query(graphene.ObjectType):
    organizations = graphene.List(OrganizationType)
    organization_by_id = graphene.Field(
        OrganizationType, id=graphene.Int())
    organization_by_place_id = graphene.Field(
        OrganizationType, place_id=graphene.String())
    organization_by_name = graphene.List(
        OrganizationType, name=graphene.String())
    organization_by_tilt_partnership = graphene.List(
        OrganizationType, tilt_partnership=graphene.Boolean())

    def resolve_organizations(self, info):
        return Organization.objects.all()

    def resolve_organization_by_id(self, info, id):
        return Organization.objects.get(pk=id)

    def resolve_organization_by_place_id(self, info, place_id):
        return Organization.objects.get(place_id=place_id)

    def resolve_organization_by_name(self, info, name):
        return Organization.objects.filter(name=name)

    def resolve_organization_by_tilt_partnership(self, info, tilt_partnership):
        return Organization.objects.filter(tilt_partnership=tilt_partnership)


class CreateOrganization(graphene.Mutation):
    organization = graphene.Field(OrganizationType)

    class Arguments:
        place_id = graphene.String()
        business_status = graphene.String()
        icon = graphene.String()
        name = graphene.String()
        lat = graphene.Float()
        lng = graphene.Float()
        address = graphene.String()
        phone_number = graphene.String()
        url = graphene.String()
        website = graphene.String()
        types = graphene.List(graphene.String)
        tilt_partnership = graphene.Boolean()

    def mutate(
        self,
        info,
        place_id,
        business_status,
        icon,
        name,
        lat,
        lng,
        address,
        phone_number,
        url,
        website,
        types,
        tilt_partnership
    ):

        try:
            organization = Organization.objects.get(place_id=place_id)
        except Organization.DoesNotExist:
            organization = None

        if organization is None:
            organization = Organization(
                place_id=place_id,
                business_status=business_status,
                icon=icon,
                name=name,
                lat=lat,
                lng=lng,
                address=address,
                phone_number=phone_number,
                url=url,
                website=website,
                types=types,
                tilt_partnership=tilt_partnership,
            )
            organization.save()
            return CreateOrganization(organization=organization)
        else:
            return CreateOrganization(organization=organization)


class OrganizationSearch(graphene.Mutation):
    organization = graphene.Field(OrganizationType)

    class Arguments:
        place = graphene.String()
        location = graphene.String()

    def mutate(self, info, place, location):
        api = GooglePlacesAPI()
        data = api.details(place, location)

        try:
            if data["errors"] is not None:
                return ValueError(data["errors"])
        except:
            results = data.get('result')

            place_id = data.get('place_id')
            business_status = results.get('business_status', None)
            icon = results.get('icon', None)
            name = results.get('name', None)
            lat = results.get("geometry")["location"]["lat"]
            lng = results.get("geometry")["location"]["lng"]
            address = results.get('formatted_address', None)
            phone_number = results.get('formatted_phone_number', None)
            url = results.get('url', None)
            website = results.get('website', None)
            types = results.get('types', [])

            organization = Organization(
                place_id=place_id,
                business_status=business_status,
                icon=icon,
                name=name,
                lat=lat,
                lng=lng,
                address=address,
                phone_number=phone_number,
                url=url,
                website=website,
                types=types,
            )

            return OrganizationSearch(organization=organization)


class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
    organization_search = OrganizationSearch.Field()
