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

from io import TextIOWrapper
from .line import process_line


def process_dat(db: dict, f: TextIOWrapper):
    for l in f:
        process_line(db, l)
