from pydantic import BaseModel
from typing import List
from app.schemas.product import ProductRead

class OrderItemRead(BaseModel):
    product: ProductRead
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True

class OrderRead(BaseModel):
    id: int
    total_price: float
    status: str
    items: List[OrderItemRead]

    class Config:
        from_attributes = True
