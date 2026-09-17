from http import HTTPMethod
from typing import Any, Literal

import httpx

type SortField = Literal["id", "name", "mindate", "maxdate", "datacoverage"]
type SortOrder = Literal["asc", "desc"]


class Builder:
    DATASETS_PATH = "/datasets"
    DATA_CATEGORIES_PATH = "/datacategories"
    DATA_TYPES_PATH = "/datatypes"
    LOCATION_CATEGORIES_PATH = "/locationcategories"
    LOCATIONS_PATH = "/locations"
    STATIONS_PATH = "/stations"
    DATA_PATH = "/data"

    def __init__(self, *, token: str, base_url: str):
        """Helper class to build httpx requests

        Helper class to build requests so that it can be used in both sync and async clients.
        """
        self.headers = {"token": token}
        self.base_url = base_url

    def dataset(self, id: str) -> httpx.Request:
        return self.make_request(path=f"{self.DATASETS_PATH}/{id}")

    def datasets(
        self,
        *,
        data_type_id: str | None = None,
        location_id: str | None = None,
        station_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.DATASETS_PATH,
            params=self.build_params(
                data_type_id=data_type_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            ),
        )

    def data_category(self, id: str) -> httpx.Request:
        return self.make_request(path=f"{self.DATA_CATEGORIES_PATH}/{id}")

    def data_categories(
        self,
        *,
        dataset_id: str | None = None,
        location_id: str | None = None,
        station_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.DATA_CATEGORIES_PATH,
            params=self.build_params(
                dataset_id=dataset_id,
                location_id=location_id,
                station_id=station_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            ),
        )

    def data_type(self, id: str) -> httpx.Request:
        return self.make_request(path=f"{self.DATA_TYPES_PATH}/{id}")

    def data_types(
        self,
        *,
        dataset_id: str | None = None,
        location_id: str | None = None,
        station_id: str | None = None,
        data_category_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.DATA_TYPES_PATH,
            params=self.build_params(
                dataset_id=dataset_id,
                location_id=location_id,
                station_id=station_id,
                data_category_id=data_category_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            ),
        )

    def location_category(self, id: str) -> httpx.Request:
        return self.make_request(path=f"{self.LOCATION_CATEGORIES_PATH}/{id}")

    def location_categories(
        self,
        *,
        dataset_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.LOCATION_CATEGORIES_PATH,
            params=self.build_params(
                dataset_id=dataset_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            ),
        )

    def location(self, id: str) -> httpx.Request:
        return self.make_request(path=f"{self.LOCATIONS_PATH}/{id}")

    def locations(
        self,
        *,
        dataset_id: str | None = None,
        location_category_id: str | None = None,
        data_category_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.LOCATIONS_PATH,
            params=self.build_params(
                dataset_id=dataset_id,
                location_category_id=location_category_id,
                data_category_id=data_category_id,
                start_date=start_date,
                end_date=end_date,
                sort_field=sort_field,
                sort_order=sort_order,
                limit=limit,
                offset=offset,
            ),
        )

    def station(self, id: str) -> httpx.Request:
        return self.make_request(path=f"{self.STATIONS_PATH}/{id}")

    def stations(
        self,
        *,
        dataset_id: str | None = None,
        location_id: str | None = None,
        data_category_id: str | None = None,
        data_type_id: str | None = None,
        extent: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.STATIONS_PATH,
            params=self.build_params(
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
            ),
        )

    def data(
        self,
        dataset_id: str,
        *,
        data_type_id: str | None = None,
        location_id: str | None = None,
        station_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        units: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        limit: int | None = None,
        offset: int | None = None,
        include_metadata: bool | None = None,
    ) -> httpx.Request:
        return self.make_request(
            path=self.DATA_PATH,
            params=self.build_params(
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
            ),
        )

    def make_request(
        self, path: str, params: dict[str, Any] | None = None
    ) -> httpx.Request:
        return httpx.Request(
            method=HTTPMethod.GET,
            url=f"{self.base_url}{path}",
            params=params,
            headers=self.headers,
        )

    @staticmethod
    def build_params(
        *,
        data_category_id: str | None = None,
        dataset_id: str | None = None,
        data_type_id: str | None = None,
        extent: str | None = None,
        location_id: str | None = None,
        location_category_id: str | None = None,
        station_id: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sort_field: SortField | None = None,
        sort_order: SortOrder | None = None,
        units: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        include_metadata: bool | None = None,
    ) -> dict[str, Any]:
        params = {}
        if data_category_id:
            params["datacategoryid"] = data_category_id

        if dataset_id:
            params["datasetid"] = dataset_id

        if data_type_id:
            params["datatypeid"] = data_type_id

        if extent:
            params["extent"] = extent

        if location_id:
            params["locationid"] = location_id

        if location_category_id:
            params["locationcategoryid"] = location_category_id

        if station_id:
            params["stationid"] = station_id

        if start_date:
            params["startdate"] = start_date

        if end_date:
            params["enddate"] = end_date

        if sort_field:
            params["sortfield"] = sort_field

        if sort_order:
            params["sortorder"] = sort_order

        if units:
            params["units"] = units

        if limit is not None:
            params["limit"] = limit

        if offset is not None:
            params["offset"] = offset

        if include_metadata:
            params["includemetadata"] = include_metadata

        return params
