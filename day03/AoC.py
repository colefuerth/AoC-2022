#/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy

# AoC template for python3

def part1(f:list) -> int:
    # start by splitting each rucksack string into two, and convert each half into a set of characters
    f = [(set(s[:len(s)//2]), set(s[len(s)//2:])) for s in f]
    common = [''.join(list(a.intersection(b))) for a, b in f]
    priorities = {c: i+1 for i, c in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    return sum([priorities[c] for c in common])

def part2(f:list) -> int:
    # each group of three rucksacks has one common character
    # we can find the common character by finding the intersection of the three sets
    f = [set(s) for s in f]
    common = [''.join(list(a.intersection(b, c))) for a, b, c in zip(f[::3], f[1::3], f[2::3])]
    priorities = {c: i+1 for i, c in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    return sum([priorities[c] for c in common])

if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.strip() for l in open(fname, 'r')]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
