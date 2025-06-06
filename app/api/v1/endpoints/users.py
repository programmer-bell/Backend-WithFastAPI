from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.services import user_service
from app.core.dependencies import get_db, get_current_user

router = APIRouter(prefix="", tags=["Users"])

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.register_user(db, user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = user_service.authenticate_and_create_token(db, form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/make-admin/{user_id}")
def make_admin(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_admin = True
    db.commit()
    return {"msg": f"User {user.email} is now admin"}





