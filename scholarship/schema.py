import datetime
import graphene
import math

from scholarship.models import Provider, Scholarship, ScholarshipStatus
from college.models import College
from django.contrib.auth import get_user_model
from django.db.models import Q, Max, Min, F
from graphene_django import DjangoObjectType


################################################
### Standard Model Definitions
################################################
class ScholarshipProviderType(DjangoObjectType):
    class Meta:
        model = Provider
        fields = "__all__"


class ScholarshipType(DjangoObjectType):
    class Meta:
        model = Scholarship
        fields = "__all__"


class ScholarshipPaginationType(graphene.ObjectType):
    count = graphene.Int()
    pages = graphene.Int()
    search_results = graphene.List(ScholarshipType)


class ScholarshipStatusType(DjangoObjectType):
    class Meta:
        model = ScholarshipStatus
        fields = "__all__"

################################################
### Query
################################################
class Query(graphene.ObjectType):
    scholarship_providers = graphene.List(ScholarshipProviderType, limit=graphene.Int())
    scholarship_status = graphene.List(ScholarshipStatusType, limit=graphene.Int())
    scholarships = graphene.List(ScholarshipType, limit=graphene.Int())

    # providers
    provider_by_fields = graphene.List(
        ScholarshipProviderType,
        organization=graphene.String(),
        addressee=graphene.String(),
        address=graphene.String(),
        city=graphene.String(),
        state=graphene.String(),
        zipcode=graphene.String(),
        email=graphene.String(),
        phone_number=graphene.String(),
        phone_number_ext=graphene.String())

    # scholarships
    scholarship_max_amount = graphene.Int()

    scholarship_by_fields = graphene.List(
        ScholarshipType,
        name=graphene.String(),
        provider_id=graphene.Int(),
        description=graphene.String(),
        website=graphene.String(),
        deadline=graphene.Date(),
        max_amount=graphene.Int(),
        renewable=graphene.Boolean(),
        number_awards=graphene.Int(),
        education_level=graphene.List(graphene.String),
        education_requirements=graphene.String(),
        area_of_study=graphene.List(graphene.String),
        area_of_study_description=graphene.String(),
        writing_competition=graphene.Boolean(),
        interest_description=graphene.String(),
        college_id=graphene.Int(),
        association_requirement=graphene.List(graphene.String),
        location=graphene.String(),
        state=graphene.String(),
        ethnicity=graphene.List(graphene.String),
        gender=graphene.String(),
        min_gpa=graphene.Float(),
        max_gpa=graphene.Float(),
        min_act=graphene.Int(),
        min_sat=graphene.Int(),
        disability=graphene.String(),
        military=graphene.String(),
        citizenship=graphene.List(graphene.String),
        first_generation=graphene.Boolean(),
        financial_need=graphene.Boolean())

    # scholarship_by_user_criteria
    scholarships_by_user_criteria = graphene.Field(
        ScholarshipPaginationType,
        name=graphene.String(),
        start_deadline=graphene.Date(),
        end_deadline=graphene.Date(),
        status=graphene.String(),
        max_amount=graphene.List(graphene.Float),
        per_page=graphene.Int(),
        page=graphene.Int())

    # scholarship_status
    scholarship_status_by_fields = graphene.List(
        ScholarshipStatusType,
        user_id=graphene.Int(),
        scholarship_id=graphene.Int(),
        status=graphene.String())

    # get_all()
    def resolve_scholarship_max_amount(self, info):
        get_max = Scholarship.objects.aggregate(Max("max_amount"))
        _max = get_max['max_amount__max']
        return _max

    def resolve_providers(self, info, limit=None):
        qs = Provider.objects.all()[0:limit]
        return qs

    def resolve_scholarships(self, info, limit=None):
        qs = Scholarship.objects.all()[0:limit]
        return qs

    def resolve_scholarship_status(self, info, limit=None):
        qs = ScholarshipStatus.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_provider_by_fields(self, info, **fields):
        qs = Provider.objects.filter(**fields)
        return qs


    def resolve_scholarship_by_fields(self, info, **fields):
        qs = Scholarship.objects.filter(**fields)
        return qs

    def resolve_scholarship_status_by_fields(self, info, **fields):
        qs = ScholarshipStatus.objects.filter(**fields)
        return qs


class CreateProvider(graphene.Mutation):
    provider = graphene.Field(ScholarshipProviderType)

    class Arguments:
        organization = graphene.String()
        addressee = graphene.String()
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
        organization=None,
        addressee=None,
        address=None,
        city=None,
        state=None,
        zipcode=None,
        email=None,
        phone_number=None,
        phone_number_ext=None,
    ):

        provider = Provider(
            organization=organization,
            addressee=addressee,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            email=email,
            phone_number=phone_number,
            phone_number_ext=phone_number_ext)
        provider.save()

        return CreateProvider(provider=provider)


class CreateScholarship(graphene.Mutation):
    scholarship = graphene.Field(ScholarshipType)

    class Arguments:
        name = graphene.String()
        provider_id = graphene.Int()
        college_id = graphene.Int()
        description = graphene.String()
        website = graphene.String()
        max_amount = graphene.Int()
        deadline = graphene.Date()
        renewable = graphene.Boolean()
        number_awards = graphene.Int()
        education_level = graphene.List(graphene.String)
        education_requirements = graphene.String()
        area_of_study = graphene.List(graphene.String)
        area_of_study_description = graphene.String()
        writing_competition = graphene.Boolean()
        interest_description = graphene.String()
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
        provider_id=None,
        college_id=None,
        description=None,
        website=None,
        deadline=None,
        max_amount=None,
        renewable=None,
        number_awards=None,
        education_level=None,
        education_requirements=None,
        area_of_study=None,
        area_of_study_description=None,
        writing_competition=None,
        interest_description=None,
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

        provider = Provider.objects.get(pk=provider_id)
        college = College.objects.get(pk=college_id)

        scholarship = Scholarship(
            name=name,
            provider=provider,
            college=college,
            description=description,
            website=website,
            max_amount=max_amount,
            deadline=deadline,
            renewable=renewable,
            number_awards=number_awards,
            education_level=education_level,
            education_requirements=education_requirements,
            area_of_study=area_of_study,
            area_of_study_description=area_of_study_description,
            writing_competition=writing_competition,
            interest_description=interest_description,
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
            financial_need=financial_need)
        scholarship.save()

        return CreateScholarship(scholarship=scholarship)

class CreateOrUpdateScholarshipStatus(graphene.Mutation):
    scholarship_status = graphene.Field(ScholarshipStatusType)

    class Arguments:
        scholarship_id = graphene.Int()
        status = graphene.String()

    def mutate(
        self,
        info,
        user_id=None,
        scholarship_id=None,
        status=None
    ):

        user = info.context.user
        scholarship = Scholarship.objects.get(pk=scholarship_id)
        scholarshipStatus = ScholarshipStatus.objects.filter(user=user, scholarship=scholarship)

        if scholarshipStatus.count() > 0:
            scholarshipStatus = scholarshipStatus.get(user=user)
            scholarshipStatus.status = status
            scholarshipStatus.save()
        else:
            scholarshipStatus = ScholarshipStatus.objects.create(status=status)
            scholarshipStatus.user.add(user)
            scholarshipStatus.scholarship.add(scholarship)
            scholarshipStatus.save()

        return CreateOrUpdateScholarshipStatus(scholarship_status=scholarshipStatus)

class Mutation(graphene.ObjectType):
    create_provider = CreateProvider.Field()
    create_scholarship = CreateScholarship.Field()
    create_or_update_scholarship_status = CreateOrUpdateScholarshipStatus.Field()
