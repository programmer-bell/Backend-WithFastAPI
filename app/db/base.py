from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Add all the models 
from app.db.models import user,product

