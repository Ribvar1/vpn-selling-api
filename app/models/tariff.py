from dataclasses import field

from sqlalchemy import Column, String, Float, Integer, Boolean

from app.models.base import IdentifiableMixin, model


@model()
class Tariff(IdentifiableMixin):
    name: str = field(metadata={"sa": Column(String(32), nullable=False)})
    price: float = field(metadata={"sa": Column(Float, nullable=False)})
    currency: str = field(metadata={"sa": Column(String(8), nullable=False)})
    days: int = field(metadata={"sa": Column(Integer, nullable=False)})
    country: str = field(metadata={"sa": Column(String(2), nullable=False)})
    active: bool = field(metadata={"sa": Column(Boolean, nullable=False)})
