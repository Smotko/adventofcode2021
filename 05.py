from rich.progress import track

from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, s: str) -> "Point":
        x, y = s.split(",")
        return Point(int(x), int(y))

    def __add__(self, p: "Point"):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point"):
        return Point(self.x - p.x, self.y - p.y)

    def step(self, p1: "Point"):
        s = self - p1
        return Point(
            0 if s.x == 0 else -1 * int(s.x / abs(s.x)),
            0 if s.y == 0 else int(-1 * s.y / abs(s.y)),
        )


inp = get_input(5)
# inp = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".splitlines()


def get_answer(ignore_diagonal: bool):
    grid = defaultdict(int)
    for line in track(inp):
        first, second = line.split(" -> ")
        p1, p2 = Point.from_str(first), Point.from_str(second)
        if ignore_diagonal and p1.x != p2.x and p1.y != p2.y:
            continue
        while True:
            grid[p1] += 1
            if p1 == p2:
                break
            p1 = p1 + p1.step(p2)
    return sum(1 for i in grid.values() if i > 1)


console.log("Part 1", get_answer(ignore_diagonal=True))
console.log("Part 2", get_answer(ignore_diagonal=False))
