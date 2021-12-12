from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(12)
# inp = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""".splitlines()

graph = defaultdict(set)

for line in inp:
    n1, n2 = line.split("-")
    graph[n1].add(n2)
    graph[n2].add(n1)


def is_lower(node):
    return node == node.lower()


def visit(node, path):
    for node in graph[node]:
        # console.log(path, node, is_lower(node), node in path)
        if is_lower(node) and node in path:
            continue
        new_path = path + [node]

        path_str = ",".join(new_path)
        if path_str in paths:
            continue
        paths.add(path_str)
        if node != "end":
            visit(node, new_path)


def visit2(node, path):
    for node in graph[node]:
        # console.log(path, node, is_lower(node), node in path)
        if is_lower(node) and node in path and node:
            if node == "start":
                continue
            cntr = Counter(path)
            is_lower_twice = [c for c in cntr if is_lower(c) and cntr[c] >= 2]
            # console.log(f"{is_lower_twice=}, {cntr=}")
            if is_lower_twice:
                continue
        new_path = path + [node]

        path_str = ",".join(new_path)
        if path_str in paths:
            continue
        paths.add(path_str)
        if node != "end":
            visit2(node, new_path)


paths = set()

# visit("start", ["start"])
# console.log([p for p in paths if "end" in p])
# console.log(len([p for p in paths if "end" in p]))
paths = set()

visit2("start", ["start"])
# console.log([p for p in paths if "end" in p])
console.log(len([p for p in paths if "end" in p]))
