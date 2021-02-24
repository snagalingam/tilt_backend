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
from services.sendgrid.send_email import send_subscription_verification, add_subscriber, send_verification, send_reset_password, send_password_changed, send_email_changed
from services.google.google_places import search_place_id
from services.helpers.actions import create_action, create_timestamp, create_date
from users.models import Action, DeletedAccount, Ethnicity, EthnicityUser, Income, Pronoun, PronounUser, Source, SourceUser, User, UserCategory


################################################
# Object Definitions
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
# Query
################################################
class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

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
# Mutations
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
            if user.preferred_name is not None:
                name = user.preferred_name
            else:
                name = user.first_name

            send_reset_password(email=user.email, name=name)
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


class UpdateEmail(graphene.Mutation):
    class Arguments:
        email = graphene.String()

    user = graphene.Field(UserType)

    def mutate(
        self,
        info,
        email
    ):

        user = info.context.user

        if user.is_authenticated:
            if email and email != user.email:
                old_email = user.email
                lowercase_email = email.lower()
                new_email = BaseUserManager.normalize_email(lowercase_email)
                user.email = new_email

                if user.preferred_name is not None:
                    name = user.preferred_name
                else:
                    name = user.first_name

                send_email_changed(
                    old_email=old_email,
                    new_email=new_email,
                    name=name
                )
                user.save()
                return UpdateEmail(user=user)

        # raise exception if not authenticated
        raise Exception("Incorrect credentials")


class UpdatePassword(graphene.Mutation):
    class Arguments:
        new_password = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(
        self,
        info,
        new_password,
        password,
    ):

        user = info.context.user

        if user.is_authenticated:
            # check if the password is the same
            if password == new_password:
                raise Exception("The passwords are the same")

            else:
                # password validation
                try:
                    password_validation.validate_password(new_password, user=user)
                except ValidationError as e:
                    raise e

                if user.preferred_name is not None:
                    name = user.preferred_name
                else:
                    name = user.first_name

                user.set_password(new_password)
                user.save()
                success = True
                send_password_changed(email=user.email, name=name)

                return UpdatePassword(success=success)

        # raise exception if not authenticated
        raise Exception("Incorrect credentials")

