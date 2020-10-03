import graphene
import json
import math
import os
from graphene_django import DjangoObjectType
from services.google_api.google_places import GooglePlacesAPI, extract_photo_urls
from services.helpers.fav_finder import get_favicon
from .models import College


class CollegeType(DjangoObjectType):
    class Meta:
        model = College
        fields = "__all__"


class CollegePaginationType(graphene.ObjectType):
    count = graphene.Int()
    pages = graphene.Int()
    search_results = graphene.List(CollegeType)


class Query(graphene.ObjectType):
    colleges = graphene.List(CollegeType, limit=graphene.Int())
    colleges_by_popularity = graphene.List(CollegeType, limit=graphene.Int())
    college_by_id = graphene.Field(
        CollegeType, id=graphene.Int())
    college_by_unit_id = graphene.Field(
        CollegeType, unit_id=graphene.String())
    college_by_ope_id = graphene.Field(
        CollegeType, ope_id=graphene.String())
    college_by_name = graphene.List(
        CollegeType, name=graphene.String())
    filter_colleges = graphene.Field(
        CollegePaginationType,
        name=graphene.String(),
        address=graphene.String(),
        per_page=graphene.Int(),
        page=graphene.Int(),
        sort_by=graphene.String(),
        sort_order=graphene.String()
    )

    def resolve_filter_colleges(
            self,
            info,
            name=None,
            address=None,
            per_page=12,
            page=1,
            sort_by='name',
            sort_order='asc'
    ):
        qs = College.objects.all()
        if name:
            qs = qs.filter(name__icontains=name)
        if address:
            qs = qs.filter(address__icontains=address)

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
