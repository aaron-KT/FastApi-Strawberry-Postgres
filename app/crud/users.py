from sqlalchemy.orm import Session
from app.db.models.user import User
from passlib.context import CryptContext
from app.graphql.types import UserInput

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserInput):
    hashed_pw = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user