from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(11)
# inp = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""".splitlines()
# inp = """11111
# 19991
# 19191
# 19991
# 11111""".splitlines()


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __add__(self, p: "Point"):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point"):
        return Point(self.x - p.x, self.y - p.y)


neighours = set(
    [
        Point(0, 1),
        Point(0, -1),
        Point(1, 0),
        Point(-1, 0),
        Point(-1, 1),
        Point(1, -1),
        Point(1, 1),
        Point(-1, -1),
    ]
)


def flash(p, grid):
    for neighbour in neighours:
        if p + neighbour not in grid:
            continue
        grid[p + neighbour] += 1


def simulate(grid):
    flashes = 0
    for g in grid:
        grid[g] += 1

    flashed = set()
    cont = True
    while cont:
        cont = False
        for g in grid:
            if grid[g] > 9 and g not in flashed:
                flash(g, grid)
                flashed.add(g)
                cont = True

    for g in grid:
        if grid[g] > 9:
            grid[g] = 0
    return len(flashed)


def print_out(grid):
    for line in range(len(inp)):
        console.log(
            "".join([str(grid[Point(line, column)]) for column in range(len(inp))])
        )


grid = dict()
for i, line in enumerate(inp):
    for j, column in enumerate(line):
        grid[Point(i, j)] = int(column)

total = 0
for i in range(10000000000000):
    # console.log(i + 1)
    total += simulate(grid)
    for g in grid:
        if grid[g] != 0:
            break
    else:
        console.log(i + 1)
        break
    # print_out(grid)

console.log(total)
