from sqlalchemy.orm import Session
from app.db.models.product import Product
from app.schemas.product import ProductCreate
from typing import List

def create_product(db: Session, product_in: ProductCreate) -> Product:
    product = Product(**product_in.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_product_by_id(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip=0, limit=10, search=None, category=None, price_min=None, price_max=None) -> List[Product]:
    query = db.query(Product)
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))
    if category:
        query = query.filter(Product.category == category)
    if price_min:
        query = query.filter(Product.price >= price_min)
    if price_max:
        query = query.filter(Product.price <= price_max)
    return query.offset(skip).limit(limit).all()
