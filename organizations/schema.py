import graphene

from organizations.models import Organization
from graphene_django import DjangoObjectType
from services.google_api.google_places import GooglePlacesAPI


################################################
### Standard Model Definitions
################################################
class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = (
            # main information
            'id',
            'name',
            'place_id',
            'partner',

            # additional details
            'address',
            'business_status',
            'icon',
            'lat',
            'lng',
            'phone_number',
            'types',
            'url',
            'website'
        )


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

    def resolve_organizations_by_fields(self, info, **kwargs):
        qs = Organization.objects.filter(**kwargs)
        return qs


################################################
### Mutations
################################################
class MutateOrganization(graphene.Mutation):
    organization = graphene.Field(OrganizationType)

    def mutate(self, info):
        return "hi"

class Mutation(graphene.ObjectType):
    mutate_organization = MutateOrganization.Field()
