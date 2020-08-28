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

    def resolve_organization_by_id(root, info, id):
        return Organization.objects.get(pk=id)

    def resolve_organization_by_place_id(root, info, place_id):
        return Organization.objects.get(place_id=place_id)

    def resolve_organization_by_name(root, info, name):
        return Organization.objects.filter(name=name)

    def resolve_organization_by_tilt_partnership(root, info, tilt_partnership):
        return Organization.objects.filter(tilt_partnership=tilt_partnership)


class CreateOrganization(graphene.Mutation):
    organization = graphene.Field(OrganizationType)

    class Arguments:
        place_id = graphene.String()
        business_status = graphene.String()
        icon = graphene.String()
        name = graphene.String()
        lat = graphene.String()
        lng = graphene.String()
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

        place_id = data['place_id']
        business_status = data['result']['business_status']
        icon = data['result']['icon']
        name = data['result']['name']
        lat = data['result']['geometry']['location']['lat']
        lng = data['result']['geometry']['location']['lng']
        address = data['result']['formatted_address']
        phone_number = data['result']['formatted_phone_number']
        url = data['result']['url']
        website = data['result']['website']
        types = data['result']['types']

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
