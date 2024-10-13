from typing import Sequence

from adaptix import Retort, dumper, name_mapping
from dataclass_rest import get
from dataclass_rest.client_protocol import FactoryProtocol
from dataclass_rest.http.aiohttp import AiohttpClient, AiohttpMethod
from dataclass_rest.http_request import HttpRequest

from weather.api.enums import Exclude, Units
from weather.api.models import Coordinates, Weather

BASE_URL = "http://api.openweathermap.org"


class OpenWeatherMethod(AiohttpMethod):
    client: "OpenWeatherClient"

    async def _pre_process_request(self, request: HttpRequest) -> HttpRequest:
        request.query_params = {
            k: v for k, v in request.query_params.items() if v is not None
        }
        request.query_params["appid"] = self.client._api_key
        return request


class OpenWeatherClient(AiohttpClient):
    method_class = OpenWeatherMethod

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        super().__init__(base_url=BASE_URL)

    def _init_request_args_factory(self) -> FactoryProtocol:
        return Retort(recipe=[dumper(Sequence[Exclude], lambda x: ",".join(x))])

    def _init_response_body_factory(self) -> FactoryProtocol:
        return Retort(
            recipe=[
                name_mapping(
                    Weather,
                    map=[
                        ("temp|feels_like|pressure|humidity", ("main", ...)),
                        ("description", ("weather", 0, ...)),
                    ],
                )
            ]
        )

    @get("geo/1.0/direct")
    async def get_coordinates(self, q: str, limit: int | None = 1) -> list[Coordinates]:
        pass

    @get("data/2.5/weather")
    async def get_current_weather(
        self,
        lat: float,
        lon: float,
        lang: str | None = None,
        units: Units | None = None,
    ) -> Weather:
        pass
