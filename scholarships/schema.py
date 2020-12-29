import datetime
import graphene
import math

from colleges.models import College
from django.contrib.auth import get_user_model
from django.db.models import Q, Max, Min, F
from graphene_django import DjangoObjectType
from scholarships.models import (
    Association,
    Citizenship,
    Degree,
    Disability,
    EducationCategory,
    EducationDetail,
    EducationScholarship,
    FieldCategory,
    FieldDetail,
    FieldScholarship,
    Gender,
    Heritage,
    Interest,
    LocationDetail,
    LocationScholarship,
    Military,
    Provider,
    Scholarship,
    ScholarshipStatus,
    State
)


################################################
### Standard Model Definitions
################################################
class ScholarshipAssociationType(DjangoObjectType):
    class Meta:
        model = Association
        fields = ('id', 'name')


class ScholarshipCitizenshipType(DjangoObjectType):
    class Meta:
        model = Citizenship
        fields = ('id', 'category')


class ScholarshipDegreeType(DjangoObjectType):
    class Meta:
        model = Degree
        fields = ('id', 'category')


class ScholarshipDisabilityType(DjangoObjectType):
    class Meta:
        model = Disability
        fields = ('id', 'category')


class ScholarshipEducationCategoryType(DjangoObjectType):
    class Meta:
        model = EducationCategory
        fields = ('id', 'category')


class ScholarshipEducationDetailType(DjangoObjectType):
    class Meta:
        model = EducationDetail
        fields = ('id', 'description')


class ScholarshipEducationScholarshipType(DjangoObjectType):
    class Meta:
        model = EducationScholarship
        fields = ('id', 'education_category', 'education_detail', 'scholarship')


class ScholarshipFieldCategoryType(DjangoObjectType):
    class Meta:
        model = FieldCategory
        fields = ('id', 'category')


class ScholarshipFieldDetailType(DjangoObjectType):
    class Meta:
        model = FieldDetail
        fields = ('id', 'description')


class ScholarshipFieldScholarshipType(DjangoObjectType):
    class Meta:
        model = FieldScholarship
        fields = ('id', 'field_category', 'field_detail', 'scholarship')


class ScholarshipGenderType(DjangoObjectType):
    class Meta:
        model = Gender
        fields = ('id', 'category')


class ScholarshipHeritageType(DjangoObjectType):
    class Meta:
        model = Heritage
        fields = ('id', 'category')


class ScholarshipInterestType(DjangoObjectType):
    class Meta:
        model = Interest
        fields = ('id', 'category')


class ScholarshipLocationDetailType(DjangoObjectType):
    class Meta:
        model = LocationDetail
        fields = ('id', 'description')


class ScholarshipLocationScholarshipType(DjangoObjectType):
    class Meta:
        model = LocationScholarship
        fields = ('id', 'location_detail', 'scholarship', 'state',)


class ScholarshipMilitaryType(DjangoObjectType):
    class Meta:
        model = Military
        fields = ('id', 'category')


class ScholarshipProviderType(DjangoObjectType):
    class Meta:
        model = Provider
        fields = (
            'id',
            'addressee',
            'city',
            'email',
            'phone_number',
            'phone_number_ext',
            'organization',
            'state',
            'street',
            'zipcode'
        )


class ScholarshipType(DjangoObjectType):
    class Meta:
        model = Scholarship
        fields = (
            # scholarship details
            'id',
            'name',
            'deadline',
            'description',
            'max_amount',
            'number_awards',
            'provider',
            'renewable',
            'website',
            # requirements
            'association_set',
            'citizenship_set',
            'college_set',
            'degree_set',
            'disability_set',
            'financial_need',
            'first_generation',
            'gender_set',
            'heritage_set',
            'interest_set',
            'military_set',
            'min_act',
            'min_gpa',
            'min_sat',
            'max_gpa',
            'writing'
        )


class ScholarshipPaginationType(graphene.ObjectType):
    count = graphene.Int()
    pages = graphene.Int()
    search_results = graphene.List(ScholarshipType)


