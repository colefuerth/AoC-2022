# /usr/bin/python3

import sys
from itertools import product
from copy import deepcopy

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def part1(S: tuple, E: tuple, mountain: dict) -> int:
    available = set(mountain.keys())
    available.remove(S)
    queue = set([S])
    steps = 0
    while E in available:
        steps += 1
        new_queue = set([
            (q[0] + d[0], q[1] + d[1])
            for q, d in product(queue, DIRECTIONS)
            if (q[0] + d[0], q[1] + d[1]) in available
            and mountain[(q[0] + d[0], q[1] + d[1])] <= mountain[q] + 1
        ])
        available -= new_queue
        queue = new_queue
        if len(queue) == 0:
            break
    return steps if E not in available else -1


def part2(S: tuple, E: tuple, mountain: dict) -> int:
    S = [s for s in mountain.keys() if mountain[s] == ord('a')]
    dist = [part1(s, E, mountain) for s in S if part1(s, E, mountain) != -1]
    return min(dist)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]

    mountain = {}
    start = None
    end = None
    for i, row in enumerate(f):
        for j, c in enumerate(row):
            if c == 'S':
                start = (i, j)
                mountain[(i, j)] = ord('a')
            elif c == 'E':
                end = (i, j)
                mountain[(i, j)] = ord('z')
            else:
                mountain[(i, j)] = ord(c)

    print('Part 1:', part1(start, end, mountain))
    print('Part 2:', part2(start, end, mountain))
