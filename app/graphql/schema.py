import strawberry
from app.graphql.resolvers.mutation import Mutation
from app.graphql.resolvers.query import Query

schema = strawberry.federation.Schema(query=Query, mutation=Mutation)