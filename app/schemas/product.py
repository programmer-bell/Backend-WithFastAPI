from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category: str
    stock: int

class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    in_stock: int


class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    in_stock: Optional[int]


class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True

