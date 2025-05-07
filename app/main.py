from fastapi import FastAPI
from app.db.session import engine
from app.db import base
from app.api.v1.endpoints.users import router as users_router

base.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Backend")

@app.get("/")
async def get():
    return {"message":"Welcome to our Ecommerce FastAPI"}


# Include all routers here:
app.include_router(users_router, prefix="/api/v1")














