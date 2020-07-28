import graphene
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import BaseUserManager
from graphene_django import DjangoObjectType
from services.sendgrid.usecases import send_verfication, send_forgot_password


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
        if user.is_authenticated:
            return user


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_authenticated = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password):
        email = BaseUserManager.normalize_email(email)
        user = authenticate(username=email, password=password)

        if user is not None:
            login(info.context, user)
            return LoginUser(user=user, is_authenticated=user.is_authenticated)
        else:
            raise Exception("Incorrect credentials")


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(
        self,
        info,
        email,
        password,
        first_name,
        last_name,
    ):
        user = get_user_model()(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
        )
        user.set_password(password)
        user.save()

        # send validation email
        send_verification(email, url, first_name)
        send_forgot_password(email, url, first_name)

        # login user after signup
        user = authenticate(username=email, password=password)
        login(info.context, user)

        return CreateUser(user=user)


class OnboardUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_score = graphene.Int()
        terms_and_conditions = graphene.Boolean()
        pronouns = graphene.String()
        ethnicity = graphene.String()
        user_type = graphene.String()
        highschool_graduation_year = graphene.Int()

    def mutate(
        self,
        info,
        id,
        gpa=None,
        act_score=None,
        sat_score=None,
        terms_and_conditions=None,
        pronouns=None,
        ethnicity=None,
        user_type=None,
        highschool_graduation_year=None
    ):
        user = get_user_model().objects.get(pk=id)

        if user is not None:
            user.gpa = gpa
            user.act_score = act_score
            user.sat_score = sat_score
            terms_and_conditions = terms_and_conditions
            pronouns = pronouns
            ethnicity = ethnicity
            user_type = user_type
            highschool_graduation_year = highschool_graduation_year
            user.save()
            return user
        else:
            raise Exception("User is not logged in")


class LogoutUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_logged_out: graphene.Boolean()

    def mutate(self, info):
        logout(info.context)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
    onboard_user = OnboardUser.Field()
    logout_user = LogoutUser.Field()
