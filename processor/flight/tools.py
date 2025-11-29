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


def gethl(hl: str, h1: int):
    match hl.strip():
        case "+" | "J":
            return 2
        case "-":
            return 3
        case "B":
            return 4
        case _:
            return 1 if h1 else 0


def getspec(ch: str):
    match ch:
        case "A" | "B" | "C":
            return 1
        case "F":
            return 2
        case "M":
            return 3
        case _:
            return 0


def getturn(turn: str):
    match turn:
        case "L":
            return 1
        case "R":
            return 2
        case _:
            return 0
