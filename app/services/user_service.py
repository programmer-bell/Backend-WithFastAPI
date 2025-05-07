from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.repositories import user_repo
from app.db.models.user import User

def register_user(db: Session, user_data: UserCreate) -> User:
    existing_user = user_repo.get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("Email already registered")
    
    return user_repo.create_user(db, user_data)

def get_user_by_id(db: Session, user_id: int) -> User:
    return user_repo.get_user(db, user_id)