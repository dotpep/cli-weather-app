# from enum import Enum
#
#
# class OpenWeatherLanguageValues(Enum):
#     EN = "en"
#     RU = "ru"


USE_ROUNDED_COORS: bool = True

OPENWEATHER_API = "YOUR_API_HERE"
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# OPENWEATHER_LANGUAGE = OpenWeatherLanguageValues.EN
#
# OPENWEATHER_URL = (
#     OPENWEATHER_BASE_URL
#     + f"appid={OPENWEATHER_API}&"
#     f"lang={OPENWEATHER_LANGUAGE}&"
#     "units=metric&"
#     "lat={latitude}&lon={longitude}"
# )

OPENWEATHER_URL_TEMPLATE = (
        OPENWEATHER_BASE_URL
        + "appid=" + OPENWEATHER_API + "&"
        "lang=ru&"
        "units=metric"
        "&lat={latitude}&lon={longitude}"
)
