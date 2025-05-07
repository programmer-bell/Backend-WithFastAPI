# app/db/base.py

from sqlalchemy.orm import DeclarativeBase

# Declare Base
class Base(DeclarativeBase):
    pass

from app.db.models import user
