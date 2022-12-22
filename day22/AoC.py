# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re

DIR = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]
TRN = {
    'L': -1,
    'R': 1,
}


def add(a: tuple, b: tuple) -> tuple:
    return (a[0] + b[0], a[1] + b[1])


def part1(board: dict, instructions: list) -> int:
    facing = 0
    x = min(board.keys(), key=lambda x: x[0])[0]
    y = min(k for k, v in board.items() if k[0] == x)[1]
    for v in instructions:
        if v in ['L', 'R']:
            facing = (facing + TRN[v]) % 4
        else:
            for _ in range(int(v)):
                t = add((x, y), DIR[facing])
                if t not in board:
                    t = (x, y)
                    while add(DIR[(facing + 2) % 4], t) in board:
                        t = add(DIR[(facing + 2) % 4], t)
                if board[t] == '#':
                    break
                x, y = t
    return 1000 * x + 4 * y + facing


def part2(f: list) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = open(fname, 'r').readlines()
    m, k = f[:-2], f[-1]
    board = {}
    for i, l in enumerate(m):
        for j, c in enumerate(l):
            if c in ['.', '#']:
                board[(i+1, j+1)] = c

    k = re.findall(r'(\d+|[RL])', k)

    print('Part 1:', part1(board, k))
    print('Part 2:', part2(f))
