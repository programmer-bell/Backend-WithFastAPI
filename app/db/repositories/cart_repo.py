from sqlalchemy.orm import Session
from app.db.models.cart_item import CartItem
from app.schemas.cart import CartItemCreate
from typing import List

def get_cart_items(db: Session, user_id: int) -> List[CartItem]:
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def add_or_update_cart_item(db: Session, user_id: int, item_in: CartItemCreate) -> CartItem:
    cart_item = db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == item_in.product_id
    ).first()

    if cart_item:
        cart_item.quantity = item_in.quantity
    else:
        cart_item = CartItem(user_id=user_id, **item_in.dict())
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)
    return cart_item

def remove_cart_item(db: Session, user_id: int, product_id: int):
    cart_item = db.query(CartItem).filter(
        CartItem.user_id == user_id,
        CartItem.product_id == product_id
    ).first()
    if cart_item:
        db.delete(cart_item)
        db.commit()
