# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re

SAND = (500, 0)

DIR_ORDER = [
    (0, 1),    # down first
    (-1, 1),    # then down-left
    (1, 1),    # then down-right
]


class Sand:
    def __init__(self, pos):
        self.pos = tuple(pos)

    def __add__(self, other):
        return Sand((self.pos[0] + other[0], self.pos[1] + other[1]))

    def __getitem__(self, key):
        return self.pos[key]

    def __iter__(self):
        return iter(self.pos)

    def __hash__(self):
        return hash(self.pos)

    def __eq__(self, other):
        return self.pos == other if isinstance(other, tuple) else self.pos == other.pos

    def __repr__(self):
        return 's' + str(self.pos)


def pointsOnLine(p1, p2) -> list:
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    res = None
    if dx == 0:
        res = [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)]
    elif dy == 0:
        res = [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]
    return res


def print_rocks(rocks: dict):
    minx = min(rocks.keys(), key=lambda x: x[0])[0]
    maxx = max(rocks.keys(), key=lambda x: x[0])[0]
    miny = min(rocks.keys(), key=lambda x: x[1])[1]
    maxy = max(rocks.keys(), key=lambda x: x[1])[1]
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print(rocks.get((x, y), '.'), end='')
        print()


def part1(f: list) -> int:
    rocks = {}
    for group in f:
        for line in zip(group[:-1], group[1:]):
            rocks.update({p: '#' for p in pointsOnLine(*line)})
    minpos = max(rocks.keys(), key=lambda x: x[1])[1]

    def simulate() -> bool:
        grain = Sand(SAND)
        while grain[1] <= minpos:
            lastpos = grain
            for d in DIR_ORDER:
                if grain + d not in rocks:
                    grain += d
                    break
            if grain == lastpos:
                rocks[grain] = 'o'
                return True
        return False
    while simulate():
        pass
    return sum(1 for v in rocks.values() if v == 'o')


def part2(f: list) -> int:
    rocks = {}
    for group in f:
        for line in zip(group[:-1], group[1:]):
            rocks.update({p: '#' for p in pointsOnLine(*line)})
    minpos = max(rocks.keys(), key=lambda x: x[1])[1] + 1

    def simulate() -> bool:
        grain = Sand(SAND)
        if grain + (0, 1) not in rocks:
            new_y = min([r[1]
                        for r in rocks.keys() if r[0] == grain[0]] + [minpos])
            grain = Sand((grain[0], new_y - 1))
        while True:
            lastpos = grain
            for d in DIR_ORDER:
                newgrain = grain + d
                if newgrain[1] <= minpos and newgrain not in rocks:
                    grain = newgrain
                    break
            if grain == lastpos:
                rocks[grain] = 'o'
                return True
        return False

    while (500, 0) not in rocks:
        simulate()

    return sum(1 for v in rocks.values() if v == 'o')


if __name__ == '__main__':
    r = re.compile(r'\d+,\d+')
    f = [[
        [int(x) for x in rock.split(',')]
        for rock in r.findall(l)]
        for l in open('/home/cole/AoC/AoC-2022/day14/input.txt', 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
