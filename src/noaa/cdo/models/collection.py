from typing import TypeVar

from pydantic import Field

from .base import Base

ResultT = TypeVar("ResultT")


class ResultSet(Base):
    offset: int
    count: int
    limit: int


class Metadata(Base):
    result_set: ResultSet = Field(..., alias="resultset")


class Collection[ResultT](Base):
    metadata: Metadata
    results: list[ResultT]
