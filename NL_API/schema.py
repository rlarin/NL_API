import graphene
import graphql_jwt
import users.schema
import nlp_methods.schema


class Query(
    nlp_methods.schema.Query,
    users.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    nlp_methods.schema.Mutation,

    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
