from fastapi import FastAPI,APIRouter
from app.api.v1 import endpoints
from app.db.session import engine
from app.db import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Backend")

@app.get("/")
def home():
    return {"message":"Welcome"}

# Register routers
app.include_router(endpoints.router, prefix="/api/v1")














