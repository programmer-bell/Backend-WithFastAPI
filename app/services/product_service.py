from sqlalchemy.orm import Session
from app.db.repositories import product_repo
from app.schemas.product import ProductCreate
from typing import List
from app.db.models.product import Product

def create_product_service(db: Session, product_in: ProductCreate) -> Product:
    return product_repo.create_product(db, product_in)

def get_product_service(db: Session, product_id: int) -> Product:
    return product_repo.get_product_by_id(db, product_id)

def list_products_service(db: Session, skip=0, limit=10, search=None, category=None, price_min=None, price_max=None) -> List[Product]:
    return product_repo.get_products(db, skip, limit, search, category, price_min, price_max)
