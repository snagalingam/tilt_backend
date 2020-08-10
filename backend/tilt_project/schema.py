import graphene
import graphql_jwt

import users.schema
import scholarships.schema
import organizations.schema
import tilt_partners.schema

class Query(
    users.schema.Query,
    scholarships.schema.Query,
    organizations.schema.Query,
    tilt_partners.schema.Query,
    graphene.ObjectType,
):
    pass

class Mutation(
    users.schema.Mutation,
    scholarships.schema.Mutation,
    organizations.schema.Mutation,
    tilt_partners.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refersh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
