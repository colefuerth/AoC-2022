# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re

SDIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
DIRS = list(SDIRS.values())
DIRS.append((0, 0))


def add_tup(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul_tup(a, b):
    return a[0] * b[0], a[1] * b[1]


def simulate(walls: set, snowflake: list, size: tuple) -> None:
    for i, (pos, d) in enumerate(snowflake):
        dx, dy = SDIRS[d]
        pos[0] += dx
        pos[1] += dy
        if tuple(pos) in walls:
            if d == '>':
                pos[1] -= size[1] - 2
            elif d == '<':
                pos[1] += size[1] - 2
            elif d == '^':
                pos[0] += size[0] - 2
            elif d == 'v':
                pos[0] -= size[0] - 2


def print_mountain(elves:set, snowflake:list, walls:set, size:tuple):
    sf2 = [tuple(p) for p, _ in snowflake]
    for i in range(size[0]):
        for j in range(size[1]):
            if (i, j) in walls:
                print('#', end='')
            elif (i, j) in elves:
                print('E', end='')
            elif (i, j) in sf2:
                if sf2.count((i, j)) > 1:
                    print(sf2.count((i, j)), end='')
                else:
                    print(snowflake[sf2.index((i, j))][1], end='')
            else:
                print('.', end='')
        print()
    print()


def part1(f: list) -> int:
    walls, snowflake, start, end, size = f
    queue = set([start])
    print_mountain(queue, snowflake, walls, size)
    c = count()
    for _ in c:
        simulate(walls, snowflake, size)
        sfset = set(tuple(p) for p, _ in snowflake)
        new_queue = set()
        for p, d in product(queue, DIRS):
            new_p = add_tup(p, d)
            if new_p in walls or new_p in sfset:
                continue
            if new_p == end:
                return next(c)
            new_queue.add(new_p)
        queue = new_queue
        print_mountain(queue, snowflake, walls, size)

        # 153 is too low


def part2(f: list) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [l.strip() for l in open(fname, 'r').readlines()]
    start = (0, f[0].index('.'))
    end = (len(f) - 1, f[-1].index('.'))
    snowflake = []
    walls = set()
    for i, l in enumerate(f):
        for j, c in enumerate(l):
            if c in '><^v':
                snowflake.append([[i, j], c])
            elif c == '#':
                walls.add((i, j))
    size = (len(f), len(f[0]))
    print('Part 1:', part1(deepcopy([walls, snowflake, start, end, size])))
    print('Part 2:', part2(f))
