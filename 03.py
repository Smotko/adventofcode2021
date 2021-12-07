from rich.progress import track

from dataclasses import dataclass
from collections import Counter
from utils import get_input, submit, console


inp = get_input(3)
inp = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".splitlines()
num_numerals = len(inp[0])

# gamma = ""
# epsilon = ""
# for i in track(range(num_numerals)):
#     cntr = Counter([v[i] for v in inp])
#     if cntr["0"] > cntr["1"]:
#         gamma += "0"
#         epsilon += "1"
#     else:
#         gamma += "1"
#         epsilon += "0"
# answer = int(gamma, 2) * int(epsilon, 2)

# console.log(f"1. {answer=}")

ignored = set()
numbers = set(inp)
for i in track(range(num_numerals)):
    cntr = Counter([v[i] for v in numbers.difference(ignored)])
    if cntr["0"] > cntr["1"]:
        ignore = "0"
    else:
        ignore = "1"
    for v in numbers.difference(ignored):
        if v[i] == ignore:
            ignored.add(v)
            if len(numbers.difference(ignored)) == 1:
                console.log(
                    "FOUND 1",
                    numbers.difference(ignored),
                    int(numbers.difference(ignored).pop(), 2),
                )
                break

ignored = set()
numbers = set(inp)
for i in track(range(num_numerals)):
    cntr = Counter([v[i] for v in numbers.difference(ignored)])

    if cntr["0"] > cntr["1"]:
        ignore = "1"
    else:
        ignore = "0"
    for v in numbers.difference(ignored):
        if v[i] == ignore:
            ignored.add(v)
            if len(numbers.difference(ignored)) == 1:
                console.log(
                    "FOUND",
                    numbers.difference(ignored),
                    int(numbers.difference(ignored).pop(), 2),
                )
                break


# submit(day=3, level=1, answer=answer)


# answer = None
# submit(day=3, level=2, answer=answer)
