from pydantic import BaseModel
from typing import Optional
from app.schemas.product import ProductRead

class CartItemBase(BaseModel):
    product_id: int
    quantity: int

class CartItemCreate(CartItemBase):
    pass

class CartItemRead(CartItemBase):
    id: int
    product: ProductRead

    class Config:
        from_attributes = True
