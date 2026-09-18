from pydantic import Field

from .base import Base


class Data(Base):
    date: str
    data_type: str = Field(..., alias="datatype")
    station: str
    attributes: str
    value: float
