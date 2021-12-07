from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(7, no_split=True)
# inp = """16,1,2,0,4,2,7,1,2,14"""
inp = [int(i) for i in inp.split(",")]
target_pos = statistics.median(inp)
answer = int(sum([abs(i - target_pos) for i in inp]))
console.log(f"{answer}")

mn, mx = min(inp), max(inp)
min_fuel = math.inf
t = None

crab_distances = dict()
cur_distance = 0
for distance in range(mx + 1):
    cur_distance += distance
    crab_distances[distance] = cur_distance

for target_pos in track(range(mn, mx)):
    fuel = 0
    for crab in inp:
        distance = abs(crab - target_pos)
        fuel += crab_distances[distance]
    if fuel < min_fuel:
        min_fuel = fuel
        t = target_pos
console.log(min_fuel)
