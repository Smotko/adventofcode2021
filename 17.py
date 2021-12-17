from rich.progress import track
import math
import statistics
import heapq
from dataclasses import dataclass
from collections import Counter, defaultdict

# from utils import get_input, submit, console
from itertools import pairwise, product


inp = "target area: x=241..275, y=-75..-49"
# inp = "target area: x=20..30, y=-10..-5"


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __add__(self, p: "Point"):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point"):
        return Point(self.x - p.x, self.y - p.y)


target = inp.replace("target area: ", "").split(", ")
x_min, x_max = map(int, target[0].replace("x=", "").split(".."))
y_min, y_max = map(int, target[1].replace("y=", "").split(".."))
# console.log(x_min, x_max, y_min, y_max)
target = {Point(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)}


def step(pos, speed):
    pos += speed
    speed += Point(-1 if speed.x > 0 else 0, -1)
    return pos, speed


highest = -math.inf
cnt_hits = 0
for speed in track([Point(x, y) for x in range(1000) for y in range(-1000, 1000)]):
    ini_speed = speed
    pos = Point(0, 0)
    max_y = -math.inf
    while True:
        pos, speed = step(pos, speed)
        max_y = max(max_y, pos.y)
        if pos.y < y_min:
            max_y = -math.inf
            break
        if speed.x == 0 and pos.x < x_min:
            max_y = -math.inf
            break
        if pos.x > x_max:
            max_y = -math.inf
            break
        if pos in target:
            cnt_hits += 1
            break
    highest = max(max_y, highest)

print(highest, cnt_hits)
