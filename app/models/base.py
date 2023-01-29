"""
SQL Alchemy models declaration.
https://docs.sqlalchemy.org/en/14/orm/declarative_styles.html#example-two-dataclasses-with-declarative-table
Dataclass style for powerful autocompletion support.

https://alembic.sqlalchemy.org/en/latest/tutorial.html
Note, it is used by alembic migrations logic, see `alembic/env.py`

Alembic shortcuts:
# create migration
alembic revision --autogenerate -m "migration_name"

# apply all migrations
alembic upgrade head
"""
from dataclasses import field, dataclass
from datetime import datetime
from typing import TypeVar

from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import registry

from app.utils import camel_to_snake

Base = registry()

T = TypeVar("T")


def model(abstract=False) -> T:
    def wrapped(cls: T):
        cls.__sa_dataclass_metadata_key__ = "sa"
        cls.__tablename__ = camel_to_snake(cls.__name__)
        cls.__abstract__ = abstract

        dataclass(cls)
        Base.mapped(cls)

        return cls

    return wrapped


@model(abstract=True)
class IdentifiableMixin:
    id: int = field(init=False, metadata={"sa": Column(Integer, primary_key=True, autoincrement=True, index=True)})


@model(abstract=True)
class TimestampableMixin:
    created: datetime = field(
        init=False, metadata={"sa": Column(DateTime(), server_default=func.now(), nullable=False)}
    )
    updated: datetime = field(
        init=False,
        metadata={
            "sa": Column(DateTime(), server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
        }
    )
