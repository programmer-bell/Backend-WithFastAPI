from sqlalchemy.orm import Session
from app.db.models.orders import Order
from app.db.repositories import order_repo

def place_order_service(db: Session, user_id: int) -> Order:
    return order_repo.create_order_from_cart(db, user_id)

def get_user_orders_service(db: Session, user_id: int):
    return order_repo.get_user_orders(db, user_id)

def update_order_status_service(db: Session, order_id: int, new_status: str):
    return order_repo.update_order_status(db, order_id, new_status)
