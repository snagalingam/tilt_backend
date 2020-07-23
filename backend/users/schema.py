import graphene
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import BaseUserManager
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password, next_url="/"):
        email = BaseUserManager.normalize_email(email)
        user = authenticate(username=email, password=password)

        if user is not None:
            login(info.context, user)
            return LoginUser(user=user)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_score = graphene.Int()
        efc = graphene.Int()
        terms_and_conditions = graphene.Boolean()
        pronouns = graphene.String()
        pronouns_other_value = graphene.String()
        ethnicity = graphene.String()
        ethnicity_other_value = graphene.String()
        user_type = graphene.String()
        highschool_graduation_year = graphene.String()

    def mutate(
        self,
        info,
        email,
        password,
        first_name,
        last_name,
        preferred_name,
        gpa,
        act_score,
        sat_score,
        efc,
        terms_and_conditions,
        pronouns,
        pronouns_other_value,
        ethnicity,
        ethnicity_other_value,
        user_type,
        highschool_graduation_year,
    ):
        user = get_user_model()(
            email=email,
            first_name=first_name,
            last_name=last_name,
            preferred_name=preferred_name,
            gpa=gpa,
            act_score=act_score,
            sat_score=sat_score,
            efc=efc,
            terms_and_conditions=terms_and_conditions,
            pronouns=pronouns,
            pronouns_other_value=pronouns_other_value,
            ethnicity=ethnicity,
            ethnicity_other_value=ethnicity_other_value,
            user_type=user_type,
            highschool_graduation_year=highschool_graduation_year,
            is_staff=False,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
