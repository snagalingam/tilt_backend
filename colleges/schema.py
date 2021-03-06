import graphene
import json
import math
import os

from colleges.models import College, CollegeStatus, FieldOfStudy, Ipeds, Scorecard
from django.contrib.auth import get_user_model
from django.db.models import F, Max, Min, Q
from django.db.models.functions import Greatest, Least
from graphene_django import DjangoObjectType
from itertools import chain
from services.google.google_places import extract_photo_urls, GooglePlacesAPI
from services.helpers.fav_finder import get_favicon
from services.helpers.nearby_coordinates import check_by_city, check_by_coordinates, check_by_zipcode, check_distance


User = get_user_model()

################################################
# Standard Model Definitions
################################################
class CollegeType(DjangoObjectType):
    class Meta:
        model = College
        fields = "__all__"


class CollegeStatusType(DjangoObjectType):
    class Meta:
        model = CollegeStatus
        convert_choices_to_enum = False
        fields = "__all__"


class CollegeFieldOfStudyType(DjangoObjectType):
    class Meta:
        model = FieldOfStudy
        fields  = "__all__"


class CollegeIpedsType(DjangoObjectType):
    class Meta:
        model = Ipeds
        fields  = "__all__"


class CollegeScorecardType(DjangoObjectType):
    class Meta:
        model = Scorecard
        fields = "__all__"


################################################
# Queries
################################################
class CollegePaginationType(graphene.ObjectType):
    count = graphene.Int()
    pages = graphene.Int()
    search_results = graphene.List(CollegeType)


class NetPriceRangeType(graphene.ObjectType):
    max = graphene.Int()
    min = graphene.Int()


