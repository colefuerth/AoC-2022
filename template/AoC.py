#/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re

# AoC template for python3

def part1(f:list) -> int:
    pass

def part2(f:list) -> int:
    pass

if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    regex = re.compile(r"(\d+)")
    f = [
        int(regex.findall(l)[0])
        for l in open(fname, 'r').readlines()
    ]
    print(f)

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
