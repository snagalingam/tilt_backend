import graphene
import graphql_social_auth
import jwt
import os
import datetime

from django.contrib.auth import get_user_model, authenticate, login, logout, password_validation
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from graphene_django import DjangoObjectType
from organizations.models import Organization
from organizations.schema import OrganizationType
from services.sendgrid_api.send_email import send_subscription_verification, add_subscriber, send_verification, send_reset_password, send_password_changed, send_email_changed
from services.google_api.google_places import search_details
from services.helpers.actions import create_action, create_timestamp, create_date
from users.models import AccountType, Action, DeletedAccount, Ethnicity, EthnicityUser, Income, Pronoun, PronounUser, Source, SourceUser


User = get_user_model()


################################################
### Standard Model Definitions
################################################
class AccountType(DjangoObjectType):
    class Meta:
        model = AccountType
        fields = "__all__"

class ActionType(DjangoObjectType):
    class Meta:
        model = Action
        fields = "__all__"


class EthnicityType(DjangoObjectType):
    class Meta:
        model = Ethnicity
        fields = "__all__"


class EthnicityUserType(DjangoObjectType):
    class Meta:
        model = EthnicityUser
        fields = "__all__"


class IncomeType(DjangoObjectType):
    class Meta:
        model = Income
        fields = "__all__"


class PronounType(DjangoObjectType):
    class Meta:
        model = Pronoun
        fields = "__all__"


class PronounUserType(DjangoObjectType):
    class Meta:
        model = PronounUser
        fields = "__all__"


class SourceType(DjangoObjectType):
    class Meta:
        model = Source
        fields = "__all__"


class SourceUserType(DjangoObjectType):
    class Meta:
        model = SourceUser
        fields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = User


################################################
### Query
################################################
class Query(graphene.ObjectType):
    me = graphene.Field(TiltUserType)
    users = graphene.List(TiltUserType)

    def resolve_users(self, info):
        user = info.context.user
        if user.is_staff:
            return User.objects.all()
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
            # user is_authenticated and not is_verified
            raise Exception("User is not verified")


################################################
### Mutations
################################################
class AddSubscriber(graphene.Mutation):
    user = graphene.Field(TiltUserType)
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
        raise Exception("User not logged in")


class CreateUser(graphene.Mutation):
    user = graphene.Field(TiltUserType)

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
        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
        )

        # password validation
        try:
            password_validation.validate_password(password, user=user)
        except ValidationError as e:
            raise e

        user.set_password(password)
        user.save()
        # send email verification user after signup
        send_verification(user.email, user.first_name)
        return CreateUser(user=user)


class DeleteUser(graphene.Mutation):
    user = graphene.Field(TiltUserType)
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
        raise Exception("User account was not deleted")


class LoginUser(graphene.Mutation):
    user = graphene.Field(TiltUserType)
    is_authenticated = graphene.Boolean()

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        user = authenticate(username=email, password=password)

        if user:
            if user.is_verified:
                login(info.context, user,
                      backend="django.contrib.auth.backends.ModelBackend")
                # track user login
                create_action(user, 'Logged in')
                return LoginUser(user=user, is_authenticated=user.is_authenticated)
            raise Exception("User is not verified")
        raise Exception("Incorrect credentials")


class LogoutUser(graphene.Mutation):
    user = graphene.Field(TiltUserType)
    is_logged_out = graphene.Boolean()

    def mutate(self, info):
        user = info.context.user
        # track user logout
        create_action(user, 'Logged out')
        logout(info.context)
        return LogoutUser(is_logged_out=True)


