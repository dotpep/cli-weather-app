from datetime import datetime
import json
# from json.decoder import JSONDecodeError
# import ssl
import urllib.request
# from urllib.error import URLError

from enum import Enum
from typing import Literal, NamedTuple, TypeAlias

import config
from coordinates import Coordinates
# from exceptions import ApiServiceError

Celsius: TypeAlias = int


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    """Requests weather in OpenWeatherMap API and returns it"""
    lat, lon = coordinates

    url = config.OPENWEATHER_URL_TEMPLATE.format(
        latitude=lat, longitude=lon
    )

    openweather_response = urllib.request.urlopen(url).read()
    openweather_dict = json.loads(openweather_response)

    temperature = openweather_dict["main"]["temp"]
    weather_type = openweather_dict["weather"][0]["id"]
    # sunrise = openweather_dict["sys"]["sunrise"]
    # sunset = openweather_dict["sys"]["sunset"]
    sunrise = datetime.fromtimestamp(openweather_dict["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(openweather_dict["sys"]["sunset"])
    city = openweather_dict["name"]

    return Weather(
        temperature=temperature,
        weather_type=weather_type,
        sunrise=sunrise,
        sunset=sunset,
        city=city,
    )


if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=55.75, longitude=37.65)))
