import graphene
from graphene_django import DjangoObjectType
import json
import os
from django.contrib.auth import get_user_model
from .models import CollegeStatus
from .models import College
from django.db.models import Count

class CollegeStatusType(DjangoObjectType):
    class Meta:
        model = CollegeStatus
        fields = "__all__"

class Query(graphene.ObjectType):
    college_statuses = graphene.List(CollegeStatusType)
    # college_status_by_popularity = graphene.List(CollegeStatusType)

    college_status_by_college_id = graphene.Field(
        CollegeStatusType, college_id=graphene.Int())

    college_status_by_user_id = graphene.Field(
        CollegeStatusType, user_id=graphene.Int())

    def resolve_college_statuses(self, info):
        return CollegeStatus.objects.all()

    # def resolve_college_status_by_popularity(self, info):
    #     # .values('<field value>') ==> gets name of model field
    #     # .annotate(<name of key>=Count('<field value>') ==> what you want to count in each instance

    #     college_set = CollegeStatus.objects.exclude(
    #         college_status="Not interested").values('college_id').annotate(count=Count('college_id'))
    #     college_count = (each['college_id'] for each in college_set)

    #     return Query(college_count)

    def resolve_college_status_by_college_id(root, info, college_id):
        return CollegeStatus.objects.get(college_id=college_id)

    def resolve_college_status_by_user_id(root, info, user_id):
        return CollegeStatus.objects.get(user_id=user_id)


class CreateCollegeStatus(graphene.Mutation):
    college_status = graphene.Field(CollegeStatusType)

    class Arguments:
        user_id = graphene.Int()
        college_id = graphene.Int()
        college_status = graphene.String()
        net_price = graphene.Int()

    def mutate(
        self,
        info,
        user_id=None,
        college_id=None,
        college_status=None,
        net_price=None,
    ):
        user = get_user_model().objects.get(pk=user_id)
        college = College.objects.get(pk=college_id)

        college_status = CollegeStatus(
            user_id=user,
            college_id=college,
            college_status=college_status,
            net_price=net_price,
            )

        college_status.save()
        return CreateCollegeStatus(college_status=college_status)


class UpdateCollegeStatus(graphene.Mutation):
    college_status = graphene.Field(CollegeStatusType)

    class Arguments:
        user_id = graphene.Int()
        college_id = graphene.Int()
        college_status = graphene.String()

    def mutate(
        self,
        info,
        user_id,
        college_id,
        college_status,
    ):

        try:
            college_status = CollegeStatus.objects.get(
                user_id=user_id, college_id=college_id)
        except:
            raise Exception('No college status found')

        if college_status is not None: 
            college_status.college_status = college_status
            return UpdateCollegeStatus(college_status=college_status)
        else: 
            raise Exception('Status not changed')


class Mutation(graphene.ObjectType):
    create_college_status = CreateCollegeStatus.Field()
    update_college_status = UpdateCollegeStatus.Field()