class ScholarshipStatusType(DjangoObjectType):
    class Meta:
        model = ScholarshipStatus
        fields = ('id', 'user', 'scholarship', 'status')


class ScholarshipStateType(DjangoObjectType):
    class Meta:
        model = State
        fields = ('id', 'name', 'abbreviation')


################################################
### Query
################################################
class Query(graphene.ObjectType):
    scholarship_providers = graphene.List(ScholarshipProviderType, limit=graphene.Int())
    scholarship_statuses = graphene.List(ScholarshipStatusType, limit=graphene.Int())
    scholarships = graphene.List(ScholarshipType, limit=graphene.Int())

    # providers
    scholarship_providers_by_fields = graphene.List(
        ScholarshipProviderType,
        addressee=graphene.String(),
        city=graphene.String(),
        email=graphene.String(),
        organization=graphene.String(),
        phone_number=graphene.String(),
        phone_number_ext=graphene.String(),
        state=graphene.ID(),
        street=graphene.String(),
        zipcode=graphene.String()
    )

    # scholarships
    scholarships_by_fields = graphene.List(
        ScholarshipType,
        # contact
        name=graphene.String(),
        deadline=graphene.Date(),
        description=graphene.String(),
        max_amount=graphene.Int(),
        number_awards=graphene.Int(),
        provider=graphene.ID(),
        renewable=graphene.Boolean(),
        website=graphene.String(),
        association=graphene.ID(),
        citizenship=graphene.ID(),
        college=graphene.ID(),
        degree=graphene.ID(),
        disability=graphene.ID(),
        financial_need=graphene.Boolean(),
        first_generation=graphene.Boolean(),
        gender=graphene.ID(),
        heritage=graphene.ID(),
        interest=graphene.ID(),
        military=graphene.ID(),
        min_act=graphene.Int(),
        min_gpa=graphene.Float(),
        min_sat=graphene.Int(),
        max_gpa=graphene.Float(),
        writing=graphene.Boolean()
    )
    scholarships_by_user_criteria = graphene.Field(
        ScholarshipPaginationType,
        end_deadline=graphene.Date(),
        max_amount=graphene.List(graphene.Float),
        page=graphene.Int(),
        per_page=graphene.Int(),
        name=graphene.String(),
        start_deadline=graphene.Date(),
        status=graphene.String()
    )
    scholarship_max_amount = graphene.Int()

    # scholarship status
    scholarship_statuses_by_fields = graphene.List(
        ScholarshipStatusType,
        scholarship=graphene.ID(),
        status=graphene.String(),
        user=graphene.ID()
    )

    # get_all()
    def resolve_scholarship_max_amount(self, info):
        get_max = Scholarship.objects.aggregate(Max("max_amount"))
        _max = get_max['max_amount__max']
        return _max

    def resolve_scholarship_providers(self, info, limit=None):
        qs = Provider.objects.all()[0:limit]
        return qs

    def resolve_scholarships(self, info, limit=None):
        qs = Scholarship.objects.all()[0:limit]
        return qs

    def resolve_scholarship_statuses(self, info, limit=None):
        qs = ScholarshipStatus.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_scholarship_providers_by_fields(self, info, **kwargs):
        qs = Provider.objects.filter(**kwargs)
        return qs

    def resolve_scholarships_by_fields(self, info, **kwargs):
        qs = Scholarship.objects.filter(**kwargs)
        return qs

    def resolve_scholarship_statuses_by_fields(self, info, **kwargs):
        qs = ScholarshipStatus.objects.filter(**kwargs)
        return qs


################################################
### Mutations
################################################
class CreateOrUpdateScholarshipStatus(graphene.Mutation):
    class Arguments:
        scholarship_id = graphene.Int()
        status = graphene.String()

    scholarship_status = graphene.Field(ScholarshipStatusType)

    def mutate(self,info, scholarship_id=None, status=None, user_id=None):
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
    create_or_update_scholarship_status = CreateOrUpdateScholarshipStatus.Field()
