import graphene
import graphql_jwt

import aid.schema
import college.schema
import organization.schema
import scholarship.schema
import user.schema


class Query(
    aid.schema.Query,
    college.schema.Query,
    organization.schema.Query,
    scholarship.schema.Query,
    user.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    aid.schema.Mutation,
    college.schema.Mutation,
    organization.schema.Mutation,
    scholarship.schema.Mutation,
    user.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
