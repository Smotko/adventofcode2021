from dataclasses import dataclass
from utils import get_input


inp = get_input(2)
# inp = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# """.splitlines()

lines = []
for line in inp:
    direction, amount = line.split()
    lines.append((direction, int(amount)))

@dataclass
class Position:
    horizontal: int
    depth: int
    aim: int | None = None

cur_pos = Position(horizontal=0, depth=0)
for direction, amount in lines:
    match direction:
        case "down":
            cur_pos.depth += amount
        case "up":
            cur_pos.depth -= amount
        case "forward":
            cur_pos.horizontal += amount
print(cur_pos.horizontal * cur_pos.depth)


cur_pos = Position(horizontal=0, depth=0, aim=0)
for direction, amount in lines:
    match direction:
        case "down":
            cur_pos.aim += amount
        case "up":
            cur_pos.aim -= amount
        case "forward":
            cur_pos.depth += cur_pos.aim * amount
            cur_pos.horizontal += amount
print(cur_pos.horizontal * cur_pos.depth)
