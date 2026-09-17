from pydantic import Field

from .base import Base


class Station(Base):
    elevation: float
    min_date: str = Field(..., alias="mindate")
    max_date: str = Field(..., alias="maxdate")
    latitude: float
    name: str
    data_coverage: float = Field(..., alias="datacoverage")
    id: str
    elevation_unit: str = Field(..., alias="elevationUnit")
    longitude: float
