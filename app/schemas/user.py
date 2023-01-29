from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.base import IdentifiableSchema


class LanguageType(str, Enum):
    RUSSIAN = "ru"
    ENGLISH = "en"


class UserUpdateRequestSchema(BaseModel):
    username: Optional[str] = Field(title="Username", max_length=255)
    full_name: str = Field(title="Full name", max_length=255)
    language: LanguageType = Field(title="Language", default="ru")


class UserSchema(UserUpdateRequestSchema, IdentifiableSchema):
    pass
