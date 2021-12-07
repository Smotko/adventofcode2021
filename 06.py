from rich.progress import track

from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(6)
inp = [int(i) for i in inp[0].split(",")]
# inp = [int(i) for i in """3,4,3,1,2""".split(",")]
counts = Counter(inp)
all_positions = dict()
for i in range(9):
    all_positions[i] = counts.get(i, 0)


for _ in track(range(256)):
    pos_0 = all_positions[0]
    new_positions = {i - 1: all_positions[i] for i in range(1, 9)}

    new_positions[6] += pos_0
    new_positions[8] = pos_0
    all_positions = new_positions
console.log(sum(all_positions.values()))
