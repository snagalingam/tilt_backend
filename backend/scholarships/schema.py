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
    organization = graphene.String()
    url = graphene.String()
    due_date = graphene.types.datetime.Date()
    max_amount = graphene.Int()
    renewable = graphene.Boolean()
    category = graphene.String()
    area_of_study = graphene.String()
    location = graphene.String()
    state = graphene.String()
    ethnicity = graphene.String()
    gender = graphene.String()
    gpa = graphene.Float()
    us_citizen = graphene.Boolean()
    daca_status = graphene.Boolean()
    financial_need = graphene.Boolean()
    hbcu = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        organization = graphene.String()
        url = graphene.String()
        due_date = graphene.types.datetime.Date()
        max_amount = graphene.Int()
        renewable = graphene.Boolean()
        category = graphene.String()
        area_of_study = graphene.String()
        location = graphene.String()
        state = graphene.String()
        ethnicity = graphene.String()
        gender = graphene.String()
        gpa = graphene.Float()
        us_citizen = graphene.Boolean()
        daca_status = graphene.Boolean()
        financial_need = graphene.Boolean()
        hbcu = graphene.Boolean()

    def mutate(
        self,
        info,
        name,
        organization,
        url,
        due_date,
        max_amount,
        renewable,
        category,
        area_of_study,
        location,
        state,
        ethnicity,
        gender,
        gpa,
        us_citizen,
        daca_status,
        financial_need,
        hbcu
    ):

        scholarship = Scholarship(
            name=name,
            organization=organization,
            url=url,
            due_date=due_date,
            max_amount=max_amount,
            renewable=renewable,
            category=category,
            area_of_study=area_of_study,
            location=location,
            state=state,
            ethnicity=ethnicity,
            gender=gender,
            gpa=gpa,
            us_citizen=us_citizen,
            daca_status=daca_status,
            financial_need=financial_need,
            hbcu=hbcu,
        )
        scholarship.save()

        return CreateScholarship(scholarship=scholarship)

class Mutation(graphene.ObjectType):
    create_scholarship = CreateScholarship.Field()
