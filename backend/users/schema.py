import graphene
from django.contrib.auth import get_user_model, authenticate, login
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

        return user


class LoginUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, email, password):
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


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
