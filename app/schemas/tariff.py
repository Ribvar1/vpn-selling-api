from enum import Enum

from pydantic import Field

from app.schemas.base import IdentifiableSchema, BaseSchema


class CountryType(str, Enum):
    GERMANY = "DE"


class CurrencyType(str, Enum):
    BTC = "BTC"
    USDT = "USDT"


class TariffRequestSchema(BaseSchema):
    name: str = Field(title="Name", max_length=32)
    price: float = Field(title="Price")
    currency: CurrencyType = Field(title="Currency", max_length=8)
    days: int = Field(title="Duration in days")
    country: CountryType = Field(title="Country", max_length=2)
    active: bool = Field(title="Active", default=True)


class TariffSchema(TariffRequestSchema, IdentifiableSchema):
    pass
