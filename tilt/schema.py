import graphene
import graphql_jwt

import financial_aid.schema
import colleges.schema
import organizations.schema
import scholarships.schema
import users.schema


class Query(
    financial_aid.schema.Query,
    colleges.schema.Query,
    organizations.schema.Query,
    scholarships.schema.Query,
    users.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    financial_aid.schema.Mutation,
    colleges.schema.Mutation,
    organizations.schema.Mutation,
    scholarships.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
