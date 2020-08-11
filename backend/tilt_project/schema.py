import graphene
import graphql_jwt

import scholarships.schema
import users.schema
import organizations.schema


class Query(
    scholarships.schema.Query,
    users.schema.Query,
    organizations.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    scholarships.schema.Mutation,
    users.schema.Mutation,
    organizations.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
