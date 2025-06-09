import strawberry
from strawberry.types import Info
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.graphql.types import UserType
from app.crud.users import get_user_by_email

@strawberry.type
class Query:
    @strawberry.field
    def get_user(self, email: str, info: Info) -> UserType:
        db: Session = next(get_db())
        user = get_user_by_email(db, email)
        if not user:
            raise Exception("User not found")
        return UserType(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phone_number=user.phone_number
        )
