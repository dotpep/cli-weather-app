import json
from datetime import datetime
from pathlib import Path
from typing import TypedDict, Protocol

from weather_api_service import Weather
from weather_formatter import format_weather

# TODO: Refactor my Interface and Implementation of Interface or Abstract class in python for IWeatherStorage
# from abc import


class IWeatherStorage(Protocol):
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage(IWeatherStorage):
    """Store weather in plain text file"""

    def __init__(self, file: Path):
        self._txt_file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._txt_file, "a") as file:
            file.write(f"{now}\n{formatted_weather}\n")


class HistoryRecord(TypedDict):
    date: str
    weather: str


class JSONFileWeatherStorage(IWeatherStorage):
    def __init__(self, file: Path):
        self._json_file = file
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": format_weather(weather)
        })
        self._write(history)

    def _init_storage(self) -> None:
        if not self._json_file.exists():
            self._json_file.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._json_file, "r") as file:
            data = json.load(file)
            return data

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._json_file, "w") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)


def save_weather(weather: Weather, storage: IWeatherStorage) -> None:
    """Saved weather in the storage"""
    storage.save(weather)


if __name__ == "__main__":
    import coordinates as _coors
    import weather_api_service as _api_service
    from coordinates import Coordinates

    _coordinates = _coors.get_gps_coordinates()
    _weather_gps = _api_service.get_weather(_coordinates)
    _weather_writen = _api_service.get_weather(Coordinates(latitude=55.75, longitude=37.65))
    _weather_input_city = NotImplemented

    _weather = _weather_gps

    def _save_weather(weather: Weather) -> None:
        save_weather(
            weather,
            JSONFileWeatherStorage(Path.cwd() / "history.json")
        )


    _save_weather(_weather)


    def _read_saved_weather() -> str:
        with open("history.json", "r") as file:
            data = file.read()
            return data


    print(_read_saved_weather())
