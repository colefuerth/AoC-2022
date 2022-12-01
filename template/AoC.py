#/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy

# AoC template for python3

def part1(f:list) -> int:
    pass

def part2(f:list) -> int:
    pass

if __name__ == "__main__":
    # start by getting file as a list of strings
    f = [l.strip() for l in open(sys.argv[1], 'r')]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
