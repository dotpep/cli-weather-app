USE_ROUNDED_COORS: bool = False

OPENWEATHER_API = "YOUR_API_HERE"

OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
OPENWEATHER_URL_TEMPLATE = (
        OPENWEATHER_BASE_URL
        + "appid=" + OPENWEATHER_API + "&"
        "lang=ru&"
        "units=metric&"
        "lat={latitude}"
        "&lon={longitude}"
)

# TODO: Input Your API key, make it possible for the user to enter api from OpenWeatherMap API through the console
# OPENWEATHER_API = "YOUR_API_HERE"

# TODO: Choose Language Output, make it so that the user can enter in which language he wants to receive data himself
# from enum import Enum
# class OpenWeatherLanguageValues(Enum):
#     EN = "en"
#     RU = "ru"
# OPENWEATHER_URL = (
#     OPENWEATHER_BASE_URL
#     + f"appid={OPENWEATHER_API}&"
#     f"lang={OPENWEATHER_LANGUAGE}&"
#     "units=metric&"
#     "lat={latitude}&lon={longitude}"
# )

# TODO: Use GPS or Input, make it so that the user can select the option to track GPS in windows or Input city name
# USE_GPS: bool = NotImplemented
# OPENWEATHER_CITY_URL_TEMPLATE = (
#         OPENWEATHER_BASE_URL
#         + "appid=" + OPENWEATHER_API + "&"
#         "lang=ru&"
#         "units=metric&"
#         "q={city}"
# )

# TODO: write README.md file, guide for how to set weather.bat into PATH variable, requirements and etc.
# TODO: real-time updated weather information functionality, and updated coordinates.py
#  also attempt 3 times try to get GPS coordination and print "attempt 1 is Failed", "2 is Failed"...
