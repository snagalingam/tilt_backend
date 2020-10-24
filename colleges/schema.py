import graphene
import json
import math
import os
from graphene_django import DjangoObjectType
from services.google_api.google_places import GooglePlacesAPI, extract_photo_urls
from services.helpers.nearby_coordinates import check_distance, check_by_city, check_by_zipcode, check_by_coordinates
from services.helpers.fav_finder import get_favicon
from .models import College, FieldOfStudy, Scorecard
from django.db.models import Q, Max, Min
from itertools import chain


class CollegeType(DjangoObjectType):
    class Meta:
        model = College
        fields = "__all__"


class FieldOfStudyType(DjangoObjectType):
    class Meta:
        model = FieldOfStudy
        fields = "__all__"


class ScorecardType(DjangoObjectType):
    class Meta:
        model = Scorecard
        fields = "__all__"


class CollegePaginationType(graphene.ObjectType):
    count = graphene.Int()
    pages = graphene.Int()
    search_results = graphene.List(CollegeType)


class NetPriceRangeType(graphene.ObjectType):
    min = graphene.Int()
    max = graphene.Int()


class Query(graphene.ObjectType):
    colleges = graphene.List(CollegeType, limit=graphene.Int())
    scorecards = graphene.List(ScorecardType, limit=graphene.Int())
    field_of_studies = graphene.List(
        FieldOfStudyType, college_id=graphene.Int())
    colleges_by_popularity = graphene.List(CollegeType, limit=graphene.Int())
    college_by_id = graphene.Field(
        CollegeType, id=graphene.Int())
    college_by_unit_id = graphene.Field(
        CollegeType, unit_id=graphene.String())
    college_by_ope_id = graphene.Field(
        CollegeType, ope_id=graphene.String())
    college_by_name = graphene.List(
        CollegeType, name=graphene.String())
    nearby_colleges = graphene.List(
        CollegeType,
        lat=graphene.Float(),
        lng=graphene.Float(),
        zipcode=graphene.Int(),
        city=graphene.String(),
        state=graphene.String(),
        limit=graphene.Int()
    )
    filter_colleges = graphene.Field(
        CollegePaginationType,
        name=graphene.String(),
        address=graphene.String(),
        per_page=graphene.Int(),
        page=graphene.Int(),
        sort_by=graphene.String(),
        sort_order=graphene.String(),
        city=graphene.String(),
        state=graphene.String(),
        state_fips=graphene.String(),
        predominant_degree_awarded=graphene.String(),
        ownership=graphene.String(),
        admissions_rate=graphene.List(graphene.Float),
        program_type=graphene.String(),
        gender=graphene.String(),
        ethnicity=graphene.String(),
        religious_affiliation=graphene.String(),
        net_price=graphene.List(graphene.Float),
        income_quintile=graphene.String()
    )
    state_fips = graphene.List(ScorecardType, state_fip=graphene.String())
    states = graphene.List(ScorecardType, state=graphene.String())
    cities = graphene.List(ScorecardType, city=graphene.String())
    net_price_range = graphene.Field(NetPriceRangeType)
    religious_affiliation = graphene.List(ScorecardType)

    def resolve_religious_affiliation(self, info):
        qs = Scorecard.objects.filter(
            religious_affiliation__isnull=False).distinct("religious_affiliation")
        return qs

    def resolve_state_fips(self, info, state_fip=""):
        qs = Scorecard.objects.filter(
            state_fips__icontains=state_fip).distinct("state_fips")
        return qs

    def resolve_states(self, info, state=""):
        qs = Scorecard.objects.filter(
            state__icontains=state).distinct('state')
        return qs

    def resolve_cities(self, info, city=""):
        qs = Scorecard.objects.filter(city__icontains=city)
        return qs

    def resolve_net_price_range(self, info):
        min = Scorecard.objects.aggregate(Min("avg_net_price"))
        max = Scorecard.objects.aggregate(Max("avg_net_price"))
        return NetPriceRangeType(min=min["avg_net_price__min"], max=max["avg_net_price__max"])

    def resolve_filter_colleges(
            self,
            info,
            name=None,
            address=None,
            per_page=12,
            page=1,
            sort_by='name',
            sort_order='asc',
            city=None,
            state=None,
            state_fips=None,
            predominant_degree_awarded=None,
            ownership=None,
            admissions_rate=None,
            program_type=None,
            gender=None,
            ethnicity=None,
            religious_affiliation=None,
            net_price=None,
            income_quintile=None
    ):
        qs = College.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
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
                scorecard__predominant_degree_awarded__icontains=predominant_degree_awarded)
        if ownership:
            qs = qs.filter(scorecard__ownership__icontains=ownership)
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
            if (income_quintile):
                income_filter_type = f'scorecard__avg_net_price_{income_quintile}__range'
                qs = qs.filter(Q(scorecard__avg_net_price__range=(net_price[0], net_price[1])) |
                               Q(**{income_filter_type: (net_price[0], net_price[1])}))
            else:
                qs = qs.filter(scorecard__avg_net_price__range=(
                    net_price[0], net_price[1]))

        if sort_by == "name":
            qs = qs.order_by(sort_by if sort_order == "asc" else f'-{sort_by}')

        count = qs.count()
        pages = math.ceil(count / per_page)
        start = (page - 1) * per_page
        end = start + per_page
        search_results = qs[start:end]
        # print(search_results.explain(verbose=True, analyze=True))
        return CollegePaginationType(search_results=search_results, pages=pages, count=count)

    def resolve_colleges(self, info, limit=None):
        return College.objects.all()[0:limit]

    def resolve_scorecards(self, info, limit=None):
        return Scorecard.objects.all()[0:limit]

    def resolve_field_of_studies(self, info, college_id):
        return FieldOfStudy.objects.filter(college=college_id,
                                           num_students_ipeds_awards2__isnull=False)

    def resolve_colleges_by_popularity(self, info, limit=None):
        return College.objects.order_by('-popularity_score')[0:limit]

    def resolve_college_by_id(root, info, id):
        return College.objects.get(pk=id)

    def resolve_college_by_unit_id(root, info, unit_id):
        return College.objects.get(unit_id=unit_id)

    def resolve_college_by_ope_id(root, info, ope_id):
        return College.objects.get(ope_id=ope_id)

    def resolve_college_by_name(root, info, name):
        return College.objects.filter(name=name)

    def resolve_nearby_colleges(
            root,
            info,
            lat=None,
            lng=None,
            zipcode=None,
            city=None,
            state=None,
            limit=None
    ):

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
            address__contains=state,
            scorecard__predominant_degree_awarded=degree)[0:limit]
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
        return sort_nearest


