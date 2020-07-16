import graphene
import graphql_jwt
import graphql_social_auth

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
    social_auth = graphql_social_auth.SocialAuth.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
