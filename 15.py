from rich.progress import track
import math
import statistics
import heapq
from dataclasses import dataclass
from collections import Counter, defaultdict

from utils import get_input, submit, console
from itertools import pairwise


inp = get_input(15)
# inp = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""".splitlines()


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    def __add__(self, p: "Point"):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point"):
        return Point(self.x - p.x, self.y - p.y)

    def __lt__(self, other):
        return self

    def neighbours(self) -> list["Point"]:
        return [
            self + Point(0, 1),
            self + Point(1, 0),
            self + Point(0, -1),
            self + Point(-1, 0),
        ]


@dataclass(frozen=True)
class Path:
    score = 0
    current_pos: Point | None = None
    visited = set()


size = len(inp)
grid = {}
end = None
for i, line in enumerate(inp):
    for j, v in enumerate(line):
        # grid[Point(j, i)] = int(v)
        for b in range(5):
            for c in range(5):
                grid[Point(j + size * b, i + size * c)] = (
                    int(v) + c + b if int(v) + c + b < 10 else (int(v) + c + b) % 10 + 1
                )
                end = Point(j + size * b, i + size * c)
# console.log(len(grid))


def print_out(grid):
    for line in range(len(inp) * 5):
        console.log(
            "".join(
                [
                    str(grid.get(Point(line, column), "X"))
                    for column in range(len(inp) * 5)
                ]
            )
        )


# print_out(grid)
visited = set()
start = Point(0, 0)
path = [start]


def dijkstra():
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    visited = set()
    queue = [(0, start)]
    while end not in visited:
        _, nex = heapq.heappop(queue)
        visited.add(nex)
        for n in nex.neighbours():
            if n in visited:
                continue
            if dist[n] > dist[nex] + grid.get(n, math.inf):
                dist[n] = dist[nex] + grid.get(n, math.inf)
                heapq.heappush(queue, (dist[nex] + grid.get(n, math.inf), n))
    console.log(dist[end])


dijkstra()
