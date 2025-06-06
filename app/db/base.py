from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here so they are discovered by SQLAlchemy
from app.db.models.user import User  # noqa
