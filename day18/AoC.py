# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re


def tuple_add(a, b):
    return tuple(map(sum, zip(a, b)))


def part1(f: list) -> int:
    cube = set(map(tuple, f))
    sa = 0
    directions = [i for i in list(
        product([-1, 0, 1], repeat=3)) if i.count(0) == 2]
    for c, d in product(cube, directions):
        if tuple_add(c, d) not in cube:
            sa += 1
    return sa


def part2(f: list) -> int:
    cube = set(map(tuple, f))
    directions = [i for i in list(
        product([-1, 0, 1], repeat=3)) if i.count(0) == 2]

    # define a bounding box for the simulation, 2 units larger than the initial cube
    def shell(a, b):
        s = set()
        for x, y, z in product(range(a[0], b[0] + 1), range(a[1], b[1] + 1), range(a[2], b[2] + 1)):
            if x == a[0] or x == b[0] or y == a[1] or y == b[1] or z == a[2] or z == b[2]:
                s.add((x, y, z))
        return s
    edges = ((min(cube, key=lambda x: x[0])[0] - 2, min(cube, key=lambda x: x[1])[1] - 2, min(cube, key=lambda x: x[2])[
             2] - 2), (max(cube, key=lambda x: x[0])[0] + 2, max(cube, key=lambda x: x[1])[1] + 2, max(cube, key=lambda x: x[2])[2] + 2))
    bounds = shell(*edges)

    # open air can be a set one inside of the bounds
    open_air = shell(tuple_add(edges[0], (1, 1, 1)),
                     tuple_add(edges[1], (-1, -1, -1)))

    # keep simulating cycles until the air is stable
    for i in count():
        last_size = len(open_air)
        for a, d in product(deepcopy(open_air), directions):
            t = tuple_add(a, d)
            if t not in open_air and t not in bounds and t not in cube:
                open_air.add(t)
        if len(open_air) == last_size:
            break

    # count the surface area of the cube that is exposed to the open air
    sa = 0
    for c, d in product(cube, directions):
        if tuple_add(c, d) not in cube and tuple_add(c, d) in open_air:
            sa += 1
    return sa


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(x) for x in l.strip().split(',')]
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))
