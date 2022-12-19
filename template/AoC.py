# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
import numpy as np
from collections import defaultdict, Counter
import progressbar as pb


class Blueprint:
    def __init__(self, ore:int, clay:int, obsidian:tuple, geode:tuple):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode


def part1(blueprints: list) -> int:
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
    blueprints = []
    for bp in re.split(r'Blueprint \d+: ', ' '.join(f)):
        fd = list(map(int, re.findall(r'\d+', bp)))
        ore, clay = fd[:2]
        obsidian = tuple(fd[2:4])
        geode = tuple(fd[4:6])
        blueprints.append(Blueprint(ore, clay, obsidian, geode))

    print('Part 1:', part1(blueprints))
    print('Part 2:', part2(blueprints))