class Query(graphene.ObjectType):
    # standard queries
    college_statuses = graphene.List(
        CollegeStatusType,
        college_id=graphene.Int(),
        user_id=graphene.Int(),
        limit=graphene.Int()
    )
    college_statuses_by_id = graphene.Field(CollegeStatusType, id=graphene.Int())
    colleges = graphene.List(
        CollegeType, id=graphene.Int(), limit=graphene.Int())
    college_fields_of_study = graphene.List(
        CollegeFieldOfStudyType, college_id=graphene.Int())
    college_scorecards = graphene.List(
        CollegeScorecardType, limit=graphene.Int())

    # speicfic queries
    cities = graphene.List(CollegeScorecardType, city=graphene.String())
    college_by_id = graphene.Field(CollegeType, id=graphene.Int())
    colleges_by_popularity = graphene.List(CollegeType, limit=graphene.Int())
    filter_colleges = graphene.Field(
        CollegePaginationType,
        address=graphene.String(),
        admissions_rate=graphene.List(graphene.Float),
        city=graphene.String(),
        ethnicity=graphene.String(),
        gender=graphene.String(),
        income=graphene.String(),
        name=graphene.String(),
        net_price=graphene.List(graphene.Float),
        ownership=graphene.List(graphene.String),
        page=graphene.Int(),
        per_page=graphene.Int(),
        predominant_degree_awarded=graphene.List(graphene.String),
        program_type=graphene.String(),
        religious_affiliation=graphene.String(),
        sort_by=graphene.String(),
        sort_order=graphene.String(),
        state=graphene.String(),
        state_fips=graphene.String()
    )
    nearby_colleges = graphene.List(
        CollegeType,
        city=graphene.String(),
        lat=graphene.Float(),
        limit=graphene.Int(),
        lng=graphene.Float(),
        state=graphene.String(),
        zipcode=graphene.Int()
    )
    net_price_range = graphene.Field(
        NetPriceRangeType, income=graphene.String())
    religious_affiliation = graphene.List(CollegeScorecardType)
    state_fips = graphene.List(
        CollegeScorecardType, state_fip=graphene.String())
    states = graphene.List(CollegeScorecardType, state=graphene.String())
    my_colleges = graphene.List(CollegeStatusType)

    # standard model queries
    def resolve_college_statuses(self, info, limit=None, **kwargs):
        qs = CollegeStatus.objects.filter(**kwargs)[0:limit]
        return qs

    def resolve_college_statuses_by_id(self, info, id):
        qs = CollegeStatus.objects.get(id=id)
        return qs

    def resolve_my_colleges(self, info):
        user = info.context.user
        qs = CollegeStatus.objects.filter(user=user)
        return qs

    def resolve_colleges(self, info, limit=None, **kwargs):
        qs = College.objects.filter(show=True, **kwargs)[0:limit]
        return qs

    def resolve_college_fields_of_study(self, info, **kwargs):
        qs = FieldOfStudy.objects.filter(show=True, **kwargs)
        return qs

    def resolve_college_scorecards(self, info, limit=None):
        qs = Scorecard.objects.filter(show=True)[0:limit]
        return qs

    # speicfic queries
    def resolve_cities(self, info, city=""):
        qs = Scorecard.objects.filter(show=True, city__icontains=city)
        return qs

    def resolve_college_by_id(self, info, id):
        qs = College.objects.get(pk=id)
        return qs

    def resolve_colleges_by_popularity(self, info, limit=None):
        qs = College.objects.filter(show=True)
        qs = qs.order_by('-popularity_score')[0:limit]
        return qs

    def resolve_filter_colleges(
            self,
            info,
            address=None,
            admissions_rate=None,
            city=None,
            ethnicity=None,
            gender=None,
            income=None,
            name=None,
            net_price=None,
            ownership=None,
            page=1,
            per_page=12,
            predominant_degree_awarded=None,
            program_type=None,
            religious_affiliation=None,
            sort_by='name',
            sort_order='asc',
            state=None,
            state_fips=None
    ):
        qs = College.objects.filter(show=True)
        user = info.context.user
        income = user.income
        if name:
            qs = qs.filter(Q(scorecard__name__icontains=name) | Q(
                scorecard__alias__icontains=name) | Q(name__icontains=name))
        if address:
            qs = qs.filter(address__icontains=address)
        if city:
            city_state = city.split(", ")
            c = city_state[0]
            s = city_state[1]
            qs = qs.filter(scorecard__city__icontains=c).filter(
                scorecard__state__icontains=s)
        if state:
            qs = qs.filter(scorecard__state__icontains=state)
        if state_fips:
            qs = qs.filter(scorecard__state_fips__icontains=state_fips)
        if predominant_degree_awarded:
            qs = qs.filter(
                scorecard__predominant_degree_awarded__in=predominant_degree_awarded)
        if ownership:
            qs = qs.filter(scorecard__ownership__in=ownership)
        if admissions_rate:
            if (admissions_rate[1]) == 1:
                qs = qs.filter(Q(scorecard__admissions_rate__isnull=True) | Q(scorecard__admissions_rate__range=(
                    admissions_rate[0], admissions_rate[1])))
            else:
                qs = qs.filter(scorecard__admissions_rate__range=(
                    admissions_rate[0], admissions_rate[1]))
        if program_type:
            filter_type = f'scorecard__{program_type}__gte'
            qs = qs.filter(**{filter_type: 0.00001})
        if gender:
            filter_type = f'scorecard__{gender}'
            qs = qs.filter(**{filter_type: True})
        if ethnicity:
            filter_type = f'scorecard__{ethnicity}'
            qs = qs.filter(**{filter_type: True})
        if religious_affiliation:
            qs = qs.filter(
                scorecard__religious_affiliation__icontains=religious_affiliation)
        if net_price:
            if (income):
                income_filter_type = f'scorecard__avg_net_price_{income}__range'
                qs = qs.filter(Q(scorecard__avg_net_price__range=(net_price[0], net_price[1])) |
                               Q(**{income_filter_type: (net_price[0], net_price[1])}))
            else:
                qs = qs.filter(scorecard__avg_net_price__range=(
                    net_price[0], net_price[1]))

        if sort_by == "name":
            qs = qs.order_by(sort_by if sort_order == "asc" else f'-{sort_by}')
        if sort_by == "popularity_score":
            qs = qs.order_by('popularity_score' if sort_order ==
                             "asc" else '-popularity_score')
        if sort_by == "net_price":
            if (income is not None):
                if sort_order == 'asc':
                    qs = qs.annotate(real_net_price=Least('status__net_price',
                                                          'scorecard__avg_net_price', f'scorecard__avg_net_price_{income}')).order_by(F('real_net_price').asc(nulls_last=True))
                else:
                    qs = qs.annotate(real_net_price=Least('status__net_price',
                                                          'scorecard__avg_net_price', f'scorecard__avg_net_price_{income}')).order_by(F('real_net_price').desc(nulls_last=True))
            else:
                if sort_order == 'asc':
                    qs = qs.annotate(real_net_price=Least('status__net_price',
                                                          'scorecard__avg_net_price')).order_by(F('real_net_price').asc(nulls_last=True))
                else:
                    qs = qs.annotate(real_net_price=Least('status__net_price',
                                                          'scorecard__avg_net_price')).order_by(F('real_net_price').desc(nulls_last=True))
        if sort_by == "admissions_rate":
            if sort_order == 'asc':
                qs = qs.order_by(
                    F("scorecard__admissions_rate").asc(nulls_last=True))
            else:
                qs = qs.order_by(
                    F("scorecard__admissions_rate").desc(nulls_last=True))
        if sort_by == "city":
            qs = qs.order_by('scorecard__city' if sort_order ==
                             'asc' else '-scorecard__city')
        if sort_by == "state":
            qs = qs.order_by('scorecard__state_fips' if sort_order ==
                             'asc' else '-scorecard__state_fips')
        if sort_by == "ownership":
            qs = qs.order_by('scorecard__ownership' if sort_order ==
                             'asc' else '-scorecard__ownership')
        if sort_by == "predominant_degree_awarded":
            qs = qs.order_by(
                'scorecard__predominant_degree_awarded' if sort_order == 'asc' else '-scorecard__predominant_degree_awarded')

        count = qs.count()
        pages = math.ceil(count / per_page)
        start = (page - 1) * per_page
        end = start + per_page
        search_results = qs[start:end]
        return CollegePaginationType(search_results=search_results, pages=pages, count=count)

    def resolve_nearby_colleges(
        self,
        info,
        city=None,
        lat=None,
        limit=None,
        lng=None,
        state=None,
        zipcode=None
    ):
        data = []
        if zipcode:
            data = check_by_zipcode(zipcode)
        if city and state:
            data = check_by_city(city, state)
        if lat and lng:
            data = check_by_coordinates(lat, lng)

        state = data[0]
        user_lat = data[1]
        user_lng = data[2]
        degree = "Predominantly bachelor's-degree granting"

        # filter by state and degree
        qs = College.objects.filter(
            show=True,
            address__contains=state,
            scorecard__predominant_degree_awarded=degree)
        nearby_colleges = []

        # filter by coordinates within radius of 50 miles
        for college in qs:
            college_lat = college.lat
            college_lng = college.lng
            distance = check_distance(
                college_lat, college_lng, user_lat, user_lng)

            # 100 miles radius
            if distance <= 100:
                college.distance = round(distance, 5)
                nearby_colleges.append(college)

        sort_nearest = sorted(nearby_colleges, key=lambda x: x.distance)
        return sort_nearest[0:limit]

    def resolve_net_price_range(self, info):
        user = info.context.user
        income = user.income
        avg_net_price_min = Scorecard.objects.aggregate(Min("avg_net_price"))
        avg_net_price_max = Scorecard.objects.aggregate(Max("avg_net_price"))
        min = avg_net_price_min["avg_net_price__min"]
        max = avg_net_price_max["avg_net_price__max"]

        if min is not None and max is not None:
            if income:
                income_min = Scorecard.objects.aggregate(
                    Min(f"avg_net_price_{income}"))
                income_max = Scorecard.objects.aggregate(
                    Max(f"avg_net_price_{income}"))
                if min > income_min[f"avg_net_price_{income}__min"]:
                    min = income_min[f"avg_net_price_{income}__min"]
                if max < income_max[f"avg_net_price_{income}__max"]:
                    max = income_max[f"avg_net_price_{income}__max"]

            return NetPriceRangeType(min=min, max=max)
        else:
            return NetPriceRangeType(min=0, max=0)

    def resolve_religious_affiliation(self, info):
        qs = Scorecard.objects.filter(
            show=True, religious_affiliation__isnull=False).distinct("religious_affiliation")
        return qs

    def resolve_state_fips(self, info, state_fip=""):
        qs = Scorecard.objects.filter(
            show=True, state_fips__icontains=state_fip).distinct("state_fips")
        return qs

    def resolve_states(self, info, state=""):
        qs = Scorecard.objects.filter(
            show=True, state__icontains=state).distinct('state')
        return qs


