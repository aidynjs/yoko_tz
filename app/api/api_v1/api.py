from fastapi import APIRouter

from app.api.api_v1.endpoints import customer, employee, shop_point

api_router = APIRouter()
api_router.include_router(employee.router, prefix="/employee", tags=["employee"])
api_router.include_router(shop_point.router, prefix="/shop-point", tags=["shop-point"])
api_router.include_router(customer.router, prefix="/customer", tags=["customer"])
