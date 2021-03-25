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
    Field,
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
# Standard Model Definitions
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
        fields = ('id', 'education_category',
                  'education_detail', 'scholarship')


class ScholarshipFieldType(DjangoObjectType):
    class Meta:
        model = Field
        fields = ('id', 'category')


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
        fields = "__all__"


class ScholarshipPaginationType(graphene.ObjectType):
    count = graphene.Int()
    pages = graphene.Int()
    search_results = graphene.List(ScholarshipType)


class ScholarshipStatusType(DjangoObjectType):
    class Meta:
        model = ScholarshipStatus
        fields = "__all__"


class ScholarshipStateType(DjangoObjectType):
    class Meta:
        model = State
        fields = ('id', 'name', 'abbreviation')


################################################
# Query
################################################
class Query(graphene.ObjectType):
    # graphene type
    scholarship_by_id = graphene.Field(ScholarshipType, id=graphene.Int())
    scholarship_max_amount = graphene.Int()
    scholarships = graphene.List(ScholarshipType, limit=graphene.Int())
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

    # function definition
    def resolve_scholarship_by_id(self, info, id):
        scholarship = Scholarship.objects.get(pk=id)
        return scholarship

    def resolve_scholarship_max_amount(self, info):
        get_max = Scholarship.objects.aggregate(Max("max_amount"))
        _max = get_max['max_amount__max']
        return _max

    def resolve_scholarships(self, info, limit=None):
        qs = Scholarship.objects.all()[0:limit]
        return qs

    def resolve_scholarships_by_user_criteria(
        self,
        info,
        name=None,
        start_deadline=None,
        end_deadline=None,
        status=None,
        max_amount=None,
        per_page=None,
        page=None
    ):
        qs = Scholarship.objects.all()
        user = info.context.user

        if name:
            qs = qs.filter(Q(name__icontains=name) | Q(
                provider__organization__icontains=name))
        if start_deadline is not None and end_deadline is not None:
            qs = qs.filter(deadline__range=(start_deadline, end_deadline))

        if start_deadline is not None and end_deadline is None:
            qs = qs.filter(deadline=start_deadline)

        if status is not None:
            # status is not Noneindicates that a user wants to see their own scholarships
            qs = qs.filter(scholarshipstatus__user=user)
            if (status == "no status"):
                qs = qs.filter(scholarshipstatus__status__isnull=True)
            else:
                qs = qs.filter(scholarshipstatus__status=status)

        if max_amount:
            qs = qs.filter(max_amount__range=(max_amount[0], max_amount[1]))

        qs = qs.order_by('-created')
        count = qs.count()
        pages = math.ceil(count / per_page)
        start = (page - 1) * per_page
        end = start + per_page

        search_results = qs[start:end]
        return ScholarshipPaginationType(search_results=search_results, pages=pages, count=count)


################################################
# Mutations
################################################
class CreateOrUpdateScholarshipStatus(graphene.Mutation):
    class Arguments:
        scholarship_id = graphene.Int()
        status = graphene.String()

    scholarship_status = graphene.Field(ScholarshipStatusType)

    def mutate(self, info, scholarship_id=None, status=None):
        user = info.context.user
        scholarship = Scholarship.objects.get(pk=scholarship_id)

        try:
            scholarship_status = ScholarshipStatus.objects.get(
                user=user, scholarship=scholarship)
        except:
            scholarship_status = None

        if scholarship_status is None:
            scholarship_status = ScholarshipStatus.objects.create(user=user)
            scholarship_status.scholarship = scholarship

        scholarship_status.status = status
        scholarship_status.save()

        return CreateOrUpdateScholarshipStatus(scholarship_status=scholarship_status)


class Mutation(graphene.ObjectType):
    create_or_update_scholarship_status = CreateOrUpdateScholarshipStatus.Field()
