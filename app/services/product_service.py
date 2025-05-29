from sqlalchemy.orm import Session
from app.db.repositories.product_repo import create_product, update_product, delete_product
from app.schemas.product import ProductCreate, ProductUpdate

def create_product_service(db: Session, product_data: ProductCreate):
    return create_product(db, product_data)

def update_product_service(db: Session, product_id: int, updates: ProductUpdate):
    return update_product(db, product_id, updates)

def delete_product_service(db: Session, product_id: int):
    return delete_product(db, product_id)

