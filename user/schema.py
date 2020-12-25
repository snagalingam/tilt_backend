import graphene
import graphql_social_auth
import jwt
import os
import datetime

from django.contrib.auth import get_user_model, authenticate, login, logout, password_validation
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from graphene_django import DjangoObjectType
from organization.models import Organization
from services.sendgrid_api.send_email import send_subscription_verification, add_subscriber, send_verification, send_reset_password, send_password_changed, send_email_changed
from services.google_api.google_places import search_details
from services.helpers.actions import create_action, create_timestamp, create_date
from user.models import DeletedAccount, Action


################################################
### Standard Model Definitions
################################################
class UserActionType(DjangoObjectType):
    class Meta:
        model = Action
        fields = "__all__"

class OrganizationType_(DjangoObjectType):
    class Meta:
        model = Organization
        fields = "__all__"

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


################################################
### Query
################################################
class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        user = info.context.user
        if user.is_staff:
            return get_user_model().objects.all()
        else:
            raise Exception('User not authorized please contact admin')

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        if user.is_authenticated:
            if user.social_auth.exists():
                if not user.is_verified:
                    user.is_verified = True
                    user.save()
                # track GET_ME query
                create_action(user, 'Social GET_ME query')
                return user
            if user.is_verified:
                # track GET_ME query
                create_action(user, 'Non-social GET_ME query')
                return user
            else:
                raise Exception("User is not verified")


################################################
### Mutations
################################################
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


