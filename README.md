# noaa-api-py
[![PyPI version](https://img.shields.io/pypi/v/noaa-api-py)](https://pypi.org/project/noaa-api-py/)
![License](https://img.shields.io/pypi/l/noaa-api-py)
![Python versions](https://img.shields.io/pypi/pyversions/noaa-api-py)

Python client to access [NCDC NOAA](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) data

## Installation

To install the package

```bash
pip install noaa-api-py
```

## Usage

First, request a access token at NOAA [here](https://www.ncdc.noaa.gov/cdo-web/token).

Then, use the following to use the sync client.

```python
from noaa import Client

TOKEN = "<your-token-here>"

with Client(token=TOKEN) as client:
    data = client.get_datasets(limit=3)

print(data.model_dump_json(indent=2))
# {
#   "metadata": {
#     "result_set": {
#       "offset": 1,
#       "count": 11,
#       "limit": 3
#     }
#   },
#   "results": [
#     {
#       "uid": "gov.noaa.ncdc:C00861",
#       "min_date": "1763-01-01",
#       "max_date": "2026-09-14",
#       "name": "Daily Summaries",
#       "data_coverage": 1.0,
#       "id": "GHCND"
#     },
#     {
#       "uid": "gov.noaa.ncdc:C00946",
#       "min_date": "1763-01-01",
#       "max_date": "2026-09-01",
#       "name": "Global Summary of the Month",
#       "data_coverage": 1.0,
#       "id": "GSOM"
#     },
#     {
#       "uid": "gov.noaa.ncdc:C00947",
#       "min_date": "1763-01-01",
#       "max_date": "2026-01-01",
#       "name": "Global Summary of the Year",
#       "data_coverage": 1.0,
#       "id": "GSOY"
#     }
#   ]
# }
```

Similarly, to use the async client:

```python
import asyncio

from noaa import AsyncClient

TOKEN = "<your-token-here>"


async def main():
    async with AsyncClient(token=TOKEN) as client:
        data = await client.get_datasets(limit=3)

    print(data.model_dump_json(indent=2))


asyncio.run(main())
```

## License

[Apache License 2.0](LICENSE)
