from rich.progress import track

from dataclasses import dataclass
from collections import Counter
from utils import get_input, submit, console


inp = get_input(4)
# inp = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7""".splitlines()

draw = [int(i) for i in inp[0].split(",")]
boards = []
board = {}
row = 0
for line in inp[1:]:
    if line == "":
        row = 0
        board = {}
        boards.append(board)
        continue
    for column, l in enumerate(line.split()):
        board[(row, column)] = int(l)
    row += 1


def play_bingo():
    drawn = set()
    for d in track(draw):
        drawn.add(d)
        for board in boards:
            for i in range(5):
                column = set(board[i, j] for j in range(5))
                row = set(board[j, i] for j in range(5))
                if len(column.intersection(drawn)) == 5:
                    console.log(
                        f"column winner: {sum([b for b in board.values() if b not in drawn])*d}"
                    )
                    return
                if len(row.intersection(drawn)) == 5:
                    console.log(
                        f"row winner: {sum([b for b in board.values() if b not in drawn])*d}"
                    )
                    return


def play_bingo_until_last():
    drawn = set()
    winners = set()
    for d in track(draw):
        drawn.add(d)
        for bnum, board in enumerate(boards):
            for i in range(5):
                column = set(board[i, j] for j in range(5))
                row = set(board[j, i] for j in range(5))
                if len(column.intersection(drawn)) == 5:

                    winners.add(bnum)
                if len(row.intersection(drawn)) == 5:

                    winners.add(bnum)
                if len(winners) == len(boards):
                    console.log(
                        f"LAST winner: {sum([b for b in board.values() if b not in drawn])*d}"
                    )
                    return


play_bingo()
play_bingo_until_last()
