from dataclasses import field

from sqlalchemy import Column, Integer, String

from app.models.base import IdentifiableMixin, model


@model()
class VPNServer(IdentifiableMixin):
    host: str = field(metadata={"sa": Column(String(64), nullable=False)})
    port: int = field(metadata={"sa": Column(Integer, nullable=False)})
    country: str = field(metadata={"sa": Column(String(2), nullable=False)})
