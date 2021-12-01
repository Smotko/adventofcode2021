import math
from utils import get_int_input


inp = get_int_input(1)
# inp = [
#     int(i)
#     for i in """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263""".splitlines()
# ]

prev = math.inf
cnt = 0
for i in inp:
    if i > prev:
        cnt += 1
    prev = i
print(cnt)

prev = math.inf
cnt = 0
for i, _ in enumerate(inp[:-2]):
    window = sum(inp[i : i + 3])
    if window > prev:
        cnt += 1
    prev = window
print(cnt)
