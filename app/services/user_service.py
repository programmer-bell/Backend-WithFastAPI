from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.models.user import User
from app.db.repositories import user_repo
from app.core import security

def register_user(db: Session, user_data: UserCreate) -> User:
    if user_repo.get_user_by_email(db, user_data.email):
        raise ValueError("Email already registered")
    if user_repo.get_user_by_username(db, user_data.username):
        raise ValueError("Username already taken")
    return user_repo.create_user(db, user_data)

def authenticate_and_create_token(db: Session, username: str, password: str) -> str:
    user = user_repo.authenticate_user(db, username, password)
    if not user:
        return None
    return security.create_access_token(data={"sub": user.username})

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return user_repo.get_user(db, user_id)

