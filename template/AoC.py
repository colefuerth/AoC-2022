# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
import numpy as np
from collections import defaultdict, Counter
import progressbar as pb
from termcolor import colored


def part1(f: list) -> int:
    pass


def part2(f: list) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]
    print(f)

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
