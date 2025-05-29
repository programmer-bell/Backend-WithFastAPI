from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.cart import CartItemCreate, CartItemRead
from app.services import cart_service
from app.core.dependencies import get_db, get_current_user
from app.db.models.user import User

router = APIRouter()

@router.post("/", response_model=CartItemRead)
def add_item(item: CartItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return cart_service.add_item_to_cart(db, current_user.id, item)

@router.get("/", response_model=List[CartItemRead])
def view_cart(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return cart_service.get_user_cart(db, current_user.id)

@router.delete("/{product_id}")
def remove_item(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cart_service.remove_item_from_cart(db, current_user.id, product_id)
    return {"message": "Item removed"}
