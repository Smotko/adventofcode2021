from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(13, no_split=True)
# inp = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""
coordinates, folds = inp.split("\n\n")


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __add__(self, p: "Point"):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point"):
        return Point(self.x - p.x, self.y - p.y)


def get_bounds(paper):
    max_x = max([p.x for p in paper.keys()]) + 1
    max_y = max([p.y for p in paper.keys()]) + 1
    return max_x, max_y


def print_out(paper):
    max_x = max([p.x for p in paper.keys()]) + 1
    max_y = max([p.y for p in paper.keys()]) + 1
    for line in range(max_y):
        console.log(
            "".join([paper.get(Point(column, line), ".") for column in range(max_x)])
        )


paper = dict()
for coordiante in coordinates.splitlines():
    x, y = coordiante.split(",")
    paper[Point(int(x), int(y))] = "#"

for fold in folds.splitlines():
    coo, val = fold.replace("fold along ", "").split("=")
    val = int(val)
    new_paper = dict()
    max_x, max_y = get_bounds(paper)
    for r in range(max_y):
        for c in range(max_x):
            if Point(c, r) not in paper:
                continue
            if coo == "y":
                if r < val:
                    new_paper[Point(c, r)] = "#"
                else:
                    new_paper[Point(c, val * 2 - r)] = "#"
            else:
                if c < val:
                    new_paper[Point(c, r)] = "#"
                else:
                    new_paper[Point(val * 2 - c, r)] = "#"

    # print_out(new_paper)
    console.log(len(new_paper))
    paper = new_paper

print_out(paper)
