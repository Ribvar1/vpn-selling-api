from dataclasses import field
from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from app.models.base import IdentifiableMixin, TimestampableMixin, model
from app.models.tariff import Tariff
from app.models.user import User
from app.models.vpn_server import VPNServer


@model()
class Subscription(IdentifiableMixin, TimestampableMixin):
    user_id: int = field(metadata={"sa": Column(ForeignKey("user.id", ondelete="CASCADE"))})
    until: datetime = field(metadata={"sa": Column(DateTime(), nullable=False, index=True)})
    vpn_server_id: int = field(metadata={"sa": Column(ForeignKey("vpn_server.id", ondelete="CASCADE"))})
    vpn_user_id: int = field(metadata={"sa": Column(Integer, nullable=False)})
    tariff_id: int = field(metadata={"sa": Column(ForeignKey("tariff.id", ondelete="CASCADE"))})

    user: User = relationship(User, foreign_keys=[user_id.metadata["sa"]])  # type: ignore
    vpn_server: VPNServer = relationship(VPNServer, foreign_keys=[vpn_server_id.metadata["sa"]])  # type: ignore
    tariff: Tariff = relationship(Tariff, foreign_keys=[tariff_id.metadata["sa"]])  # type: ignore
