from fastapi import FastAPI
# from app.api.v1 import endpoints
from app.db.session import engine
from app.db import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Backend")

@app.get("/")
async def get():
    return {"message":"Welcome to our Ecommerce FastAPI"}

# # Register routers
# app.include_router(endpoints.router, prefix="/api/v1")

# from fastapi import APIRouter
# from . import users  # Add other modules like products, cart later

# router = APIRouter()
# router.include_router(users.router, prefix="/users", tags=["Users"])














