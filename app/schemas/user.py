from enum import Enum
from typing import Optional

from pydantic import Field

from app.schemas.base import IdentifiableSchema, BaseSchema


class LanguageType(str, Enum):
    RUSSIAN = "RU"
    ENGLISH = "EN"


class UserUpdateRequestSchema(BaseSchema):
    username: Optional[str] = Field(title="Username", max_length=255)
    full_name: str = Field(title="Full name", max_length=255)
    language: LanguageType = Field(title="Language", default=LanguageType.RUSSIAN)


class UserSchema(UserUpdateRequestSchema, IdentifiableSchema):
    pass
