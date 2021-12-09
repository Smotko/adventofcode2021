from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(8)
# inp = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()
out = [i.split(" | ")[1].split(" ") for i in inp]
inp = [i.split(" | ")[0].split(" ") for i in inp]
values = dict(
    a=8,
    b=6,
    c=8,
    d=7,
    e=4,
    f=9,
    g=7,
)
sums = dict()
for i, val in enumerate(
    [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]
):
    sums[sum([values[j] for j in val])] = i
# console.log(sums)
answer = 0
for curr_sig, curr_out in zip(inp, out):
    counts = Counter("".join(curr_sig))
    full_num = ""
    for num in curr_out:
        sm = sum([counts[n] for n in num])
        val = sums[sm]
        # console.log(num, val)
        full_num += str(val)
    answer += int(full_num)
console.log(answer)


# for i in inp:
#     for j in i:
#         console.log(sorted(j))
#     break
# # console.log(inp, out)
# cnt = 0
# for o in out:

#     for j in o:
#         if len(j) in (2, 3, 4, 7):
#             cnt += 1
# console.log(cnt)
