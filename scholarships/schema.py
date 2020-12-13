import graphene
from graphene_django import DjangoObjectType

from users.schema import UserType
from .models import Scholarship, Provider

class ProviderType(DjangoObjectType):
    class Meta:
        model = Provider

class ScholarshipType(DjangoObjectType):
    class Meta:
        model = Scholarship

class Query(graphene.ObjectType):
    providers = graphene.List(ProviderType)
    dproviders_results_by_fields = graphene.List(
        ProviderType, 
        name=graphene.String(),
        sent=graphene.Boolean(),
        processed=graphene.Boolean(),
        pass_fail=graphene.Boolean(),
        expired=graphene.Boolean(),
        start_date=graphene.Boolean())
    scholarships = graphene.List(ScholarshipType)
    scholarship_by_name = graphene.Field(ScholarshipType, name=graphene.String())

    def resolve_providers(self, info):
        return ProviderType.objects.all()

    def resolve_provider_by_field(self, info, name=None):
        qs = ProviderType.objects.get(name=name)
        return qs

    def resolve_scholarships(self, info):
        return Scholarship.objects.all()

    def resolve_scholarship_by_name(self, info, name=None):
        qs = Scholarship.objects.get(name=name)
        return qs

class CreateProvider(graphene.Mutation):
    contact = graphene.Field(ProviderType)

    class Arguments:
        name = graphene.String()
        address = graphene.String()
        city = graphene.String()
        state = graphene.String()
        zipcode = graphene.String()
        email = graphene.String()
        phone_number = graphene.String()
        phone_number_ext = graphene.String()

    def mutate(
        self,
        info,
        name=None,
        address=None,
        city=None,
        state=None,
        zipcode=None,
        email=None,
        phone_number=None,
        phone_number_ext=None,
    ):

        contact = Provider(
            name=name,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            email=email,
            phone_number=phone_number,
            phone_number_ext=phone_number_ext,
        )
        contact.save()

        return CreateProvider(contact=contact)


class CreateScholarship(graphene.Mutation):
    scholarship = graphene.Field(ScholarshipType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()
        website = graphene.String()
        deadline = graphene.Date()
        date_added = graphene.DateTime()
        max_amount = graphene.Int()
        renewable = graphene.Boolean()
        number_awards = graphene.Int()
        education_level = graphene.List(graphene.String)
        education_requirements = graphene.String()
        area_of_study = graphene.List(graphene.String)
        area_of_study_description = graphene.String()
        writing_competition = graphene.Boolean()
        # interest = graphene.String()
        association_requirement = graphene.List(graphene.String)
        location = graphene.String()
        state = graphene.String()
        ethnicity = graphene.List(graphene.String)
        gender = graphene.String()
        min_gpa = graphene.Float()
        max_gpa = graphene.Float()
        min_act = graphene.Int()
        min_sat = graphene.Int()
        disability = graphene.String()
        military = graphene.String()
        citizenship = graphene.List(graphene.String)
        first_generation = graphene.Boolean()
        financial_need = graphene.Boolean()

    def mutate(
        self,
        info,
        name=None,
        description=None,
        website=None,
        deadline=None,
        date_added=None,
        max_amount=None,
        renewable=None,
        number_awards=None,
        education_level=None,
        education_requirements=None,
        area_of_study=None,
        area_of_study_description=None,
        writing_competition=None,
        # interest=None,
        association_requirement=None,
        location=None,
        state=None,
        ethnicity=None,
        gender=None,
        min_gpa=None,
        max_gpa=None,
        min_act=None,
        min_sat=None,
        disability=None,
        military=None,
        citizenship=None,
        first_generation=None,
        financial_need=None,
    ):

        contact = Provider.objects.get(name=name)

        scholarship = Scholarship(
            name=name,
            contact=contact,
            description=description,
            website=website,
            deadline=deadline,
            date_added=date_added,
            max_amount=max_amount,
            renewable=renewable,
            number_awards=number_awards,
            education_level=education_level,
            education_requirements=education_requirements,
            area_of_study=area_of_study,
            area_of_study_description=area_of_study_description,
            writing_competition=writing_competition,
            # interest=None,
            association_requirement=association_requirement,
            location=location,
            state=state,
            ethnicity=ethnicity,
            gender=gender,
            min_gpa=min_gpa,
            max_gpa=max_gpa,
            min_act=min_act,
            min_sat=min_sat,
            disability=disability,
            military=military,
            citizenship=citizenship,
            first_generation=first_generation,
            financial_need=financial_need,
        )
        scholarship.save()

        return CreateScholarship(scholarship=scholarship)

class Mutation(graphene.ObjectType):
    create_contact = CreateProvider.Field()
    create_scholarship = CreateScholarship.Field()