################################################
# Mutations
################################################
class CreateOrUpdateCollegeBudget(graphene.Mutation):
    # send all fields to update the budget
    class Arguments:
        college_id = graphene.Int(required=True)
        family = graphene.Int()
        job = graphene.Int()
        loan_plus = graphene.Int()
        loan_private = graphene.Int()
        loan_school = graphene.Int()
        loan_subsidized = graphene.Int()
        loan_unsubsidized = graphene.Int()
        other_scholarships = graphene.Int()
        savings = graphene.Int()
        work_study = graphene.Int()

    college_status = graphene.Field(CollegeStatusType)

    def mutate(
        self,
        info,
        college_id=None,
        family=None,
        job=None,
        loan_plus=None,
        loan_private=None,
        loan_school=None,
        loan_subsidized=None,
        loan_unsubsidized=None,
        other_scholarships=None,
        savings=None,
        work_study=None
    ):
        user = info.context.user
        college = College.objects.get(pk=college_id)

        try:
            college_status = CollegeStatus.objects.get(
                college=college, user=user)
        except:
            college_status = None

        if college_status is None:
            college_status = CollegeStatus.objects.create(
                college=college,
                status="accepted",
                user=user,
            )

        college_status.family = family
        college_status.job = job
        college_status.loan_plus = loan_plus
        college_status.loan_private = loan_private
        college_status.loan_school = loan_school
        college_status.loan_subsidized = loan_subsidized
        college_status.loan_unsubsidized = loan_unsubsidized
        college_status.other_scholarships = other_scholarships
        college_status.savings = savings
        college_status.work_study = work_study
        college_status.save()

        return CreateOrUpdateCollegeBudget(college_status=college_status)


