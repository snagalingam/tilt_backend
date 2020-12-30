import datetime
import graphene
import graphql_social_auth
import jwt
import os
import re

from django.contrib.auth import get_user_model, authenticate, login, logout, password_validation
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from graphene_django import DjangoObjectType
from organizations.models import Organization
from organizations.schema import OrganizationType
from services.sendgrid_api.send_email import send_subscription_verification, add_subscriber, send_verification, send_reset_password, send_password_changed, send_email_changed
from services.google_api.google_places import search_details
from services.helpers.actions import create_action, create_timestamp, create_date
from users.models import Action, DeletedAccount, Ethnicity, EthnicityUser, Income, Pronoun, PronounUser, Source, SourceUser, User, UserCategory


################################################
### Object Definitions
################################################
class EthnicityType(DjangoObjectType):
    class Meta:
        model = Ethnicity
        fields = ('id', 'category', 'description')


class EthnicityUserType(DjangoObjectType):
    class Meta:
        model = EthnicityUser
        fields = ('id', 'ethnicity', 'other_value', 'user')


class IncomeType(DjangoObjectType):
    class Meta:
        model = Income
        fields = ('id', 'category', 'description')


class PronounType(DjangoObjectType):
    class Meta:
        model = Pronoun
        fields = ('id', 'category')


class PronounUserType(DjangoObjectType):
    class Meta:
        model = PronounUser
        fields = ('id', 'other_value', 'pronoun', 'user')


class SourceType(DjangoObjectType):
    class Meta:
        model = Source
        fields = ('id', 'category')


class SourceUserType(DjangoObjectType):
    class Meta:
        model = SourceUser
        fields = ('id', 'other_value', 'source', 'user')


class UserType(DjangoObjectType):
    class Meta:
        convert_choices_to_enum = False
        fields = (
            "act_score",
            "efc",
            "email",
            "ethnicityuser_set",
            "first_name",
            "gpa",
            "high_school_grad_year",
            "id",
            "income",
            "last_name",
            "organization",
            "phone_number",
            "preferred_contact_method",
            "preferred_name",
            "pronounuser_set",
            "sat_math",
            "sat_verbal",
            "sourceuser_set",
            "user_category",
            "is_onboarded",
            "is_superuser",
            "is_verified"
        )
        model = User


class UserCategoryType(DjangoObjectType):
    class Meta:
        model = UserCategory
        fields = ('id', 'category')


################################################
### Query
################################################
class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        user = info.context.user
        if user.is_superuser:
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
    class Arguments:
        email = graphene.String()

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(self, info, email):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        add_subscriber(email)
        return AddSubscriber(success=True)


class CreateAction(graphene.Mutation):
    class Arguments:
        description = graphene.String()

    success = graphene.Boolean()

    def mutate(self, info, description):
        user = info.context.user
        if user.is_authenticated:
            create_action(user, description)
            return CreateAction(success=True)
        raise Exception("User not logged in")


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    def mutate(
        self,
        info,
        email,
        first_name,
        last_name,
        password
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
        raise Exception("User account was not deleted")


class LoginUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)
    is_authenticated = graphene.Boolean()

    def mutate(self, info, email, password):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        user = authenticate(username=email, password=password)

        if user:
            if user.is_verified:
                login(
                    info.context,
                    user,
                    backend="django.contrib.auth.backends.ModelBackend"
                )
                # track user login
                create_action(user, 'Logged in')
                return LoginUser(user=user, is_authenticated=user.is_authenticated)
            raise Exception("User is not verified")
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


