from typing import TypeVar

from .base import Base

ResponseT = TypeVar("ResponseT")


class Metadata(Base):
    id: str
    name: str
    lat: str
    lon: str


class Response[ResponseT](Base):
    metadata: Metadata
    data: list[ResponseT]
