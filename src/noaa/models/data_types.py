from pydantic import Field

from .base import Base


class DataType(Base):
    min_date: str = Field(..., alias="mindate")
    max_date: str = Field(..., alias="maxdate")
    name: str | None = None
    data_coverage: float = Field(..., alias="datacoverage")
    id: str
