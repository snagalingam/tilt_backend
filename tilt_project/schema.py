import graphene
import graphql_jwt

import scholarships.schema
import users.schema
import organizations.schema
import colleges.schema
import college_status.schema


class Query(
    scholarships.schema.Query,
    users.schema.Query,
    organizations.schema.Query,
    colleges.schema.Query,
    college_status.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    scholarships.schema.Mutation,
    users.schema.Mutation,
    organizations.schema.Mutation,
    colleges.schema.Mutation,
    college_status.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
