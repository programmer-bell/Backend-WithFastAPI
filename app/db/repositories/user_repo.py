# from sqlalchemy.orm import Session
# from app.db.models.user import User
# from app.schemas.user import UserCreate
# from app.core.security import get_password_hash

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

# def create_user(db: Session, user: UserCreate):
#     db_user = User(
#         email=user.email,
#         username=user.username,
#         hashed_password=get_password_hash(user.password),
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()
# from sqlalchemy.orm import Session
# from app.db.models.user import User
# from app.schemas.user import UserCreate
# from app.core.security import get_password_hash

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

# def create_user(db: Session, user: UserCreate):
#     db_user = User(
#         email=user.email,
#         username=user.username,
#         hashed_password=get_password_hash(user.password),
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()
# from sqlalchemy.orm import Session
# from app.db.models.user import User
# from app.schemas.user import UserCreate
# from app.core.security import get_password_hash

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

# def create_user(db: Session, user: UserCreate):
#     db_user = User(
#         email=user.email,
#         username=user.username,
#         hashed_password=get_password_hash(user.password),
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()
# from sqlalchemy.orm import Session
# from app.db.models.user import User
# from app.schemas.user import UserCreate
# from app.core.security import get_password_hash

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

# def create_user(db: Session, user: UserCreate):
#     db_user = User(
#         email=user.email,
#         username=user.username,
#         hashed_password=get_password_hash(user.password),
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()
# from sqlalchemy.orm import Session
# from app.db.models.user import User
# from app.schemas.user import UserCreate
# from app.core.security import get_password_hash

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

# def create_user(db: Session, user: UserCreate):
#     db_user = User(
#         email=user.email,
#         username=user.username,
#         hashed_password=get_password_hash(user.password),
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()







from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_password = pwd_context.hash(user_in.password)
    user = User(
        email=user_in.email,
        username=user_in.username,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str) -> User | None:
    user = get_user_by_username(db, username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


