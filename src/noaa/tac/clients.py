from typing import Any

import httpx

from .builder import (
    BeginAndEndDates,
    BeginDateAndRange,
    Builder,
    Date,
    Datum,
    EndDateAndRange,
    TimeZone,
    Units,
)
from .models import Response, WaterLevel

DEFAULT_BASE_URL = "https://api.tidesandcurrents.noaa.gov/api/prod"


class Client:
    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        client_options: dict[str, Any] | None = None,
    ):
        self._builder = Builder(base_url=base_url)
        self._client = httpx.Client(**(client_options or {}))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        return self._client.close()

    def _send_request(self, request: httpx.Request) -> httpx.Response:
        resp = self._client.send(request)
        return resp

    def get_water_level(
        self,
        station: str,
        date: (
            Date | int | BeginAndEndDates | BeginDateAndRange | EndDateAndRange
        ) = "today",
        units: Units = "metric",
        time_zone: TimeZone = "gmt",
        datum: Datum = "MLLW",
    ) -> WaterLevel:
        resp = self._send_request(
            self._builder.water_level(
                station=station,
                date=date,
                datum=datum,
                units=units,
                time_zone=time_zone,
            )
        )
        return Response[WaterLevel].model_validate(resp.json())


class AsyncClient:
    pass
