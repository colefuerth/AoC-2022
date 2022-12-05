# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re


def part1(f: list, stacks: dict) -> int:
    for line in f:
        for i in range(line[0]):
            stacks[line[2]].append(stacks[line[1]].pop())
    return ''.join(s[-1] if s else '' for s in stacks.values())


def part2(f: list, stacks: dict) -> int:
    # now, we can move multiple at a time instead of just one
    for line in f:
        stacks[line[2]] += stacks[line[1]][-line[0]:]
        stacks[line[1]] = stacks[line[1]][:-line[0]]
    return ''.join(s[-1] if s else '' for s in stacks.values())


if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [str(l) for l in open(fname, 'r').readlines()]

    # start by finding the first row that contains any numbers; this is the end of the stacks definition
    stacks = None
    for i, l in enumerate(f):
        if re.search(r"\d", l):
            stacks = f[:i+1]
            f = f[i+2:]
            break

    # transpose stacks so that the enunmeration and stack bottom is first
    stacks = [''.join(s) for s in zip(*reversed(stacks))]
    # remove any stacks that do not start with a number, strip whitespace
    stacks = [s.strip() for s in stacks if re.search(r"\d", s)]
    # convert to a dict of stacks, enumerated by the integer first number
    stacks = {int(s[0]): list(s[1:]) for s in stacks}
    # print(stacks)

    # also pull out the three ints from each line in f
    f = [list(map(int, re.findall(r"\d+", l))) for l in f]
    # print(f)

    print("Part 1:", part1(deepcopy(f), deepcopy(stacks)))
    print("Part 2:", part2(deepcopy(f), deepcopy(stacks)))
