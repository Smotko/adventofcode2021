from rich.progress import track
import math
import statistics
from dataclasses import dataclass
from collections import Counter, defaultdict
from utils import get_input, submit, console


inp = get_input(10)
# inp = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

score = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 3, "[": 57, "{": 1197, "<": 25137}
score2 = {")": 1, "]": 2, "}": 3, ">": 4, "(": 1, "[": 2, "{": 3, "<": 4}
opposite = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
    ")": "(",
    "]": "[",
    ">": "<",
    "}": "{",
}
# curr_score = 0
# for line in track(inp):
#     stack = []
#     for c in line:
#         # console.log(stack)
#         if c in ("[", "{", "<", "("):
#             stack.append(c)
#             continue
#         curr = stack.pop()
#         if curr == opposite[c]:
#             continue
#         curr_score += score[c]
#         break
# console.log(curr_score)

curr_score = 0
score_full2 = []
for line in track(inp):
    stack = []
    for c in line:
        if c in ("[", "{", "<", "("):
            stack.append(c)
            continue
        curr = stack.pop()
        if curr == opposite[c]:
            continue
        curr_score += score[c]
        break
    else:
        # Incomplete line:
        scr = 0
        for s in reversed(stack):
            scr *= 5
            scr += score2[s]
        score_full2.append(scr)
score_full2 = sorted(score_full2)
console.log(curr_score, score_full2[len(score_full2) // 2])
