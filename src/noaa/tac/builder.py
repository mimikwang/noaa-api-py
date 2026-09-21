from http import HTTPMethod
from typing import Literal

import httpx
from pydantic import BaseModel

type Date = Literal["today", "latest", "recent"]
type Datum = Literal[
    "CRD", "IGLD", "LWD", "MHHW", "MHW", "MTL", "MSL", "MLW", "MLLW", "NAVD", "STND"
]
type Expand = Literal["detailed"]
type Units = Literal["metric", "english"]
type TimeZone = Literal["gmt", "lst", "lst_ldt"]
type VelocityType = Literal["speed_dir", "default"]


class BeginAndEndDates(BaseModel):
    begin_date: str
    end_date: str


class BeginDateAndRange(BaseModel):
    begin_date: str
    range: int


class EndDateAndRange(BaseModel):
    end_date: str
    range: int


class Builder:
    METADATA_API_PATH = "/webapi"
    DATA_API_PATH = "/datagetter"

    def __init__(self, base_url: str):
        self.base_url = base_url

    def water_level(
        self,
        *,
        station: str,
        date: Date | BeginAndEndDates | BeginDateAndRange | EndDateAndRange | int,
        units: Units,
        time_zone: TimeZone,
        datum: Datum,
    ) -> httpx.Request:

        begin_date = None
        end_date = None
        date_str = None
        range = None

        if isinstance(date, str):
            date_str = date
        elif isinstance(date, BeginAndEndDates):
            begin_date = date.begin_date
            end_date = date.end_date
        elif isinstance(date, BeginDateAndRange):
            begin_date = date.begin_date
            range = date.range
        elif isinstance(date, EndDateAndRange):
            end_date = date.end_date
            range = date.range
        elif isinstance(date, int):
            range = date

        return self.data(
            station=station,
            begin_date=begin_date,
            end_date=end_date,
            range=range,
            date=date_str,
            product="water_level",
            datum=datum,
            units=units,
            time_zone=time_zone,
        )

    def data(
        self,
        *,
        station: str | None = None,
        begin_date: str | None = None,
        end_date: str | None = None,
        range: int | None = None,
        date: Date | None = None,
        product: str | None = None,
        expand: Expand | None = None,
        datum: str | None = None,
        units: Units | None = None,
        time_zone: TimeZone | None = None,
        interval: str | None = None,
        bin: int | None = None,
        velocity_type: VelocityType | None = None,
    ) -> httpx.Request:
        """Build http request for the data api

        The API is documented here: https://api.tidesandcurrents.noaa.gov/api/prod/
        """
        params = {"format": "json"}
        if station:
            params["station"] = station

        if begin_date:
            params["begin_date"] = begin_date

        if end_date:
            params["end_date"] = end_date

        if range:
            params["range"] = range

        if date:
            params["date"] = date

        if product:
            params["product"] = product

        if expand:
            params["expand"] = expand

        if datum:
            params["datum"] = datum

        if units:
            params["units"] = units

        if time_zone:
            params["time_zone"] = time_zone

        if interval:
            params["interval"] = interval

        if bin is not None:
            params["bin"] = bin

        if velocity_type:
            params["vel_type"] = velocity_type

        return httpx.Request(
            method=HTTPMethod.GET,
            url=f"{self.base_url}{self.DATA_API_PATH}",
            params=params,
        )
