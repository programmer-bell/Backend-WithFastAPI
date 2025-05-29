from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.product import ProductCreate, ProductRead
from app.services import product_service
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=ProductRead)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product_service(db, product_in)

@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product_service(db, product_id)

@router.get("/", response_model=List[ProductRead])
def list_products(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    category: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None
):
    return product_service.list_products_service(db, skip, limit, search, category, price_min, price_max)
