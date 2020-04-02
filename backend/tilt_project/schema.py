import graphene
import graphql_jwt

import scholarships.schema
import users.schema

class Query(
    scholarships.schema.Query,
    users.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    scholarships.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refersh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
