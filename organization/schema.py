import graphene

from organization.models import Organization
from graphene_django import DjangoObjectType
from services.google_api.google_places import GooglePlacesAPI


################################################
### Standard Model Definitions
################################################
class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"


################################################
### Query
################################################
class Query(graphene.ObjectType):
    organizations = graphene.List(OrganizationType)
    organizations_by_fields = graphene.Field(
        OrganizationType,
        id=graphene.Int(),
        name=graphene.String(),
        partner=graphene.Boolean(),
        place_id=graphene.String()
    )

    def resolve_organizations(self, info):
        qs = Organization.objects.all()
        return qs

    def resolve_organizations_by_fields(self, info, **fields):
        qs = Organization.objects.filter(**fields)
        return qs


################################################
### Mutation
################################################
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
        partner = graphene.Boolean()

    def mutate(
        self,
        info,
        place_id=None,
        business_status=None,
        icon=None,
        name=None,
        lat=None,
        lng=None,
        address=None,
        phone_number=None,
        url=None,
        website=None,
        types=None,
        partner=None,
    ):

        try:
            organization = Organization.objects.get(place_id=place_id)
        except:
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
                partner=partner,
            )
            
            organization.save()
            return CreateOrganization(organization=organization)
        raise Exception('Organization already exists')


class OrganizationSearch(graphene.Mutation):
    organization = graphene.Field(OrganizationType)

    class Arguments:
        place = graphene.String()
        location = graphene.String()

    def mutate(self, info, place, location):
        api = GooglePlacesAPI()
        data = api.details(place, location)
        errors = data.get("errors", None)

        if errors:
            raise errors

        results = data.get("result")
        place_id = data.get('place_id', "")
        place_name = results.get("name")
        location = results["geometry"]["location"]
        lat = location.get("lat", None)
        lng = location.get("lng", None)
        business_status = results.get("business_status", "")
        icon = results.get("icon", "")
        address = results.get("formatted_address", "")
        place_phone_number = results.get("formatted_phone_number", "")
        url = results.get("url", "")
        types = results.get("types", [])
        website = results.get("website", "")

        organization = Organization(
            place_id=place_id,
            business_status=business_status,
            icon=icon,
            name=place_name,
            lat=lat,
            lng=lng,
            address=address,
            phone_number=place_phone_number,
            url=url,
            website=website,
            types=types,
        )
        return OrganizationSearch(organization=organization)


class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
    organization_search = OrganizationSearch.Field()
