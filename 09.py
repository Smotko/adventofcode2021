from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(9)
# inp = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""".splitlines()


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __add__(self, p: "Point"):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point"):
        return Point(self.x - p.x, self.y - p.y)


neighours = set([Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)])

heights = dict()
for i, vals in enumerate(inp):
    for j, val in enumerate(vals):
        heights[Point(i, j)] = int(val)

# def is_lower_than_neighbours(p):

answer = 0
low_points = []
for k in heights:
    for neigbour in neighours:
        if heights.get(k + neigbour, math.inf) <= heights[k]:
            break
    else:
        low_points.append(k)
        answer += 1 + heights[k]
console.log(f"{answer}")
sizes = []
for low_point in track(low_points):
    checked = set()
    to_check = {n + low_point for n in neighours}
    size = 0
    while to_check:
        check = to_check.pop()
        checked.add(check)
        if heights.get(check, 9) == 9:
            continue
        size += 1
        to_check |= {p + check for p in neighours if p + check not in checked}
    sizes.append(size)

console.log(f"{math.prod(sorted(sizes)[-3:])=}")
