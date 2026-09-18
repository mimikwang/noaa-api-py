from typing import Any

import httpx

from ..exceptions import NoaaApiError, NoaaNotFoundError
from .builder import Builder, SingleOrMultiple, SortField, SortOrder
from .models import (
    Collection,
    Data,
    DataCategory,
    Dataset,
    DataType,
    Location,
    LocationCategory,
    Station,
)

DEFAULT_BASE_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2"


class Client:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        client_options: dict[str, Any] | None = None,
    ):
        """Client to interact with the NCDC NOAA api

        The API is documented here: https://www.ncdc.noaa.gov/cdo-web/webservices/v2.

        Args:
            token (str): api token required for access. Follow instructions at https://www.ncdc.noaa.gov/cdo-web/token
                to request a token
            base_url (str): base url for the api, defaults to https://www.ncei.noaa.gov/cdo-web/api/v2
            client_options (dict[str, Any] | None): kwargs passed to the httpx client
        """
        self._builder = Builder(token=token, base_url=base_url)
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
            raise NoaaApiError(status_code=resp.status_code, message=str(resp.content))

        if not resp.json():
            raise NoaaNotFoundError()

        return resp

    def get_datasets(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        data_type_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        station_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
    ) -> Collection[Dataset]:
        resp = self._send_request(
            self._builder.datasets(
                data_type_id=data_type_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[Dataset].model_validate(resp.json())

    def get_dataset(self, id: str) -> Dataset:
        resp = self._send_request(self._builder.dataset(id))
        return Dataset.model_validate(resp.json())

    def get_data_categories(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        station_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[DataCategory]:
        resp = self._send_request(
            self._builder.data_categories(
                dataset_id=dataset_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[DataCategory].model_validate(resp.json())

    def get_data_category(self, id: str) -> DataCategory:
        resp = self._send_request(self._builder.data_category(id))
        return DataCategory.model_validate(resp.json())

    def get_data_types(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        data_category_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[DataType]:
        resp = self._send_request(
            self._builder.data_types(
                dataset_id=dataset_id,
                location_id=location_id,
                data_category_id=data_category_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[DataType].model_validate(resp.json())

    def get_data_type(self, id: str) -> DataType:
        resp = self._send_request(self._builder.data_type(id))
        return DataType.model_validate(resp.json())

    def get_location_categories(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[LocationCategory]:
        resp = self._send_request(
            self._builder.location_categories(
                dataset_id=dataset_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[LocationCategory].model_validate(resp.json())

    def get_location_category(self, id: str) -> LocationCategory:
        resp = self._send_request(self._builder.location_category(id))
        return LocationCategory.model_validate(resp.json())

    def get_locations(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_category_id: SingleOrMultiple | None = None,
        data_category_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[Location]:
        resp = self._send_request(
            self._builder.locations(
                dataset_id=dataset_id,
                location_category_id=location_category_id,
                data_category_id=data_category_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[Location].model_validate(resp.json())

    def get_location(self, id: str) -> Location:
        resp = self._send_request(self._builder.location(id))
        return Location.model_validate(resp.json())

    def get_stations(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        data_category_id: SingleOrMultiple | None = None,
        data_type_id: SingleOrMultiple | None = None,
        extent: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[Station]:
        resp = self._send_request(
            self._builder.stations(
                dataset_id=dataset_id,
                location_id=location_id,
                data_category_id=data_category_id,
                data_type_id=data_type_id,
                extent=extent,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[Station].model_validate(resp.json())

    def get_station(self, id: str) -> Station:
        resp = self._send_request(self._builder.station(id))
        return Station.model_validate(resp.json())

    def get_data(
        self,
        dataset_id: str,
        start_date: str,
        end_date: str,
        *,
        data_type_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        station_id: SingleOrMultiple | None = None,
        units: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
        include_metadata: bool | None = None,
    ) -> Collection[Data]:
        resp = self._send_request(
            self._builder.data(
                dataset_id=dataset_id,
                data_type_id=data_type_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                units=units,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
                include_metadata=include_metadata,
            )
        )
        return Collection[Data].model_validate(resp.json())


class AsyncClient:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        client_options: dict[str, Any] | None = None,
    ):
        """Async Client to interact with the NOAA api

        The API is documented here: https://www.ncdc.noaa.gov/cdo-web/webservices/v2.

        Args:
            token (str): api token required for access. Follow instructions at https://www.ncdc.noaa.gov/cdo-web/token
                to request a token
            base_url (str): base url for the api, defaults to https://www.ncei.noaa.gov/cdo-web/api/v2
            client_options (dict[str, Any] | None): kwargs passed to the httpx client
        """
        self._builder = Builder(token=token, base_url=base_url)
        self._client = httpx.AsyncClient(**(client_options or {}))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    async def aclose(self):
        return await self._client.aclose()

    async def _send_request(self, request: httpx.Request) -> httpx.Response:
        resp = await self._client.send(request)
        if resp.is_error:
            raise NoaaApiError(status_code=resp.status_code, message=str(resp.content))

        if not resp.json():
            raise NoaaNotFoundError()

        return resp

    async def get_datasets(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        data_type_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        station_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
    ) -> Collection[Dataset]:
        resp = await self._send_request(
            self._builder.datasets(
                data_type_id=data_type_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[Dataset].model_validate(resp.json())

    async def get_dataset(self, id: str) -> Dataset:
        resp = await self._send_request(self._builder.dataset(id))
        return Dataset.model_validate(resp.json())

    async def get_data_categories(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        station_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[DataCategory]:
        resp = await self._send_request(
            self._builder.data_categories(
                dataset_id=dataset_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[DataCategory].model_validate(resp.json())

    async def get_data_category(self, id: str) -> DataCategory:
        resp = await self._send_request(self._builder.data_category(id))
        return DataCategory.model_validate(resp.json())

    async def get_data_types(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        data_category_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[DataType]:
        resp = await self._send_request(
            self._builder.data_types(
                dataset_id=dataset_id,
                location_id=location_id,
                data_category_id=data_category_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[DataType].model_validate(resp.json())

    async def get_data_type(self, id: str) -> DataType:
        resp = await self._send_request(self._builder.data_type(id))
        return DataType.model_validate(resp.json())

    async def get_location_categories(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[LocationCategory]:
        resp = await self._send_request(
            self._builder.location_categories(
                dataset_id=dataset_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[LocationCategory].model_validate(resp.json())

    async def get_location_category(self, id: str) -> LocationCategory:
        resp = await self._send_request(self._builder.location_category(id))
        return LocationCategory.model_validate(resp.json())

    async def get_locations(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_category_id: SingleOrMultiple | None = None,
        data_category_id: SingleOrMultiple | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[Location]:
        resp = await self._send_request(
            self._builder.locations(
                dataset_id=dataset_id,
                location_category_id=location_category_id,
                data_category_id=data_category_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[Location].model_validate(resp.json())

    async def get_location(self, id: str) -> Location:
        resp = await self._send_request(self._builder.location(id))
        return Location.model_validate(resp.json())

    async def get_stations(
        self,
        *,
        dataset_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        data_category_id: SingleOrMultiple | None = None,
        data_type_id: SingleOrMultiple | None = None,
        extent: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Collection[Station]:
        resp = await self._send_request(
            self._builder.stations(
                dataset_id=dataset_id,
                location_id=location_id,
                data_category_id=data_category_id,
                data_type_id=data_type_id,
                extent=extent,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            )
        )
        return Collection[Station].model_validate(resp.json())

    async def get_station(self, id: str) -> Station:
        resp = await self._send_request(self._builder.station(id))
        return Station.model_validate(resp.json())

    async def get_data(
        self,
        dataset_id: str,
        start_date: str,
        end_date: str,
        *,
        data_type_id: SingleOrMultiple | None = None,
        location_id: SingleOrMultiple | None = None,
        station_id: SingleOrMultiple | None = None,
        units: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
        include_metadata: bool | None = None,
    ) -> Collection[Data]:
        resp = await self._send_request(
            self._builder.data(
                dataset_id=dataset_id,
                data_type_id=data_type_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                units=units,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
                include_metadata=include_metadata,
            )
        )
        return Collection[Data].model_validate(resp.json())
