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

from geopy.distance import geodesic


# airports[ICAO] = (lat, lon)
airports: dict[str, tuple[float, float]] = {}

with open(f"data/airports.nav") as f:
    for l in f:
        pos = l.find("+")
        p = l[pos:].split(maxsplit=1)[0]
        name = l[4:8]
        n = p.split("+")
        lat = float(n[1]) / 10**5
        lon = float(n[2]) / 10**5
        airports[name] = (lat, lon)

print(f"Find {len(airports)} airports")

# earth[(area, waypoint)] = (lat, lon)
earth: dict[str, dict[str, set[tuple[float, float]]]] = {}

with open(f"data/earth_nav.dat") as f:
    for i, l in enumerate(f):
        if i < 3:
            continue
        data = (" " + l).split()
        # print(data)
        if len(data) < 11:
            continue
        lat = float(data[1])
        lon = float(data[2])
        area = data[9]
        waypoint = data[7]
        earth.setdefault(area, {}).setdefault(waypoint, set()).add((lat, lon))

print(f"Find {sum(map(lambda x: sum(map(len, x.values())), earth.values()))} waypoints")


# waypoints[(area, waypoint)] = (lat, lon)
waypoints: dict[str, dict[str, set[tuple[float, float]]]] = {}

with open(f"data/waypoints.txt") as f:
    for l in f:
        data = l.strip().split(",")
        # print(data)
        wp = data[0]
        lat = float(data[1])
        lon = float(data[2])
        area = data[3]
        # print(area, wp, lat, lon)
        waypoints.setdefault(area, {}).setdefault(wp, set()).add((lat, lon))

print(
    f"Find {sum(map(lambda x: sum(map(len, x.values())), waypoints.values()))} waypoints"
)


def get_closest(wps: set[tuple[float, float]], ap: tuple[float, float]):
    if not wps or not ap:
        return None
    return min(wps, key=lambda x: geodesic(x, ap).km)


def get_waypoint(airport: str, area: str, waypoint: str, wptype: str):
    airport = airport.strip().upper()
    area = area.strip().upper()
    waypoint = waypoint.strip().upper()
    wptype = wptype.strip().upper()
    match wptype:
        case "E" | "P":
            src = waypoints
        case "D":
            src = earth
        case _:
            print(wptype)
            return None
    wp = src.get(area, {}).get(waypoint, set())
    ap = airports.get(airport, tuple())
    print(src == waypoints, src == earth, wp, ap)
    return get_closest(wp, ap)


if __name__ == "__main__":

    # import json

    # with open("waypoints.json", "w") as f:
    #     json.dump(
    #         {k: {k2: list(v2) for k2, v2 in v.items()} for k, v in waypoints.items()}, f
    #     )

    # with open("earth.json", "w") as f:
    #     json.dump(
    #         {k: {k2: list(v2) for k2, v2 in v.items()} for k, v in earth.items()}, f
    #     )

    # with open("airports.json", "w") as f:
    #     json.dump(airports, f)

    ap = input("Enter Airport ICAO: ")
    area = input("Enter Area: ")
    waypoint = input("Enter Waypoint: ")
    wptype = input("Enter Waypoint Type (E/P/D): ")
    pos = get_waypoint(ap, area, waypoint, wptype)
    if pos is None:
        print("Not Found.")
    else:
        print(f"Position: {pos}")
