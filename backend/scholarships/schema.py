import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Scholarship


class ScholarshipType(DjangoObjectType):
    class Meta:
        model = Scholarship

class Query(graphene.ObjectType):
    scholarships = graphene.List(ScholarshipType)

    def resolve_scholarships(self, info, **kwargs):
        return Scholarship.objects.all()

class CreateScholarship(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    amount = graphene.Int()
    amount_descriptor = graphene.String()
    deadline = graphene.types.datetime.Date()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        amount = graphene.Int()
        amount_descriptor = graphene.String()
        deadline = graphene.types.datetime.Date()

    def mutate(self, info, url, amount, amount_descriptor, deadline):
        user = info.context.user or None

        scholarship = Scholarship(
            url=url,
            amount=amount,
            amount_descriptor=amount_descriptor,
            deadline=deadline,
            posted_by=user,
        )
        scholarship.save()

        return CreateScholarship(
            id=scholarship.id,
            url=scholarship.url,
            amount=scholarship.amount,
            amount_descriptor=scholarship.amount_descriptor,
            deadline=scholarship.deadline,
            posted_by=scholarship.posted_by,
        )

class Mutation(graphene.ObjectType):
    create_scholarship = CreateScholarship.Field()
