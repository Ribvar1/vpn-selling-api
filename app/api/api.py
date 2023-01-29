from fastapi import APIRouter

from app.api.endpoints import tariff
from app.api.endpoints import user

api_router = APIRouter()
api_router.include_router(user.router, prefix="", tags=["user"])
api_router.include_router(tariff.router, prefix="", tags=["tariff"])
