import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import TiltPartner


class TiltPartnerType(DjangoObjectType):
    class Meta:
        model = TiltPartner


class Query(graphene.ObjectType):
    tilt_partners = graphene.List(TiltPartnerType)

    def resolve_organizations(self, info):
        return TiltPartner.objects.all()


class CreateTiltPartner(graphene.Mutation):
    tilt_partner = graphene.Field(TiltPartnerType)

    class Arguments:
        place_id = graphene.String()
        name = graphene.String()
        tilt_partnership = graphene.Boolean()

    def mutate(
        self,
        info,
        place_id,
        name,
        tilt_partnership
    ):

        tilt_partner = TiltPartner(
            place_id=place_id,
            name=name,
            tilt_partnership=tilt_partnership,
        )
        tilt_partner.save()

        return CreateTiltPartner(tilt_partner=tilt_partner)

class Mutation(graphene.ObjectType):
    create_tilt_partner = CreateTiltPartner.Field()