class CreateOrUpdateCollegeStatus(graphene.Mutation):
    class Arguments:
        college_id = graphene.Int(required=True)
        award_status = graphene.String()
        in_state_tuition = graphene.String()
        net_price = graphene.Int()
        residency = graphene.String()
        status = graphene.String()

    college_status = graphene.Field(CollegeStatusType)

    def mutate(
        self,
        info,
        college_id=None,
        award_status=None,
        in_state_tuition=None,
        net_price=None,
        residency=None,
        status=None
    ):
        user = info.context.user
        college = College.objects.get(pk=college_id)

        try:
            college_status = CollegeStatus.objects.get(
                user=user, college=college)

        except:
            college_status = None

        if college_status is None:
            if status != "not interested":
                college.popularity_score += 1
                college.save()

            college_status = CollegeStatus.objects.create(user=user)
            college_status.college = college

        else:
            # increase popularity score if change to interested
            if college_status.status == "not interested":
                if status != "not interested":
                    college.popularity_score += 1
                    college.save()

            # decrease popularity score if change to not interested
            elif college_status.status != "not interested":
                if status == "not interested":
                    college.popularity_score -= 1
                    college.save()

        if award_status is not None:
            college_status.award_status = award_status

        if in_state_tuition is not None:
            college_status.in_state_tuition = in_state_tuition

        if net_price is not None:
            college_status.net_price = net_price

        if residency is not None:
            college_status.residency = residency

        if status is not None:
            college_status.status = status

        college_status.save()
        return CreateOrUpdateCollegeStatus(college_status=college_status)


class Mutation(graphene.ObjectType):
    create_or_update_college_budget = CreateOrUpdateCollegeBudget.Field()
    create_or_update_college_status = CreateOrUpdateCollegeStatus.Field()
