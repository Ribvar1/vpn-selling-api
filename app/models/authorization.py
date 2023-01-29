import uuid
from dataclasses import field

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import model, TimestampableMixin


@model()
class AuthToken(TimestampableMixin):
    id: uuid.UUID = field(
        init=False,
        default_factory=uuid.uuid4,
        metadata={"sa": Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)},
    )
    title: str = field(metadata={"sa": Column(String(16), nullable=False)})
