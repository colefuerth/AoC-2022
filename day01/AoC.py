#/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy

# AoC template for python3

def part1(f:list) -> int:
    # sum each double newline separated group of integers
    # and return the max sum of all groups
    groups = [g.split() for g in ''.join(f).split('\n\n')]
    return max(sum(map(int, g)) for g in groups)

def part2(f:list) -> int:
    # same as part 1 but we sum the top 3 group sums
    groups = [g.split() for g in ''.join(f).split('\n\n')]
    return sum(sorted([sum(map(int, g)) for g in groups], reverse=True)[:3])

if __name__ == "__main__":
    # start by getting file as a list of strings
    f = [l for l in open(sys.argv[1], 'r')]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
