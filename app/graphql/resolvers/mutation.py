import strawberry
from strawberry.types import Info
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.graphql.types import UserInput, UserType, UpdateUserInput
from app.crud.users import get_user_by_email, create_user, update_user, delete_user

@strawberry.type
class Mutation:
    @strawberry.mutation
    def register_user(self, user_input: UserInput, info: Info) -> UserType:
        db: Session = next(get_db())
        if get_user_by_email(db, user_input.email):
            raise Exception("Email already exists")
        user = create_user(db, user_input)
        return UserType(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,  # This was missing
        phone_number=user.phone_number  # Add this too if UserType expects it
    )
    
    @strawberry.mutation
    def update_user(self, user_id: int, user_input: UpdateUserInput, info) -> UserType:
        db: Session = next(get_db())
        user = update_user(db, user_id, user_input)
        if not user:
            raise Exception("User not found")
        return user
    
    @strawberry.mutation
    def delete_user(self, user_id: int, info) -> UserType:
        db: Session = next(get_db())
        user = delete_user(db, user_id)
        if not user:
            raise Exception("User not found")
        return user