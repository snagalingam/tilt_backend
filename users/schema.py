import graphene
import graphql_social_auth
import jwt
import os
import requests

from django.contrib.auth import get_user_model, authenticate, login, logout, password_validation
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError

from graphene_django import DjangoObjectType
from django.shortcuts import redirect
from urllib.parse import urlencode, urlparse, parse_qsl
from organizations.models import Organization
from services.sendgrid_api.send_email import send_verification, send_reset_password
from services.sendgrid_api.add_subscriber_email import add_subscriber


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class OrganizationT(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"


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
            if user.social_auth.exists():
                return user
            if user.is_verified:
                return user
            else:
                raise Exception("User is not verified")


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_authenticated = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        user = authenticate(username=email, password=password)

        if user is not None:
            if (user.is_verified):
                login(info.context, user)
                return LoginUser(user=user, is_authenticated=user.is_authenticated)
            else:
                raise Exception("User is not verified")
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
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        user = get_user_model()(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
        )

        try: 
            password_validation.validate_password(password, user=user)
        except ValidationError as e:
            return e
        
        user.set_password(password)
        user.save()

        # send email verification user after signup
        send_verification(user.email, user.first_name)

        if user is not None:
            return CreateUser(user=user)
        else:
            raise Exception("Unable to create user")


class OnboardUser(graphene.Mutation):
    user = graphene.Field(UserType)
    organization = graphene.Field(OrganizationT)

    class Arguments:
        id = graphene.ID()
        last_name = graphene.String()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_score = graphene.Int()
        efc = graphene.Int()
        pronouns = graphene.String()
        ethnicity = graphene.String()
        user_type = graphene.String()
        place_id = graphene.String()
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
        pronouns=None,
        ethnicity=None,
        user_type=None,
        place_id=None,
        high_school_grad_year=None,
        income_quintile=None,
        found_from=None
    ):
        try:
            organization = Organization.objects.get(place_id=place_id)
        except:
            base_endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
            fields = "name,formatted_address,formatted_phone_number,geometry,business_status,url,website,icon,types"
            params = {
                "key": os.environ.get('GOOGLE_API'),
                "place_id": place_id,
                "fields": fields
            }
            params_encoded = urlencode(params)
            url = f"{base_endpoint}?{params_encoded}"
            r = requests.get(url)
            result = r.json()['result']

            organization = Organization(
                place_id=place_id,
                business_status=result['business_status'],
                icon=result['icon'],
                name=result['name'],
                address=result['formatted_address'],
                phone_number=result['formatted_phone_number'],
                url=result['url'],
                website=result['website'],
                lat=result['geometry']['location']['lat'],
                lng=result['geometry']['location']['lng'],
                types=result['types']
            )
            organization.save()

        user = get_user_model().objects.get(pk=id)
        if user is not None:
            user.last_name = last_name
            user.preferred_name = preferred_name
            user.gpa = gpa
            user.act_score = act_score
            user.sat_score = sat_score
            user.efc = efc
            user.pronouns = pronouns
            user.ethnicity = ethnicity
            user.user_type = user_type
            user.high_school = organization
            user.high_school_grad_year = high_school_grad_year
            user.income_quintile = income_quintile
            user.found_from = found_from
            user.is_onboarded = True
            user.save()
            return OnboardUser(user=user)
        else:
            raise Exception("User is not logged in")


class LogoutUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_logged_out: graphene.Boolean()

    def mutate(self, info):
        logout(info.context)


class SendVerificationEmail(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(
        self,
        info,
        email,

    ):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        user = get_user_model().objects.get(email=email)
        if user is not None:
            send_verification(user.email, user.first_name)
            return SendVerificationEmail(success=True)
        else:
            raise Exception("Email not found")


class SendForgotEmail(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(self, info, email):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        user = get_user_model().objects.get(email=email)

        if user is not None:
            send_reset_password(user.email, user.first_name)
            return SendForgotEmail(success=True)
        else:
            raise Exception("Email not found")


class VerifyEmail(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        token = graphene.String(required=True)

    def mutate(self, info, token):
        email = jwt.decode(token,
                           os.environ.get('SECRET_KEY'),
                           algorithms=['HS256'])['email']

        user = get_user_model().objects.get(email=email)

        if email and not user.is_verified:
            user.is_verified = True
            user.save()
            login(info.context, user)
            return VerifyEmail(success=user.is_verified)


class ResetPassword(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        password_repeat = graphene.String()
        token = graphene.String(required=True)

    def mutate(self, info, token, password, password_repeat):
        email = jwt.decode(token,
                           os.environ.get('SECRET_KEY'),
                           algorithms=['HS256'])['email']
        user = get_user_model().objects.get(email=email)

        if user is not None and password == password_repeat:
            user.set_password(password)
            user.save()
            return ResetPassword(success=True)
        elif password != password_repeat:
            raise Exception("Passwords do not match")
        else:
            raise Exception("Password did not reset")


class AddSubscriber(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(
        self,
        info,
        email
    ):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        add_subscriber(email)
        return AddSubscriber(success=True)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
    onboard_user = OnboardUser.Field()
    logout_user = LogoutUser.Field()
    verify_email = VerifyEmail.Field()
    send_forgot_email = SendForgotEmail.Field()
    reset_password = ResetPassword.Field()
    send_verification_email = SendVerificationEmail.Field()
    social_auth = graphql_social_auth.SocialAuth.Field()
    add_subscriber = AddSubscriber.Field()
