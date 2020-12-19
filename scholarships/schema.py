import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from .models import Provider, Scholarship, Status
from colleges.models import College
import datetime

class ProviderType(DjangoObjectType):
    class Meta:
        model = Provider

class ScholarshipType(DjangoObjectType):
    class Meta:
        model = Scholarship

class StatusType(DjangoObjectType):
    class Meta:
        model = Status

class Query(graphene.ObjectType):
    providers = graphene.List(ProviderType, limit=graphene.Int())
    scholarships = graphene.List(ScholarshipType, limit=graphene.Int())
    scholarship_statuses = graphene.List(StatusType, limit=graphene.Int())

    # providers
    providers_by_fields = graphene.List(
        ProviderType, 
        organization=graphene.String(),
        reference=graphene.String(),
        address=graphene.String(),
        city=graphene.String(),
        state=graphene.String(),
        zipcode=graphene.String(),
        email=graphene.String(),
        phone_number=graphene.String(),
        phone_number_ext=graphene.String())

    # scholarships
    scholarships_by_fields = graphene.List(
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
    scholarships_by_user_criteria = graphene.List(ScholarshipType)

    # scholarship_statuses
    scholarship_statuses_by_fields = graphene.List(
        StatusType, 
        user_id=graphene.Int(),
        scholarship_id=graphene.Int(),
        status=graphene.String())

    # get_all()
    def resolve_providers(self, info, limit=None):
        qs = Provider.objects.all()[0:limit]
        return qs

    def resolve_scholarships(self, info, limit=None):
        qs = Scholarship.objects.all()[0:limit]
        return qs

    def resolve_scholarship_statuses(self, info, limit=None):
        qs = Status.objects.all()[0:limit]
        return qs

    # get_by_fields()
    def resolve_providers_by_fields(self, info, **fields):
        qs = Provider.objects.filter(**fields)
        return qs

    def resolve_scholarships_by_fields(self, info, **fields):
        qs = Scholarship.objects.filter(**fields)
        return qs

    def resolve_scholarship_statuses_by_fields(self, info, **fields):
        qs = Status.objects.filter(**fields)
        return qs

#     def resolve_scholarships_by_user_criteria(self, info):
#         qs = Scholarship.objects.all()
#         user = info.context.user

# #------ find education level 
#         current_date = datetime.datetime.today()
#         education_level = "college_student"

#         # if highschool grad year is less than current year 
#         if current_date.year - user.high_school_grad_year < 0:
#             education_level = "highschool_senior"

#         # if highschool grad year is current year but today is earlier than may
#         elif current_date.year - user.high_school_grad_year == 0:
#             if current_date.month < 6:
#                 education_level = "highschool_senior"

# #------ find state from organization address
#         us_states = [
#             "AL",
#             "AK",
#             "AZ",
#             "AR",
#             "CA",
#             "CO",
#             "CT",
#             "DE",
#             "DC",
#             "FL",
#             "GA",
#             "HI",
#             "ID",
#             "IL",
#             "IN",
#             "IA",
#             "KS",
#             "KY",
#             "LA",
#             "ME",
#             "MD",
#             "MA",
#             "MI",
#             "MN",
#             "MS",
#             "MO",
#             "MT",
#             "NE",
#             "NV",
#             "NH",
#             "NJ",
#             "NM",
#             "NY",
#             "NC",
#             "ND",
#             "OH",
#             "OK",
#             "OR",
#             "PA",
#             "RI",
#             "SC",
#             "SD",
#             "TN",
#             "TX",
#             "UT",
#             "VT",
#             "VA",
#             "WA",
#             "WV",
#             "WI",
#             "WY"]

#         organization_address = user.organization.values()[0]["address"]
#         split_address = organization_address.split(" ")

#         for each in split_address:
#             if "," in each:
#                 each = each.replace(",", "")
#             if each in us_states:
#                 state = each

# #------ find ethnicity   
#         ethnicities = [
#             "american indian and alaska native",
#             "asian",
#             "black and african",
#             "hispanic and latinx",
#             "native hawaiian and pacific islander",
#             "white",
#             "other",
#         ]

#         ethnicity = user.ethnicity[0]
#         # multi_ethnic = []

#         # if len(user.ethnicity) > 1:
#         #     for i in range(len(user.ethnicity)):

#         #         ethnicity = user.ethnicity

# #------ find gender   
#         genders = {
#             "He/his": "men",
#             "She/hers": "women",
#             "They/theirs": "other"
#         }
#         gender = genders[user.pronouns]

# #------ find gpa and test scores  
#         user_gpa = user.gpa
#         user_sat = user.sat_math + user.sat_verbal
#         user_act = user.act_score

#         if education_level == "highschool_senior":
#             pass

#         if education_level == "college_student":
#             pass

#         qs = qs.filter()
#         # min_gpa =
#         # max_gpa =
#         # min_act = 
#         # min_sat = 

#         breakpoint()
#         return qs


class CreateProvider(graphene.Mutation):
    provider = graphene.Field(ProviderType)

    class Arguments:
        organization=graphene.String()
        reference=graphene.String()
        address=graphene.String()
        city=graphene.String()
        state=graphene.String()
        zipcode=graphene.String()
        email=graphene.String()
        phone_number=graphene.String()
        phone_number_ext=graphene.String()

    def mutate(
        self,
        info,
        organization=None,
        reference=None,
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
            reference=reference,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            email=email,
            phone_number=phone_number,
            phone_number_ext=phone_number_ext,
        )
        provider.save()

        return CreateProvider(provider=provider)


class CreateScholarship(graphene.Mutation):
    scholarship = graphene.Field(ScholarshipType)

    class Arguments:
        name = graphene.String()
        provider_id = graphene.Int()
        description = graphene.String()
        website = graphene.String()
        deadline=graphene.Date()
        max_amount = graphene.Int()
        deadline=graphene.Date()
        renewable = graphene.Boolean()
        number_awards = graphene.Int()
        education_level = graphene.List(graphene.String)
        education_requirements = graphene.String()
        area_of_study = graphene.List(graphene.String)
        area_of_study_description = graphene.String()
        writing_competition = graphene.Boolean()
        interest_description = graphene.String()
        college_id = graphene.Int()
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
        college_id=None,
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
            description=description,
            website=website,
            deadline=deadline,
            max_amount=max_amount,
            renewable=renewable,
            number_awards=number_awards,
            education_level=education_level,
            education_requirements=education_requirements,
            area_of_study=area_of_study,
            area_of_study_description=area_of_study_description,
            writing_competition=writing_competition,
            interest_description=interest_description,
            college=college,
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
            financial_need=financial_need
        )
        scholarship.save()

        return CreateScholarship(scholarship=scholarship)

class CreateStatus(graphene.Mutation):
    scholarship_status = graphene.Field(StatusType)

    class Arguments:
        user_id = graphene.Int()
        scholarship_id = graphene.Int()
        status = graphene.String()

    def mutate(
        self,
        info,
        user_id=None,
        scholarship_id=None,
        status=None
    ):
        
        user = get_user_model().objects.get(pk=user_id)
        scholarship = Scholarship.objects.get(pk=scholarship_id)

        scholarship_status = Provider(
            user=user,
            scholarship=scholarship,
            status=status,
        )
        scholarship_status.save()

        return CreateStatus(scholarship_status=scholarship_status)

class Mutation(graphene.ObjectType):
    create_provider = CreateProvider.Field()
    create_scholarship = CreateScholarship.Field()
    create_scholarship_status = CreateStatus.Field()
