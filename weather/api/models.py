from dataclasses import dataclass


@dataclass(slots=True)
class Coordinates:
    name: str
    lat: float
    lon: float
    country: str
    local_names: dict[str, str] | None = None
    state: str | None = None


@dataclass(slots=True)
class Weather:
    temp: float
    feels_like: float
    description: str
    pressure: float
    humidity: float
