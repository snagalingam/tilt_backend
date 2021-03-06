import graphene

from organizations.models import Organization
from graphene_django import DjangoObjectType
from services.google.google_places import GooglePlacesAPI


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
    # graphene type
    organizations = graphene.List(OrganizationType)

    # function definition
    def resolve_organizations(self, info):
        user = info.context.user

        if user.is_authenticated and user.is_superuser:
            qs = Organization.objects.all()
            return qs
        raise Exception("User does not have access to this data")

################################################
### Mutations
################################################
class MutateOrganization(graphene.Mutation):
    organization = graphene.Field(OrganizationType)

    def mutate(self, info):
        return "don't need a mutation. use user mutations"

class Mutation(graphene.ObjectType):
    mutate_organization = MutateOrganization.Field()
