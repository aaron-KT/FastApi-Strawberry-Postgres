from sqlalchemy.orm import Session
from app.db.models.user import User
from passlib.context import CryptContext
from app.graphql.types import UserInput, UpdateUserInput
from app.utils.notify import notify_n8n

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
    notify_n8n(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_input: UpdateUserInput):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    db_user.first_name = user_input.first_name
    db_user.last_name = user_input.last_name
    db_user.phone_number = user_input.phone_number

    if user_input.password:
        db_user.hashed_password = pwd_context.hash(user_input.password)

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
