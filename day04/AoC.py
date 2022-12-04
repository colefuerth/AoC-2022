# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy


def part1(f: list) -> int:
    return sum([
        r[0][0] <= r[1][0] <= r[1][1] <= r[0][1] or
        r[1][0] <= r[0][0] <= r[0][1] <= r[1][1]
        for r in f
    ])


def part2(f: list) -> int:
    return sum([
        not(r[0][1] < r[1][0] or r[1][1] < r[0][0])
        for r in f
    ])


if __name__ == "__main__":
    f = [tuple(tuple(int(a) for a in s.split('-'))
               for s in l.split(',')) for l in open(sys.argv[1], 'r')]

    print("Part 1:", part1(f))
    print("Part 2:", part2(f))
