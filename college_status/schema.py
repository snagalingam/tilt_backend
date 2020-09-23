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

    college_status_by_college_id = graphene.Field(
        CollegeStatusType, college_id=graphene.Int())

    college_status_by_user_id = graphene.Field(
        CollegeStatusType, user_id=graphene.Int())

    def resolve_college_statuses(self, info):
        return CollegeStatus.objects.all()

    def resolve_college_status_by_college_id(root, info, college_id):
        return CollegeStatus.objects.get(college_id=college_id)

    def resolve_college_status_by_user_id(root, info, user_id):
        return CollegeStatus.objects.get(user_id=user_id)


class CreateCollegeStatus(graphene.Mutation):
    college_status = graphene.Field(CollegeStatusType)

    class Arguments:
        user_id = graphene.Int()
        college_id = graphene.Int()
        status = graphene.String()
        net_price = graphene.Int()

    def mutate(
        self,
        info,
        user_id=None,
        college_id=None,
        status=None,
        net_price=None,
    ):

        status_list = ("interested",
                    "applied",
                    "accepted",
                    "waitlisted",
                    "not accepted")

        user = get_user_model().objects.get(pk=user_id)
        college = College.objects.get(pk=college_id)
        
        try:
            college_status = CollegeStatus.objects.get(
                user_id=user_id, college_id=college_id)
        except: 
            college_status = None
            pass 

        try:
            college_status = CollegeStatus.objects.get(
                user_id=user_id, college_id=college_id)
        except:
            college_status = None
            pass


        if college_status is None:
            if status in status_list:
                college.popularity_score += 1
                college.save()


            college_status = CollegeStatus(
                user_id=user,
                college_id=college,
                status=status,
                net_price=net_price,
                )

            college_status.save()
            return CreateCollegeStatus(college_status=college_status)
        else:
            raise Exception('College status exists')


class UpdateCollegeStatus(graphene.Mutation):
    college_status = graphene.Field(CollegeStatusType)

    class Arguments:
        user_id = graphene.Int()
        college_id = graphene.Int()
        status = graphene.String()
        net_price = graphene.Int()

    def mutate(
        self,
        user_id=None,
        college_id=None,
        status=None,
        net_price=None,
    ):

        status_list = ("interested",
                       "applied",
                       "accepted",
                       "waitlisted",
                       "not accepted")

        college = College.objects.get(pk=college_id)
        
        try:
            college_status = CollegeStatus.objects.get(
                user_id=user_id, college_id=college_id)
        except:
            raise Exception('College status does not exist')

        # status change from 'not interested' ==> 'status_list'
        if college_status.status == "not interested":
            if status in status_list:
                college.popularity_score += 1
                college.save()

        # status change from 'status_list' ==> 'not interested'
        elif college_status.status in status_list:
            if status == "not interested": 
                college.popularity_score -= 1
                college.save()

        if status is not None:
            college_status.status = status

        if net_price is not None:
            college_status.net_price = net_price

        college_status.save()
        return UpdateCollegeStatus(college_status=college_status)


class Mutation(graphene.ObjectType):
    create_college_status = CreateCollegeStatus.Field()
    update_college_status = UpdateCollegeStatus.Field()
