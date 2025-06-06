from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema

app = FastAPI()

graphql_app = GraphQLRouter(schema)

# Include the GraphQL router in the FastAPI app
app.include_router(graphql_app, prefix="/graphql")

# Create the database tables
@app.on_event("startup")
def on_startup():
    from app.db.session import engine
    from app.db.models import Base 
    Base.metadata.create_all(bind=engine)
