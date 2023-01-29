from typing import Optional, AsyncGenerator

from fastapi import HTTPException, Depends
from fastapi.requests import Request
from fastapi.security import HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_401_UNAUTHORIZED

from app.constants import USER_ID_HEADER
from app.core.session import async_session
from app.models.authorization import AuthToken
from app.utils import is_valid_uuid4


async def get_user_id(request: Request) -> Optional[int]:
    return request.headers.get(USER_ID_HEADER)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_authentication_token(session: AsyncSession, token: str) -> Optional[AuthToken]:
    auth_token: Optional[AuthToken] = (await session.execute(select(AuthToken).where(AuthToken.id == token))).first()
    return auth_token


class BearerTokenAuthentication(HTTPBearer):
    async def __call__(
            self, request: Request, session: AsyncSession = Depends(get_session)
    ) -> AuthToken:
        authorization_credentials = await super(BearerTokenAuthentication, self).__call__(request=request)
        if (
                is_valid_uuid4(authorization_credentials.credentials)
                and (token := await get_authentication_token(session, authorization_credentials.credentials))
        ):
            return token
        else:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )


authentication_scheme = BearerTokenAuthentication()
