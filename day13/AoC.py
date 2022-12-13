# /usr/bin/python3

import sys
from copy import deepcopy
from functools import cmp_to_key


def compare(a, b) -> int:
    if type(a) == type(b) == int:
        return -1 if a < b else 1 if a > b else 0
    if type(a) != type(b):
        if type(a) == int:
            a = [a]
        if type(b) == int:
            b = [b]
        return compare(a, b)
    for i in range(min(len(a), len(b))):
        res = compare(a[i], b[i])
        if res != 0:
            return res
    return -1 if len(a) < len(b) else 1 if len(a) > len(b) else 0


def part1(f: list) -> int:
    indices = []
    for i, l in enumerate(f):
        if compare(l[0], l[1]) == -1:
            indices.append(i+1)
    return sum(indices)


def part2(f: list) -> int:
    a, b = [[2]], [[6]]
    flat = [a, b]
    for g in f:
        flat += g
    flat = sorted(flat, key=cmp_to_key(compare))
    keys = [i + 1 for i, l in enumerate(flat) if l == a or l == b]
    return keys[0] * keys[1]


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [l for l in open(fname, 'r').readlines()]
    f = [l.splitlines() for l in ''.join(f).split('\n\n')]
    f = [[eval(l) for l in g] for g in f]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
