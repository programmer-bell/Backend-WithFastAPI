from sqlalchemy.orm import Session
from app.db.models.orders import Order
from app.db.models.order_item import OrderItem
from app.db.models.cart_item import CartItem
from typing import List

def create_order_from_cart(db: Session, user_id: int) -> Order:
    cart_items: List[CartItem] = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    if not cart_items:
        raise ValueError("Cart is empty")

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order(user_id=user_id, total_price=total_price)
    db.add(order)
    db.flush()

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.product.price
        )
        db.add(order_item)

    db.query(CartItem).filter(CartItem.user_id == user_id).delete()
    db.commit()
    db.refresh(order)
    return order

def get_user_orders(db: Session, user_id: int) -> List[Order]:
    return db.query(Order).filter(Order.user_id == user_id).all()

def update_order_status(db: Session, order_id: int, new_status: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        order.status = new_status
        db.commit()
        db.refresh(order)
        return order
    else:
        raise ValueError("Order not found")
