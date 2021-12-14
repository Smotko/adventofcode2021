from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console
from itertools import pairwise


inp = get_input(14, no_split=True)
# inp = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

template, rules = inp.split("\n\n")
rules = rules.splitlines()
rules = {r.split(" -> ")[0]: r.split(" -> ")[1] for r in rules}

template_counts = {pair: Counter(pair) for pair in rules.keys()}

for i in track(range(40)):
    new_counts = {}
    for pair, insert in rules.items():
        c = template_counts[pair[0] + insert] + template_counts[insert + pair[1]]
        c[insert] -= 1
        new_counts[pair] = c

    template_counts = new_counts

c = Counter()
for i in range(len(template) - 1):
    c += template_counts[template[i : i + 2]]
c -= Counter(template[1:-1])
console.log(c.most_common()[0][1] - c.most_common()[-1][1])
