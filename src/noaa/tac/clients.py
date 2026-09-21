from typing import Any

import httpx

from ..exceptions import NoaaApiError
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
from .models import Response, WaterLevel, WaterTemperature

DEFAULT_BASE_URL = "https://api.tidesandcurrents.noaa.gov/api/prod"
DEFAULT_DATE = "today"
DEFAULT_TIME_ZONE = "gmt"
DEFAULT_UNIT = "metric"


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
        if resp.is_error:
            try:
                message = resp.json().get("error", {}).get("message", "unknown error")
            except Exception:  # noqa: BLE001
                message = str(resp.content)

            raise NoaaApiError(message=message.strip(), status_code=resp.status_code)

        try:
            message = resp.json()
        except Exception:  # noqa: BLE001
            raise NoaaApiError(message="not json response")

        error_message = message.get("error", {}).get("message")
        if error_message:
            raise NoaaApiError(message=error_message)

        return resp

    def get_water_level(
        self,
        station: str,
        date: (
            Date | int | BeginAndEndDates | BeginDateAndRange | EndDateAndRange
        ) = DEFAULT_DATE,
        units: Units = DEFAULT_UNIT,
        time_zone: TimeZone = DEFAULT_TIME_ZONE,
        datum: Datum = "MLW",
    ) -> Response[WaterLevel]:
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

    def get_water_temperature(
        self,
        station: str,
        date: (
            Date | int | BeginAndEndDates | BeginDateAndRange | EndDateAndRange
        ) = DEFAULT_DATE,
        units: Units = DEFAULT_UNIT,
        time_zone: TimeZone = DEFAULT_TIME_ZONE,
    ) -> Response[WaterTemperature]:
        resp = self._send_request(
            self._builder.water_temperature(
                station=station,
                date=date,
                units=units,
                time_zone=time_zone,
            )
        )
        return Response[WaterTemperature].model_validate(resp.json())


class AsyncClient:
    pass
