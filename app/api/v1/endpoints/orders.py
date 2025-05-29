from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.db.models.user import User
from app.services import order_service
from app.schemas.orders import OrderRead
from typing import List

router = APIRouter()

@router.post("/", response_model=OrderRead)
def place_order(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        return order_service.place_order_service(db, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[OrderRead])
def list_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return order_service.get_user_orders_service(db, current_user.id)