class UpdateUser(graphene.Mutation):
    class Arguments:
        act_score = graphene.Int()
        delete_school = graphene.Boolean()
        efc = graphene.Int()
        email = graphene.String()
        ethnicity = graphene.List(graphene.String)
        first_name = graphene.String()
        gpa = graphene.Float()
        high_school_grad_year = graphene.Int()
        income = graphene.String()
        last_name = graphene.String()
        phone_number = graphene.String()
        place_id = graphene.String()
        place_name = graphene.String()
        preferred_contact_method = graphene.String()
        preferred_name = graphene.String()
        pronoun = graphene.String()
        sat_math = graphene.Int()
        sat_verbal = graphene.Int()
        source = graphene.List(graphene.String)
        user_category = graphene.String()

    user = graphene.Field(UserType)

    def mutate(
        self,
        info,
        act_score=None,
        delete_school=None,
        efc=None,
        email=None,
        ethnicity=None,
        first_name=None,
        gpa=None,
        high_school_grad_year=None,
        income=None,
        last_name=None,
        phone_number=None,
        place_id=None,
        place_name=None,
        preferred_contact_method=None,
        preferred_name=None,
        pronoun=None,
        sat_math=None,
        sat_verbal=None,
        source=None,
        user_category=None
    ):

        user = info.context.user

        if not user.is_authenticated:
            raise Exception ("User is not logged in")

        else:
            if act_score is not None:
                user.act_score = act_score

            if delete_school is True:
                user.organization.clear()

            if efc is not None:
                user.efc = efc

            if email and email != user.email:
                old_email = user.email
                lowercase_email = email.lower()
                new_email = BaseUserManager.normalize_email(lowercase_email)
                user.email = new_email
                send_email_changed(old_email, new_email, user.first_name)

            if ethnicity is not None:
                user.ethnicityuser_set.all().delete()

                for input in ethnicity:
                    try:
                        standard_value = Ethnicity.objects.get(category=input)
                        ethnicity_user = EthnicityUser(
                            ethnicity=standard_value,
                            user=user
                        )

                    except ObjectDoesNotExist:
                        standard_value = Ethnicity.objects.get(category="other")
                        ethnicity_user = EthnicityUser(
                            ethnicity=standard_value,
                            other_value=input,
                            user=user
                        )

                    ethnicity_user.save()

            if first_name and first_name != user.first_name:
                user.first_name = first_name

            if gpa is not None:
                user.gpa = gpa

            if high_school_grad_year is not None:
                user.high_school_grad_year = high_school_grad_year

            if income is not None:
                user.income = Income.objects.get(category=income)

            if last_name and last_name != user.last_name:
                user.last_name = last_name

            if phone_number is not None:
                user.phone_number = re.sub("[^0-9]", "", phone_number)

            if place_id is not None or place_name is not None:
                # get the place if it already exists
                if place_id is not None:
                    try:
                        organization = Organization.objects.get(place_id=place_id)
                    except ObjectDoesNotExist:
                        if place_name is not None:
                            try:
                                organization = Organization.objects.get(name=place_name)
                            except ObjectDoesNotExist:
                                None

                else:
                    try:
                        organization = Organization.objects.get(name=place_name)
                    except ObjectDoesNotExist:
                        None

                # if it doesn't exist, try to search for it
                if place_id is not None:
                    try:
                        data = search_details(place_id)
                        results = data.get("result")

                        address = results.get("formatted_address", None)
                        business_status = results.get("business_status", None)
                        icon = results.get("icon", None)
                        lat = results.get("geometry")["location"]["lat"]
                        lng = results.get("geometry")["location"]["lng"]
                        place_phone_number = results.get("formatted_phone_number", None)
                        place_name = results.get("name")
                        types = results.get("types", [])
                        url = results.get("url", None)
                        website = results.get("website", None)

                        organization = Organization(
                            address=address,
                            business_status=business_status,
                            icon=icon,
                            lat=lat,
                            lng=lng,
                            name=place_name,
                            phone_number=place_phone_number,
                            place_id=place_id,
                            types=types,
                            url=url,
                            website=website
                        )

                        organization.save()
                        user.organization.clear()
                        user.organization.add(organization)

                    except ObjectDoesNotExist:
                        if place_name is not None:
                            organization = Organization(name=place_name)
                            organization.save()
                            user.organization.clear()
                            user.organization.add(organization)

                else:
                    organization = Organization(name=place_name)
                    organization.save()
                    user.organization.clear()
                    user.organization.add(organization)

            if preferred_contact_method is not None:
                user.preferred_contact_method = preferred_contact_method

            if preferred_name is not None:
                user.preferred_name = preferred_name

            if pronoun is not None:
                user.pronounuser_set.all().delete()

                try:
                    standard_value = Pronoun.objects.get(category=pronoun)
                    pronoun_user = PronounUser(
                        pronoun=standard_value,
                        user=user
                    )

                except ObjectDoesNotExist:
                    standard_value = Pronoun.objects.get(category=pronoun)
                    pronoun_user = PronounUser(
                        other_value=input,
                        pronoun=standard_value,
                        user=user
                    )

                pronoun_user.save()

            if sat_math is not None:
                user.sat_math = sat_math

            if sat_verbal is not None:
                user.sat_verbal = sat_verbal

            if source is not None:
                user.sourceuser_set.all().delete()

                for input in source:
                    try:
                        standard_value = Source.objects.get(category=input)
                        source_user = SourceUser(
                            user=user,
                            source=standard_value
                        )

                    except ObjectDoesNotExist:
                        standard_value = Source.objects.get(category="other")
                        source_user = SourceUser(
                            user=user,
                            other_value=input,
                            source=standard_value
                        )

                    source_user.save()

            if user_category is not None:
                user.user_category = UserCategory.objects.get(category=user_category)

            user.save()
            return UpdateUser(user=user)


class ResetPassword(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()
        password_repeat = graphene.String()
        token = graphene.String(required=True)

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(self, info, password, password_repeat, token):
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
    class Arguments:
        email = graphene.String()

    user = graphene.Field(UserType)
    success = graphene.Boolean()

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
    class Arguments:
        email = graphene.String()

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(self, info, email):
        lowercase_email = email.lower()
        email = BaseUserManager.normalize_email(lowercase_email)
        send_subscription_verification(email)
        return SendSubscriptionVerification(success=True)


class SendVerificationEmail(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(self, info, email):
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
    class Arguments:
        email = graphene.String()
        first_name = graphene.String()
        new_password = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(
        self,
        info,
        email,
        first_name,
        new_password,
        password,
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
    class Arguments:
        token = graphene.String(required=True)

    user = graphene.Field(UserType)
    success = graphene.Boolean()

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
    reset_password = ResetPassword.Field()
    send_forgot_email = SendForgotEmail.Field()
    send_subscription_verification = SendSubscriptionVerification.Field()
    send_verification_email = SendVerificationEmail.Field()
    social_auth = graphql_social_auth.SocialAuth.Field()
    update_password = UpdatePassword.Field()
    update_user = UpdateUser.Field()
    verify_email = VerifyEmail.Field()
