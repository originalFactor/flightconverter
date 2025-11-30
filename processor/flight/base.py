# Copyright (C) 2025 originalFactor
#
# This file is part of flightconverter.
#
# flightconverter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# flightconverter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with flightconverter.  If not, see <https://www.gnu.org/licenses/>.

from dataclasses import dataclass


@dataclass
class FlightSegment:
    record: str  # fixed
    height_lim: int  # data[23]
    height_1: int  # data[24]
    height_2: int  # data[25]
    speed_lim: int  # bool(speed_1)
    speed_1: int  # data[28]
    speed_2: int  # fixed
    special: int  # data[8][3]
    passthrough: int  # data[8][1]
    steering: int | None = None  # data[9]
    heading: float | None = None  # data[20]
    dme: float | None = None
    sweeping: float | None = None
    start_radius: float | None = None
    azimuth: float | None = None  # data[18]
    distance: float | None = None  # data[19]
    waypoint: str | None = None  # data[4]
    latitude: float | None = None  # calc
    longitude: float | None = None  # calc
    nav_station: str | None = None  # data[13]
    distance_2: float | None = None
    radial: float | None = None
    course: float | None = None
