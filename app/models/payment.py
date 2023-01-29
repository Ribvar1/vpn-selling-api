from dataclasses import field

from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import relationship

from app.models.base import IdentifiableMixin, TimestampableMixin, model
from app.models.subscription import Subscription


@model()
class Payment(IdentifiableMixin, TimestampableMixin):
    user_id: int = field(metadata={"sa": Column(ForeignKey("user.id", ondelete="CASCADE"))})
    price: float = field(metadata={"sa": Column(Float, nullable=False)})
    currency: str = field(metadata={"sa": Column(String(8), nullable=False)})
    subscription_id: int = field(metadata={"sa": Column(ForeignKey("subscription.id", ondelete="CASCADE"))})

    subscription: Subscription = relationship(
        Subscription, foreign_keys=[subscription_id.metadata["sa"]]  # type: ignore
    )
