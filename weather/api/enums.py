from enum import StrEnum


class Exclude(StrEnum):
    CURRENT = "current"
    MINUTELY = "minutely"
    HOURLY = "hourly"
    DAILY = "daily"
    ALERTS = "alerts"


class Units(StrEnum):
    STANDARD = "standard"
    METRIC = "metric"
    IMPERIAL = "imperial"
