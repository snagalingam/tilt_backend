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
    name = graphene.String()
    amount = graphene.Int()
    deadline = graphene.types.datetime.Date()
    url = graphene.String()

    class Arguments:
        name = graphene.String()
        amount = graphene.Int()
        deadline = graphene.types.datetime.Date()
        url = graphene.String()

    def mutate(self, info, name, amount, deadline, url):

        scholarship = Scholarship(
            name=name,
            amount=amount,
            deadline=deadline,
            url=url,
        )
        scholarship.save()

        return CreateScholarship(
            id=scholarship.id,
            name=scholarship.name,
            amount=scholarship.amount,
            deadline=scholarship.deadline,
            url=scholarship.url,
        )

class Mutation(graphene.ObjectType):
    create_scholarship = CreateScholarship.Field()
