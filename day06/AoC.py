# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re

# AoC template for python3


def part1(s:str) -> int:
    # sliding window of 4 characters at a time
    for i in range(0, len(s)-4):
        if len(set(s[i:i+4])) == 4:
            return i + 4
    return -1


def part2(s:str) -> int:
    # sliding window of 14 characters at a time
    for i in range(0, len(s)-14):
        if len(set(s[i:i+14])) == 14:
            return i + 14
    return -1


if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = open(fname, 'r').readlines()[0].strip()
    # print(f) if len(f) < 10 else None

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
