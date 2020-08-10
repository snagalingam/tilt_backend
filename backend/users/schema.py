import graphene
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import BaseUserManager
from graphene_django import DjangoObjectType
from django.shortcuts import redirect
from .send_emails import *


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

        if user.is_verified: 
            if user is not None:
                login(info.context, user)
                return LoginUser(user=user, is_authenticated=user.is_authenticated)
            else:
                raise Exception("Incorrect credentials")
        else:
            raise Exception("Email is not verifed")


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

        # send email verification user after signup
        send_verification(user.email, user.first_name)

        # login user after signup
        user = authenticate(username=email, password=password)
        login(info.context, user)

        return CreateUser(user=user)


class OnboardUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        id = graphene.ID()
        last_name = graphene.String()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_score = graphene.Int()
        efc = graphene.Int()
        terms_and_conditions = graphene.Boolean()
        pronouns = graphene.String()
        ethnicity = graphene.String()
        user_type = graphene.String()
        high_school_grad_year = graphene.Int()
        income_quintile = graphene.String()
        found_from = graphene.List(graphene.String)

    def mutate(
        self,
        info,
        id,
        last_name=None,
        preferred_name=None,
        gpa=None,
        act_score=None,
        sat_score=None,
        efc=None,
        terms_and_conditions=False,
        pronouns=None,
        ethnicity=None,
        user_type=None,
        high_school_grad_year=None,
        income_quintile=None,
        found_from=None
    ):
        user = get_user_model().objects.get(pk=id)

        if user is not None:
            user.last_name = last_name
            user.preferred_name = preferred_name
            user.gpa = gpa
            user.act_score = act_score
            user.sat_score = sat_score
            user.efc = efc
            user.terms_and_conditions = terms_and_conditions
            user.pronouns = pronouns
            user.ethnicity = ethnicity
            user.user_type = user_type
            user.high_school_grad_year = high_school_grad_year
            user.income_quintile = income_quintile
            user.found_from = found_from
            user.save()
            return OnboardUser(user=user)
        else:
            raise Exception("User is not logged in")


class LogoutUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_logged_out: graphene.Boolean()

    def mutate(self, info):
        logout(info.context)

class VerifyEmail(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        token = graphene.String(required=True)
    
    def mutate(self, info, token):
        domain = os.environ.get('DOMAIN')
        email = jwt.decode(token, 
                           os.environ.get('SECRET_KEY'), 
                           algorithms=['HS256'])['email']

        user = get_user_model().objects.get(email=email)

        if email and not user.is_verified:
            user.is_verified = True
            user.save()
            login(info.context, user)
            return redirect(f"{domain}/dashboard/")

class SendForgotEmail(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(self, info, email):
        email = BaseUserManager.normalize_email(email)
        user = get_user_model().objects.get(email=email)

        if user.is_verified: 
            send_reset_password(user.email, user.first_name)
            return SendForgotEmail(success=True)
        else:
            raise Exception("Email not found")


class ResetPassword(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        password_repeat = graphene.String()
        token = graphene.String(required=True)

    def mutate(self, info, token, email, password, password_repeat):
        user = get_user_model().objects.get(email=email)
        domain = os.environ.get('DOMAIN')
        email = jwt.decode(token,
                           os.environ.get('SECRET_KEY'),
                           algorithms=['HS256'])['email']

        if email == user.email and password == password_repeat:
            user.set_password(password)
            user.save()
            return ResetPassword(success=True)
        elif password != password_repeat:
            raise Exception("Passwords do not match")
        else:
            raise Exception("Password did not reset")


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
    onboard_user = OnboardUser.Field()
    logout_user = LogoutUser.Field()
    verify_email = VerifyEmail.Field()
    send_forgot_email = SendForgotEmail.Field()
    reset_password = ResetPassword.Field()
