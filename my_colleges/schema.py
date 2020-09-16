import graphene
from graphene_django import DjangoObjectType
import json
import os
from .models import MyCollege

class MyCollegeType(DjangoObjectType):
    class Meta:
        model = MyCollege
        fields = "__all__"


class Query(graphene.ObjectType):
    my_college = graphene.List(MyCollegeType)
    my_college_by_popularity = graphene.List(MyCollegeType)

    my_college_by_college_id = graphene.Field(
        MyCollegeType, college_id=graphene.String())

    my_college_by_user_id = graphene.Field(
        MyCollegeType, user_id=graphene.String())

    def resolve_my_colleges(self, info):
        return MyCollege.objects.all()

    def my_college_by_popularity(root, info):
        # query for popularity | filter college_status != Not interested
        exclude_not_interested = MyCollege.objects.exclude(college_status="Not Interested")
        pass

    def resolve_my_college_by_college_id(root, info, college_id):
        return MyCollege.objects.get(college_id=college_id)

    def resolve_my_college_by_user_id(root, info, user_id):
        return MyCollege.objects.get(user_id=user_id)


class CreateMyCollege(graphene.Mutation):
    my_college = graphene.Field(MyCollegeType)

    class Arguments:
        user_id = graphene.String()
        college_id = graphene.String()
        college_status = graphene.String()
        net_price = graphene.Int()

    def mutate(
        self,
        info,
        user_id,
        college_id,
        college_status,
        net_price,
    ):

        my_college = MyCollege(
            user_id=user_id,
            college_id=college_id,
            college_status=college_status,
            net_price=net_price,
            )

        my_college.save()
        return CreateMyCollege(my_college=my_college)


class UpdateMyCollegeStatus(graphene.Mutation):
    my_college = graphene.Field(MyCollegeType)

    class Arguments:
        college_status = graphene.String()

    def mutate(
        self,
        info,
        user_id,
        college_id,
        college_status,
    ):

        try:
            my_college = MyCollege.objects.get(
                user_id=user_id, college_id=college_id)
        except:
            raise Exception('No college found')

        if my_college is not None: 
            my_college.college_status = college_status
            return UpdateMyCollegeStatus(my_college=my_college)
        else: 
            raise Exception('Status not changed')


class Mutation(graphene.ObjectType):
    create_my_college = CreateMyCollege.Field()
    update_my_college_status = UpdateMyCollegeStatus.Field()
