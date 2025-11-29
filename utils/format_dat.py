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

import sys

length: list[int] = [0]

with open(sys.argv[1]) as f:
    for line in f:
        l, r = line.split(":", 1)
        length[0] = max(length[0], len(l))
        rl = r.split(",")
        if len(length) - 1 < len(rl):
            length.extend([0] * (len(rl) - len(length) + 1))
        for i in range(len(rl)):
            length[i + 1] = max(length[i + 1], len(rl[i]))

with open(sys.argv[1]) as f:
    for line in f:
        l, r = line.split(":", 1)
        print(
            f'{l.rjust(length[0])}:{", ".join([x.rjust(length[i+1]) for i, x in enumerate(r.split(","))])}'
        )
