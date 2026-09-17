from pydantic import Field

from .base import Base


class Dataset(Base):
    uid: str | None = None
    min_date: str = Field(..., alias="mindate")
    max_date: str = Field(..., alias="maxdate")
    name: str
    data_coverage: float = Field(..., alias="datacoverage")
    id: str