class OnboardOrUpdateUser(graphene.Mutation):
    user = graphene.Field(TiltUserType)

    class Arguments:
        onboard_or_update = graphene.String()
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        delete_school = graphene.Boolean()
        preferred_contact_method = graphene.String()
        phone_number = graphene.String()
        preferred_name = graphene.String()
        gpa = graphene.Float()
        act_score = graphene.Int()
        sat_math = graphene.Int()
        sat_verbal = graphene.Int()
        efc = graphene.Int()
        high_school_grad_year = graphene.Int()

        # relationship to other models
        pronoun = graphene.String()
        source = graphene.List(graphene.String)
        ethnicity = graphene.List(graphene.String)
        user_type = graphene.String()
        income = graphene.String()

        # for organizations
        place_id = graphene.String()
        place_name = graphene.String()

    def mutate(
        self,
        info,
        onboard_or_update=None,
        email=None,
        first_name=None,
        last_name=None,
        delete_school=None,
        preferred_contact_method=None,
        phone_number=None,
        preferred_name=None,
        gpa=None,
        act_score=None,
        sat_math=None,
        sat_verbal=None,
        efc=None,
        high_school_grad_year=None,
        pronoun=None,
        source=None,
        ethnicity=None,
        user_type=None,
        income=None,
        place_id=None,
        place_name=None,
    ):

        user = info.context.user

        if not user.is_authenticated:
            raise Exception ("Incorrect Credentials")

        if preferred_name is None:
            preferred_name = ""

        # update user
        if onboard_or_update == "update":
            user.pronounuser_set.all().delete()
            user.sourceuser_set.all().delete()
            user.ethnicityuser_set.all().delete()

            if first_name and first_name != user.first_name:
                user.first_name = first_name

            if last_name and last_name != user.last_name:
                user.last_name = last_name

            if email and email != user.email:
                old_email = user.email
                lowercase_email = email.lower()
                new_email = BaseUserManager.normalize_email(lowercase_email)
                user.email = new_email
                send_email_changed(old_email, new_email, user.first_name)

        pronoun = Pronoun.objects.get(pronoun=pronoun)
        pronoun_user = PronounUser(
            user=user,
            pronoun=pronoun
        )
        pronoun_user.save()

        for found_from in source:
            source = Source.objects.get(source=found_from)

            if source.source == "other":
                source_user = SourceUser(
                    user=user,
                    source=source,
                    other_value=found_from
                )
            else:
                source_user = SourceUser(
                    user=user,
                    source=source
                )
            source_user.save()

        # create ethnicity_user
        for background in ethnicity:
            ethnicity = Ethnicity.objects.get(ethnicity=background)

            if ethnicity.ethnicity == "other":
                ethnicity_user = EthnicityUser(
                    user=user,
                    ethnicity=ethnicity,
                    other_value=background
                )
            else:
                ethnicity_user = EthnicityUser(
                    user=user,
                    ethnicity=ethnicity
                )
            ethnicity_user.save()

        # get user_type and income
        account_type = AccountType.objects.get(user_type=user_type)
        income = Income.objects.get(category=income)

        # delete schools
        if delete_school:
            user.organization.clear()
        else:
            # get organization
            try:
                organization = Organization.objects.get(place_id=place_id)
            except:
                organization = None

            if organization is None:
                try:
                    organization = Organization.objects.get(name=place_name)
                except:
                    organization = None

            # create new organization
            if organization is None:
                business_status = ""
                icon = ""
                lat = None
                lng = None
                address = ""
                place_phone_number = ""
                url = ""
                website = ""
                types = []

                if place_name is None:
                    place_name = ""

                if place_id is None:
                    place_id = ""
                else:
                    data = search_details(place_id)
                    results = data.get("result", "")
                    place_name = results.get("name")
                    location = results["geometry"]["location"]
                    lat = location.get("lat", None)
                    lng = location.get("lng", None)
                    business_status = results.get("business_status", "")
                    icon = results.get("icon", "")
                    address = results.get("formatted_address", "")
                    place_phone_number = results.get(
                            "formatted_phone_number", "")
                    url = results.get("url", "")
                    website = results.get("website", "")
                    types = results.get("types", [])

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
                    types=types
                )
                organization.save()

            # add organization to user
            user.organization.add(organization)

        user.phone_number = phone_number
        user.preferred_contact_method = preferred_contact_method
        user.preferred_name = preferred_name
        user.gpa = gpa
        user.act_score = act_score
        user.sat_math = sat_math
        user.sat_verbal = sat_verbal
        user.efc = efc
        user.high_school_grad_year = high_school_grad_year
        user.is_onboarded = True
        user.user_type = user_type
        user.income = income
        user.save()
        return OnboardOrUpdateUser(user=user)


class ResetPassword(graphene.Mutation):
    user = graphene.Field(TiltUserType)
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
        user = User.objects.get(email=email)

        if user is not None and password == password_repeat:
            user.set_password(password)
            user.save()
            return ResetPassword(success=True)
        elif password != password_repeat:
            raise Exception("Passwords do not match")
        raise Exception("Password did not reset")


class SendForgotEmail(graphene.Mutation):
    user = graphene.Field(TiltUserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(self, info, email):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)

        try:
            user = User.objects.get(email=email)
        except:
            user = None

        if user is not None:
            send_reset_password(user.email, user.first_name)
            return SendForgotEmail(success=True)
        raise Exception("Email not found")


class SendSubscriptionVerification(graphene.Mutation):
    user = graphene.Field(TiltUserType)
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String()

    def mutate(self, info, email):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        send_subscription_verification(email)
        return SendSubscriptionVerification(success=True)


class SendVerificationEmail(graphene.Mutation):
    user = graphene.Field(TiltUserType)
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

        try:
            user = User.objects.get(email=email)
        except:
            user = None

        if user is not None:
            send_verification(user.email, user.first_name)
            return SendVerificationEmail(success=True)
        raise Exception("Email not found")


class UpdatePassword(graphene.Mutation):
    user = graphene.Field(TiltUserType)
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

        user = info.context.user

        if user.is_authenticated:
            # password validation
            try:
                password_validation.validate_password(new_password, user=user)
            except ValidationError as e:
                raise e

            user.set_password(new_password)
            user.save()
            success = True
            send_password_changed(email, first_name)

            return UpdatePassword(success=success)
        raise Exception("Incorrect credentials")


class VerifyEmail(graphene.Mutation):
    user = graphene.Field(TiltUserType)
    success = graphene.Boolean()

    class Arguments:
        token = graphene.String(required=True)

    def mutate(self, info, token):
        email = jwt.decode(token,
                           os.environ.get('SECRET_KEY'),
                           algorithms=['HS256'])['email']

        user = User.objects.get(email=email)

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
    onboard_or_update = OnboardOrUpdateUser.Field()
    reset_password = ResetPassword.Field()
    send_forgot_email = SendForgotEmail.Field()
    send_subscription_verification = SendSubscriptionVerification.Field()
    send_verification_email = SendVerificationEmail.Field()
    social_auth = graphql_social_auth.SocialAuth.Field()
    update_password = UpdatePassword.Field()
    verify_email = VerifyEmail.Field()