class CreateCollege(graphene.Mutation):
    college = graphene.Field(CollegeType)

    class Arguments:
        unit_id = graphene.Int()
        ope_id = graphene.Int()
        place_id = graphene.String()
        business_status = graphene.String()
        name = graphene.String()
        lat = graphene.Float()
        lng = graphene.Float()
        address = graphene.String()
        phone_number = graphene.String()
        url = graphene.String()
        website = graphene.String()
        favicon = graphene.String()
        main_photo = graphene.String()
        photos = graphene.List(graphene.String)
        types = graphene.List(graphene.String)

    def mutate(
        self,
        info,
        unit_id=None,
        ope_id=None,
        place_id=None,
        business_status=None,
        name=None,
        lat=None,
        lng=None,
        address=None,
        phone_number=None,
        url=None,
        website=None,
        favicon=None,
        main_photo=None,
        photos=None,
        types=None,
    ):

        try:
            college = College.objects.get(unit_id=unit_id)
        except College.DoesNotExist:
            college = None

        if college is None:
            college = College(
                unit_id=unit_id,
                ope_id=ope_id,
                place_id=place_id,
                business_status=business_status,
                name=name,
                lat=lat,
                lng=lng,
                address=address,
                phone_number=phone_number,
                url=url,
                website=website,
                favicon=favicon,
                main_photo=main_photo,
                photos=photos,
                types=types,
            )
            college.save()
            return CreateCollege(college=college)
        else:
            return CreateCollege(college=college)


class CollegeSearch(graphene.Mutation):
    college = graphene.Field(CollegeType)

    class Arguments:
        place = graphene.String()
        location = graphene.String()

    def mutate(self, info, place, location):
        api = GooglePlacesAPI()
        data = api.details(place, location)

        try:
            if data["errors"] is not None:
                return ValueError(data["errors"])

        except:
            results = data['result']

            photos_result = results.get("photos", "")
            if photos_result != "":
                photo_arr = extract_photo_urls(photos_result)
                main_photo = photo_arr[0]
                photos = photo_arr
            else:
                main_photo = ""
                photos = []

            website = results.get('website', "")
            try:
                favicon = get_favicon(website)
            except:
                favicon = ""

            place_id = data['place_id']
            business_status = results.get('business_status', "")
            name = results.get('name', "")
            lat = data["result"]["geometry"]["location"]["lat"]
            lng = data["result"]["geometry"]["location"]["lng"]
            address = results.get('formatted_address', "")
            phone_number = results.get('formatted_phone_number', "")
            url = results.get('url', "")
            types = results.get('types', [])

            college = College(
                place_id=place_id,
                business_status=business_status,
                name=name,
                lat=lat,
                lng=lng,
                address=address,
                phone_number=phone_number,
                url=url,
                website=website,
                favicon=favicon,
                main_photo=main_photo,
                photos=photos,
                types=types,
            )

            return CollegeSearch(college=college)


class Mutation(graphene.ObjectType):
    create_college = CreateCollege.Field()
    college_search = CollegeSearch.Field()