################################################################################
# Updates the logged in user. Pass the entire User object
# expect firstname, lastname, preferred_contact_method, source, user_category
################################################################################
class UpdateUser(graphene.Mutation):
    class Arguments:
        act_score = graphene.Int()
        efc = graphene.Int()
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
        efc=None,
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
            raise Exception("User is not logged in")

        else:
            # act score
            if act_score != user.act_score:
                user.act_score = act_score

            # efc
            if efc != user.efc:
                user.efc = efc

            # ethnicity
            if ethnicity is None and user.ethnicityuser_set.all() is not None:
                user.ethnicityuser_set.all().delete()

            elif ethnicity is not None:
                original_ethnicities = list(user.ethnicityuser_set.all())
                new_categories = []

                for input in ethnicity:
                    found = False

                    # get the category
                    try:
                        standard_value = Ethnicity.objects.get(category=input)
                    except:
                        standard_value = Ethnicity.objects.get(category="other")

                    # compare the input to current categories
                    for value in original_ethnicities:
                        if standard_value.category != "other" and standard_value == value.ethnicity:
                            found = True

                        elif standard_value.category == "other" and standard_value == value.ethnicity:
                            other_ethnicity = EthnicityUser.objects.get(
                                ethnicity=standard_value,
                                user=user
                            )
                            other_ethnicity.other_value = input
                            other_ethnicity.save()
                            found = True

                    if found == False:
                        if standard_value.category == "other":
                            EthnicityUser.objects.create(
                                ethnicity=standard_value,
                                other_value=input,
                                user=user
                            )
                        else:
                            EthnicityUser.objects.create(
                                ethnicity=standard_value,
                                user=user
                            )

                    new_categories.append(standard_value.category)

                # delete extra ethnicities
                updated_ethnicities = list(user.ethnicityuser_set.all())
                for value in updated_ethnicities:
                    if str(value.ethnicity) not in new_categories:
                        value.delete()

            # first name
            # only update first name if passing data
            if first_name and first_name != user.first_name:
                user.first_name = first_name

            # gpa
            if gpa != user.gpa:
                user.gpa = gpa

            # high school grad year
            if high_school_grad_year != user.high_school_grad_year:
                user.high_school_grad_year = high_school_grad_year

            # income
            if income != user.income:
                if income is None:
                    user.income = None
                else:
                    user.income = Income.objects.get(category=income)

            # last name
            # only update last name if passing data
            if last_name and last_name != user.last_name:
                user.last_name = last_name

            # phone number
            if phone_number != user.phone_number:
                if phone_number is not None:
                    user.phone_number = re.sub("[^0-9]", "", phone_number)
                else:
                    user.phone_number = ""

            # organization
            if place_id is not None:
                try:
                    organization = Organization.objects.get(place_id=place_id)
                    user.organization.clear()
                    user.organization.add(organization)
                except:
                    data = search_place_id(place_id=place_id)
                    results = data.get("result")

                    address = results.get("formatted_address", "")
                    business_status = results.get("business_status", "")
                    icon = results.get("icon", "")
                    lat = results.get("geometry")["location"]["lat"]
                    lng = results.get("geometry")["location"]["lng"]
                    place_phone_number = results.get("formatted_phone_number", "")
                    place_name = results.get("name")
                    types = results.get("types", [])
                    url = results.get("url", "")
                    website = results.get("website", "")

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

            # only look at place name if place_id is None
            elif place_name is not None and place_id is None:
                try:
                    organization = Organization.objects.get(name=place_name)
                    user.organization.clear()
                    user.organization.add(organization)
                except:
                    organization = Organization(name=place_name)
                    organization.save()
                    user.organization.clear()
                    user.organization.add(organization)

            else:
                try:
                    user.organization.clear()
                except:
                    pass

            # preferred contact method
            # only update preferred contact method if passing data
            if preferred_contact_method is not None:
                if preferred_contact_method != user.preferred_contact_method:
                    user.preferred_contact_method = preferred_contact_method

            # preferred name
            if preferred_name != user.preferred_name:
                if preferred_name is not None:
                    user.preferred_name = preferred_name
                else:
                    user.preferred_name = ""

            # pronoun
            if pronoun is None and user.pronounuser_set.all() is not None:
                user.pronounuser_set.all().delete()

            elif pronoun is not None:
                # get the category
                try:
                    standard_category = Pronoun.objects.get(category=pronoun)
                except:
                    standard_category = Pronoun.objects.get(category="other")

                # get the pronoun if already exists
                try:
                    current_value = PronounUser.objects.get(user=user)

                    if standard_category != current_value.pronoun:
                        user.pronounuser_set.all().delete()
                        current_value = None

                    elif standard_category.category == "other" and standard_category == current_value.pronoun:
                            pronoun_user = PronounUser.objects.get(
                                pronoun=standard_category,
                                user=user
                            )
                            pronoun_user.other_value = pronoun
                            pronoun_user.save()

                except:
                    current_value = None

                if current_value is None:
                    if standard_category.category == "other":
                        PronounUser.objects.create(
                            pronoun=standard_category,
                            other_value=pronoun,
                            user=user
                        )
                    else:
                        PronounUser.objects.create(
                            pronoun=standard_category,
                            user=user
                        )

            # sat math
            if sat_math != user.sat_math:
                user.sat_math = sat_math

            # sat verbal
            if sat_verbal != user.sat_verbal:
                user.sat_verbal = sat_verbal

            # source
            # only update source if passing data
            if source is not None:
                user.sourceuser_set.all().delete()

                for input in source:
                    try:
                        standard_category = Source.objects.get(category=input)
                        source_user = SourceUser(
                            user=user,
                            source=standard_category
                        )

                    except:
                        standard_category = Source.objects.get(category="other")
                        source_user = SourceUser(
                            user=user,
                            other_value=input,
                            source=standard_category
                        )

                    source_user.save()

            # user category
            # only update source if passing data
            if user_category is not None:
                if user_category != user.user_category:
                    user.user_category = UserCategory.objects.get(category=user_category)

            # social login adds first name and last name later, so user category is a better
            # check for onboarding
            if user.user_category is not None:
                user.is_onboarded = True

            user.save()
            return UpdateUser(user=user)


################################################################################
# Updates the logged in user. Pass specific fields to be updated
################################################################################
class UpdateUserFields(graphene.Mutation):
    class Arguments:
        phone_number = graphene.String()
        preferred_contact_method = graphene.String()

    user = graphene.Field(UserType)

    def mutate(
        self,
        info,
        phone_number=None,
        preferred_contact_method=None
    ):

        user = info.context.user

        if not user.is_authenticated:
            raise Exception("User is not logged in")

        else:
            # phone number
            if phone_number is not None:
                user.phone_number = re.sub("[^0-9]", "", phone_number)

            # preferred contact method
            if preferred_contact_method is not None:
                if preferred_contact_method != user.preferred_contact_method:
                    user.preferred_contact_method = preferred_contact_method


        user.save()
        return UpdateUserFields(user=user)

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
    update_email = UpdateEmail.Field()
    update_password = UpdatePassword.Field()
    update_user = UpdateUser.Field()
    update_user_fields = UpdateUserFields.Field()
    verify_email = VerifyEmail.Field()
