from dataclasses import dataclass

import tomllib


@dataclass(slots=True, frozen=True)
class Config:
    bot_token: str
    open_weather_token: str


def load_config() -> Config:
    with open("config.toml", "rb") as f:
        res = tomllib.load(f)

    return Config(**res)
