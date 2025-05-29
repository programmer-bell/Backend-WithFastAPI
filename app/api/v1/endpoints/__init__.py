from fastapi import APIRouter
from . import users,cart,orders,products

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(cart.router,prefix='/carts',tags=["Carts"])
router.include_router(orders.router,prefix='/orders',tags=["Orders"])
router.include_router(products.router,prefix='/products',tags=["Products"])