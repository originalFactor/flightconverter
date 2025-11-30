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

from ..getpos import get_waypoint
from .base import FlightSegment
from .tools import getspec, getturn, gethl


class CD(FlightSegment):
    def __init__(self, ap: str, data: list[str]):
        self.record = "CD"
        self.waypoint = data[4]
        self.latitude, self.longitude = get_waypoint(
            ap, data[5], self.waypoint, data[6]
        ) or (0.0, 0.0)
        self.steering = getturn(data[9])
        self.nav_station = data[13] or " "
        self.azimuth = float(data[18]) / 10
        self.distance = float(data[19]) / 10
        self.heading = float(data[20]) / 10
        self.dme = float(data[21]) / 10
        self.height_1 = int(data[24])
        self.height_2 = int(data[25])
        self.height_lim = gethl(data[23], self.height_1)
        self.speed_1 = int(data[28])
        self.speed_2 = 0
        self.speed_lim = int(bool(self.speed_1))
        self.special = getspec(data[8][3])
        self.passthrough = int(data[8][1] == "Y")

    def __str__(self):
        return f"{self.record},{self.waypoint},{self.latitude},{self.longitude},{self.steering},{self.nav_station},{self.azimuth},{self.distance},{self.heading},{self.dme},{self.height_lim},{self.height_1},{self.height_2},{self.speed_lim},{self.speed_1},{self.speed_2},{self.special},{self.passthrough}"
