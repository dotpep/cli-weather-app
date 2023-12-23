import subprocess
import time
from typing import NamedTuple

import config
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    wait_time = 0
    accuracy = 3

    powershell_outputs = _get_gps_data_from_powershell(wait_time, accuracy)
    current_coordinates = _parse_coordinate(powershell_outputs)

    if config.USE_ROUNDED_COORS:
        return _round_coordinates(current_coordinates)

    return current_coordinates


def _get_gps_data_from_powershell(wait_time: int, accuracy: int) -> list:
    time.sleep(wait_time)
    powershell_command = [
        'powershell',
        'add-type -assemblyname system.device; '
        '$loc = new-object system.device.location.geocoordinatewatcher;'
        '$loc.start(); '
        'while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied")) '
        '{start-sleep -milliseconds 100}; '
        '$acc = %d; '
        'while($loc.position.location.horizontalaccuracy -gt $acc) '
        '{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)}; '
        '$loc.position.location.latitude; '
        '$loc.position.location.longitude; '
        '$loc.position.location.horizontalaccuracy; '
        '$loc.stop()' % (accuracy)
    ]

    process_outputs, _ = subprocess.Popen(
        powershell_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    ).communicate()

    return [item.strip() for item in process_outputs.split('\n')]


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    return coordinates._replace(  # replace Coordinates
        latitude=round(coordinates.latitude, 2),  # minimum rounded decimal value must equal to 2
        longitude=round(coordinates.longitude, 2)  # else OpenWeatherAPI may return incorrect address, city
    )


def _parse_coordinate(outputs: list) -> Coordinates:
    if any(item in {'NaN', None} for item in outputs):
        raise CantGetCoordinates("Unable to retrieve GPS data. Check if GPS is enabled on your device.")
    try:
        latitude: float = float(outputs[0])
        longitude: float = float(outputs[1])
        radius: int = int(outputs[2])
    except (ValueError, IndexError):
        raise CantGetCoordinates

    return Coordinates(latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    coordination = get_gps_coordinates()
    print("Coordinate latitude: ", coordination.latitude)
    print("Coordinate longitude: ", coordination.longitude)
