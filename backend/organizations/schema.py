import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Organization
from .google_places import GooglePlacesAPI

class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization

class Query(graphene.ObjectType):
    organization_by_pk = graphene.Field(OrganizationType)
    organizations = graphene.List(OrganizationType)

    def resolve_organization_by_pk(self, info, pk):
        return Organization.objects.get(pk=pk)
    
    def resolve_organizations(self, info):
        return Organization.objects.all()

class CreateOrganization(graphene.Mutation):
    organization = graphene.Field(OrganizationType)
    id = graphene.Int()
    place_id = graphene.String()
    business_status = graphene.String()
    icon = graphene.String()
    name = graphene.String()
    lat = graphene.String()
    lng = graphene.String()
    address = graphene.String()
    phone_number = graphene.Int()
    url = graphene.String()
    website = graphene.String()
    types = graphene.List(graphene.String)
    website = graphene.String()
    tilt_partnership = graphene.Boolean()

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

# class SearchForOrganization(graphene.Mutation):
#     class Arguments:
#         place = graphene.String()
#         zipcode = graphene.String()

#     def mutate(self, info, place, zipcode):
#         api = GooglePlacesAPI()
#         data = api.details(place, zipcode)

#         place_id = data['place_id']
#         business_status = data['result']['business_status']
#         icon = data['result']['icon']
#         name = data['result']['name']
#         lat = data['result']['geometry']['location']['lat']
#         lng = data['result']['geometry']['location']['lng']
#         address = data['result']['formatted_address']
#         phone_number = data['result']['formatted_phone_number']
#         url = data['result']['url']
#         website = data['result']['website']
#         types = data['result']['types']

#         org = Organization.objects.get(name=name)
#         if org is None:
#             organization = Organization(
#                 place_id=place_id,
#                 business_status=business_status,
#                 icon=icon,
#                 name=name,
#                 lat=lat,
#                 lng=lng,
#                 address=address,
#                 phone_number=phone_number,
#                 url=url,
#                 website=website,
#                 types=types,
#                 tilt_partnership=tilt_partnership,
#             )
#             organization.save()
#             return SearchForOrganization(organization=organization)
#         else:
#             return SearchForOrganization(org=org)

class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
    # search_for_organization = SearchForOrganization.Field()