class CreateAction(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        description = graphene.String()

    def mutate(self, info, description):
        user = info.context.user
        if user.is_authenticated:
            create_action(user, description)
            return CreateAction(success=True)
        else:
            return CreateAction(success=False)


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

        # password validation
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


class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_deleted = graphene.Boolean()

    def mutate(self, info):
        user = info.context.user

        if user.is_authenticated and user.is_active:
            user.delete()

            # get and format today's date (mm/dd/yyyy)
            date = create_date()

            # search for date
            try:
                get_count = DeletedAccount.objects.get(date=date)
            except:
                get_count = None

            # iternate get_count or create new_count
            if get_count is not None:
                get_count.accounts += 1
            else:
                get_count = DeletedAccount(
                    date=date,
                    accounts=1
                )
            # save DeletedAccount object
            get_count.save()

            return DeleteUser(is_deleted=True)
        else:
            raise Exception("User account was not deleted")


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
            if user.is_verified:
                login(info.context, user,
                      backend="django.contrib.auth.backends.ModelBackend")
                # track user login
                create_action(user, 'Logged in')
                return LoginUser(user=user, is_authenticated=user.is_authenticated)
            else:
                raise Exception("User is not verified")
        else:
            raise Exception("Incorrect credentials")


class LogoutUser(graphene.Mutation):
    user = graphene.Field(UserType)
    is_logged_out = graphene.Boolean()

    def mutate(self, info):
        user = info.context.user
        # track user logout
        create_action(user, 'Logged out')
        logout(info.context)
        return LogoutUser(is_logged_out=True)


class OnboardUser(graphene.Mutation):
    user = graphene.Field(UserType)
    organization = graphene.Field(OrganizationType_)

    class Arguments:
        id = graphene.ID()
        phone_number = graphene.String()
        preferred_contact_method = graphene.String()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_math = graphene.Int()
        sat_verbal = graphene.Int()
        efc = graphene.Int()
        pronouns = graphene.String()
        ethnicity = graphene.List(graphene.String)
        user_type = graphene.String()
        place_id = graphene.String()
        place_name = graphene.String()
        high_school_grad_year = graphene.Int()
        income_quintile = graphene.String()
        found_from = graphene.List(graphene.String)

    def mutate(
        self,
        info,
        id,
        phone_number=None,
        preferred_contact_method=None,
        preferred_name=None,
        gpa=None,
        act_score=None,
        sat_math=None,
        sat_verbal=None,
        efc=None,
        pronouns=None,
        ethnicity=None,
        user_type=None,
        place_id=None,
        place_name=None,
        high_school_grad_year=None,
        income_quintile=None,
        found_from=None
    ):

        user = get_user_model().objects.get(pk=id)

        if place_id is not None or place_name is not None:

            try:
                organization = Organization.objects.get(place_id=place_id)
            except:
                organization = None

            if place_name is not None:
                try:
                    organization = Organization.objects.get(name=place_name)
                except:
                    organization = None

            if organization is None:

                if place_id is not None:
                    data = search_details(place_id)
                    results = data.get("result")
                    lat = results.get("geometry")["location"]["lat"]
                    lng = results.get("geometry")["location"]["lng"]
                    place_name = results.get("name")
                    business_status = results.get("business_status", None)
                    icon = results.get("icon", None)
                    address = results.get("formatted_address", None)
                    place_phone_number = results.get(
                        "formatted_phone_number", None)
                    url = results.get("url", None)
                    website = results.get("website", None)
                    types = results.get("types", [])

                else:
                    results = {}
                    place_id = None
                    lat = None
                    lng = None
                    business_status = None
                    icon = None
                    address = None
                    place_phone_number = None
                    url = None
                    website = None
                    types = []

                organization = Organization(
                    place_id=place_id,
                    business_status=business_status,
                    icon=icon,
                    name=place_name,
                    lat=lat,
                    lng=lng,
                    address=address,
                    phone_number=place_phone_number,
                    url=url,
                    website=website,
                    types=types,
                )
                organization.save()

            # add organization to user after user is onboarded
            user.organization.add(organization)

        if user is not None:
            user.phone_number = phone_number
            user.preferred_contact_method = preferred_contact_method
            user.preferred_name = preferred_name
            user.gpa = gpa
            user.act_score = act_score
            user.sat_math = sat_math
            user.sat_verbal = sat_verbal
            user.efc = efc
            user.pronouns = pronouns
            user.ethnicity = ethnicity
            user.user_type = user_type
            user.high_school_grad_year = high_school_grad_year
            user.income_quintile = income_quintile
            user.found_from = found_from
            user.is_onboarded = True
            user.save()
            return OnboardUser(user=user)
        else:
            raise Exception("User is not logged in")


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


class SendSubscriptionVerification(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(self, info, email):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        send_subscription_verification(email)
        return SendSubscriptionVerification(success=True)


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


class UpdatePassword(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        new_password = graphene.String()
        first_name = graphene.String()

    def mutate(
        self,
        info,
        email,
        password,
        new_password,
        first_name
    ):
        user = authenticate(username=email, password=password)

        if user is not None:
            # password validation
            try:
                password_validation.validate_password(new_password, user=user)
            except ValidationError as e:
                return e
            user.set_password(new_password)
            user.save()
            success = True
            send_password_changed(email, first_name)
            return UpdatePassword(success=success)
        else:
            raise Exception("Incorrect credentials")


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    organization = graphene.Field(OrganizationType_)

    class Arguments:
        id = graphene.ID()
        first_name = graphene.String()
        last_name = graphene.String()
        phone_number = graphene.String()
        preferred_contact_method = graphene.String()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_math = graphene.Int()
        sat_verbal = graphene.Int()
        efc = graphene.Int()
        pronouns = graphene.String()
        ethnicity = graphene.List(graphene.String)
        user_type = graphene.String()
        place_id = graphene.String()
        place_name = graphene.String()
        high_school_grad_year = graphene.Int()
        income_quintile = graphene.String()
        email = graphene.String()
        delete_school = graphene.Boolean()

    def mutate(
        self,
        info,
        id,
        first_name=None,
        last_name=None,
        phone_number=None,
        preferred_contact_method=None,
        preferred_name=None,
        gpa=None,
        act_score=None,
        sat_math=None,
        sat_verbal=None,
        efc=None,
        pronouns=None,
        ethnicity=None,
        user_type=None,
        place_id=None,
        place_name=None,
        high_school_grad_year=None,
        income_quintile=None,
        email=None,
        delete_school=None,
    ):

        user = get_user_model().objects.get(pk=id)
        # set previous email to send email changed confirmation
        old_email = user.email

        if place_id is not None or place_name is not None:
            try:
                organization = Organization.objects.get(place_id=place_id)
            except:
                organization = None

            if place_name is not None:
                try:
                    organization = Organization.objects.get(name=place_name)
                except:
                    organization = None

            if organization is None:

                if place_id is not None:
                    data = search_details(place_id)
                    results = data.get("result")
                    lat = results.get("geometry")["location"]["lat"]
                    lng = results.get("geometry")["location"]["lng"]
                    place_name = results.get("name")
                    business_status = results.get("business_status", None)
                    icon = results.get("icon", None)
                    address = results.get("formatted_address", None)
                    place_phone_number = results.get(
                        "formatted_phone_number", None)
                    url = results.get("url", None)
                    website = results.get("website", None)
                    types = results.get("types", [])

                else:
                    results = {}
                    place_id = None
                    lat = None
                    lng = None
                    business_status = None
                    icon = None
                    address = None
                    place_phone_number = None
                    url = None
                    website = None
                    types = []

                organization = Organization(
                    place_id=place_id,
                    business_status=business_status,
                    icon=icon,
                    name=place_name,
                    lat=lat,
                    lng=lng,
                    address=address,
                    phone_number=place_phone_number,
                    url=url,
                    website=website,
                    types=types,
                )
                organization.save()
                user.organization.clear()
                user.organization.add(organization)
            else:
                user.organization.clear()
                user.organization.add(organization)
        elif delete_school:
            user.organization.clear()

        if user is not None:
            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.preferred_contact_method = preferred_contact_method
            user.preferred_name = preferred_name
            user.gpa = gpa
            user.act_score = act_score
            user.sat_math = sat_math
            user.sat_verbal = sat_verbal
            user.efc = efc
            user.pronouns = pronouns
            user.ethnicity = ethnicity
            user.user_type = user_type
            user.high_school_grad_year = high_school_grad_year
            user.income_quintile = income_quintile

            # if email changed send email changed confirmation
            if email != old_email:
                user.email = email
                send_email_changed(old_email, user.email, first_name)

            user.save()
            return UpdateUser(user=user)
        else:
            raise Exception("User is not logged in")


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
            login(info.context, user,
                  backend="django.contrib.auth.backends.ModelBackend")
            return VerifyEmail(success=user.is_verified)


class Mutation(graphene.ObjectType):
    add_subscriber = AddSubscriber.Field()
    create_action = CreateAction.Field()
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    login_user = LoginUser.Field()
    logout_user = LogoutUser.Field()
    onboard_user = OnboardUser.Field()
    reset_password = ResetPassword.Field()
    send_forgot_email = SendForgotEmail.Field()
    send_subscription_verification = SendSubscriptionVerification.Field()
    send_verification_email = SendVerificationEmail.Field()
    social_auth = graphql_social_auth.SocialAuth.Field()
    update_password = UpdatePassword.Field()
    update_user = UpdateUser.Field()
    verify_email = VerifyEmail.Field()
