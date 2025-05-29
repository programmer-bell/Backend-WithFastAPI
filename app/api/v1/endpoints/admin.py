from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_admin_user
from app.schemas.user import UserOut
from app.db.models.user import User
from app.db.models.orders import Order
from app.db.models.product import Product

router = APIRouter()

@router.get("/users/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db), _: User = Depends(get_current_admin_user)):
    return db.query(User).all()

@router.get("/orders/")
def list_orders(db: Session = Depends(get_db), _: User = Depends(get_current_admin_user)):
    return db.query(Order).all()

@router.get("/products/")
def list_products(db: Session = Depends(get_db), _: User = Depends(get_current_admin_user)):
    return db.query(Product).all()

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_admin_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"msg": "User deleted"}

@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db), _: User = Depends(get_current_admin_user)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"msg": "Order deleted"}


from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.services.product_service import (
    create_product_service, update_product_service, delete_product_service
)

@router.post("/products/", response_model=ProductOut)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin_user)
):
    return create_product_service(db, product)

@router.put("/products/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    updates: ProductUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin_user)
):
    updated = update_product_service(db, product_id, updates)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin_user)
):
    deleted = delete_product_service(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"msg": "Product deleted"}

