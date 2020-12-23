import graphene
import graphql_jwt

import users.schema
import organizations.schema
import colleges.schema
import scholarships.schema
import financial_aid.schema


class Query(
    users.schema.Query,
    organizations.schema.Query,
    colleges.schema.Query,
    scholarships.schema.Query,
    financial_aid.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    organizations.schema.Mutation,
    colleges.schema.Mutation,
    scholarships.schema.Mutation,
    financial_aid.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
