from dataclasses import field
from typing import Optional

from sqlalchemy import Column, String, Integer

from app.models.base import model, TimestampableMixin


@model()
class User(TimestampableMixin):
    id: int = field(metadata={"sa": Column(Integer, primary_key=True, index=True)})
    full_name: str = field(metadata={"sa": Column(String(255), nullable=False)})
    language: str = field(metadata={"sa": Column(String(2), nullable=False)})

    username: Optional[str] = field(default=None, metadata={"sa": Column(String(255), nullable=True, index=True)})
