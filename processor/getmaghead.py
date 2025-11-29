# Copyright (C) 2025 originalFactor
#
# This file is part of scripts.
#
# scripts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# scripts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with scripts.  If not, see <https://www.gnu.org/licenses/>.

from math import radians, degrees, sin, cos, atan2
from geomag import declination


def initial_bearing(f: tuple[float, float], t: tuple[float, float]):
    latf, lonf, latt, lont = map(radians, f + t)
    dlon = lont - lonf
    x = cos(latt) * sin(dlon)
    y = cos(latf) * sin(latt) - sin(latf) * cos(latt) * cos(dlon)
    return (degrees(atan2(x, y)) + 360) % 360


def magnetic_bearing(f: tuple[float, float], t: tuple[float, float]) -> float:
    return (initial_bearing(f, t) - declination(*f) + 360) % 360
