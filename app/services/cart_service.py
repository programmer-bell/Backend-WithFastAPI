from sqlalchemy.orm import Session
from app.db.repositories import cart_repo 
from app.schemas.cart import CartItemCreate
from typing import List
from app.db.models.cart_item import CartItem

def add_item_to_cart(db: Session, user_id: int, item_in: CartItemCreate) -> CartItem:
    return cart_repo.add_or_update_cart_item(db, user_id, item_in)

def get_user_cart(db: Session, user_id: int) -> List[CartItem]:
    return cart_repo.get_cart_items(db, user_id)

def remove_item_from_cart(db: Session, user_id: int, product_id: int):
    return cart_repo.remove_cart_item(db, user_id, product_id)
