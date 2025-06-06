import strawberry
from strawberry.types import Info
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.graphql.types import UserInput, UserType
from app.crud.users import get_user_by_email, create_user

@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, user_input: UserInput, info: Info) -> UserType:
        db: Session = next(get_db())
        if get_user_by_email(db, user_input.email):
            raise Exception("Email already exists")
        user = create_user(db, user_input)
        return UserType(id=user.id, email=user.email, first_name = user.first_name)
    