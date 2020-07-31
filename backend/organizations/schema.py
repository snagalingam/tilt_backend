import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Organization


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization

class Query(graphene.ObjectType):
    Organizations = graphene.List(OrganizationType)

    def resolve_organizations(self, info, **kwargs):
        return Organization.objects.all()

class CreateOrganization(graphene.Mutation):
    id = graphene.Int()
    place_id = graphene.String()
    name = graphene.String()
    formatted_address = graphene.String()
    formatted_phone_number = graphene.Int()
    geo_location = graphene.String()
    business_status = graphene.String()
    url = graphene.String()
    website = graphene.String()
    partnership = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        place_id = graphene.String()
        name = graphene.String()
        formatted_address = graphene.String()
        formatted_phone_number = graphene.Int()
        geo_location = graphene.String()
        business_status = graphene.String()
        url = graphene.String()
        website = graphene.String()
        partnership = graphene.Boolean()

    def mutate(
        self,
        info,
        place_id,
        name,
        formatted_address,
        formatted_phone_number,
        geo_location,
        business_status,
        url,
        website,
        partnership,
    ):

        Organization = Organization(
            place_id=place_id,
            name=name,
            formatted_address=formatted_address,
            formatted_phone_number=formatted_phone_number,
            geo_location=geo_location,
            business_status=business_status,
            url=url,
            website=website,
            partnership=partnership,
        )
        Organization.save()

        return CreateOrganization(
            id=Organization.id,
            place_id=Organization.place_id,
            name=Organization.name,
            formatted_address=Organization.formatted_address,
            formatted_phone_number=Organization.formatted_phone_number,
            geo_location=Organization.geo_location,
            business_status=Organization.business_status,
            url=Organization.url,
            website=Organization.website,
            partnership=Organization.partnership,
        )

class Mutation(graphene.ObjectType):
    create_organization = CreateOrganization.Field()
