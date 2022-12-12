# /usr/bin/python3

import sys
from itertools import product
from copy import deepcopy
import numpy as np

DIRECTIONS = np.array([
    np.array([0, 1]),
    np.array([0, -1]),
    np.array([1, 0]),
    np.array([-1, 0]),
])


def part1(S: np.ndarray, E: np.ndarray, mountain: dict) -> int:
    available = set(mountain.keys())
    available.remove(tuple(S))
    queue = [S]
    steps = 0
    while tuple(E) in available:
        steps += 1
        new_queue = []
        for d, q in product(DIRECTIONS, queue):
            newpos = tuple(q + d)
            if newpos in available:
                if mountain[newpos] - mountain[tuple(q)] <= 1:
                    new_queue.append(q + d)
                    available.remove(newpos)
        queue = new_queue
        if len(queue) == 0:
            break
    return steps if tuple(E) not in available else -1


def part2(S: np.ndarray, E: np.ndarray, mountain: dict, path: set = None) -> int:
    S = [s for s in mountain.keys() if mountain[s] == ord('a')]
    dist = [part1(np.array(s), E, mountain)
            for s in S if part1(s, E, mountain) != -1]
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
                start = np.array([i, j])
                mountain[(i, j)] = ord('a') - 1
            elif c == 'E':
                end = np.array([i, j])
                mountain[(i, j)] = ord('z') + 1
            else:
                mountain[(i, j)] = ord(c)

    print('Part 1:', part1(start, end, mountain))
    print('Part 2:', part2(start, end, mountain))
