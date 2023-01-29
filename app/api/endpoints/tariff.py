from facrud_router import ModelCRUDRouter
from fastapi import APIRouter

from app.api.deps import get_session, authentication_scheme
from app.models import Tariff
from app.schemas.tariff import TariffSchema, TariffRequestSchema

router = APIRouter()

tariff_crud_router = ModelCRUDRouter(
    prefix="tariff",
    model=Tariff,
    identifier_type=int,
    get_session=get_session,
    get_authentication=authentication_scheme,
    request_schema=TariffRequestSchema,
    response_schema=TariffSchema
)

router.include_router(tariff_crud_router.api_router)
