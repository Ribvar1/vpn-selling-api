from facrud_router import ModelCRUDRouter
from fastapi import APIRouter

from app.api.deps import get_session, authentication_scheme
from app.models.user import User
from app.schemas.user import UserSchema, UserUpdateRequestSchema

router = APIRouter()

user_crud_router = ModelCRUDRouter(
    prefix="user",
    model=User,
    identifier_type=int,
    get_session=get_session,
    get_authentication=authentication_scheme,
    request_schema=UserSchema,
    update_request_schema=UserUpdateRequestSchema,
    response_schema=UserSchema
)

router.include_router(user_crud_router.api_router)
