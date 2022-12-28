# /usr/bin/python3

import sys
from itertools import product, count
from copy import deepcopy

# (x, y) = (row, col)


def add_tup(a, b) -> tuple:
    return a[0] + b[0], a[1] + b[1]


def print_elves(elves: set):
    xmin = min(elves, key=lambda x: x[0])[0]
    xmax = max(elves, key=lambda x: x[0])[0]
    ymin = min(elves, key=lambda x: x[1])[1]
    ymax = max(elves, key=lambda x: x[1])[1]
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            if (i, j) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()


def part1(elves: set) -> int:
    ADJ = list(product([-1, 0, 1], repeat=2))
    ADJ.remove((0, 0))

    DIR = [
        [(-1, 0), [(-1, 0), (-1, 1), (-1, -1)]],  # N
        [(1, 0), [(1, 0), (1, 1), (1, -1)]],  # S
        [(0, -1), [(0, -1), (1, -1), (-1, -1)]],  # W
        [(0, 1), [(0, 1), (1, 1), (-1, 1)]],  # E
    ]

    for _ in range(10):
        # first half of round, find proposals
        proposals = {}
        for elf in elves:
            if any(add_tup(elf, a) in elves for a in ADJ):
                for d, fan in DIR:
                    if not any(add_tup(elf, dd) in elves for dd in fan):
                        proposals[elf] = add_tup(elf, d)
                        break
        # second half, apply proposals if no collision
        plist = list(proposals.values())
        proposals = {k: v for k, v in proposals.items() if plist.count(v) == 1}
        for elf, newelf in proposals.items():
            elves.remove(elf)
            elves.add(newelf)
        DIR.append(DIR.pop(0))

    xmin = min(elves, key=lambda x: x[0])[0]
    xmax = max(elves, key=lambda x: x[0])[0]
    ymin = min(elves, key=lambda x: x[1])[1]
    ymax = max(elves, key=lambda x: x[1])[1]
    rectangle = (xmax - xmin + 1) * (ymax - ymin + 1)
    return rectangle - len(elves)


def part2(elves: set) -> int:

    ADJ = list(product([-1, 0, 1], repeat=2))
    ADJ.remove((0, 0))

    DIR = [
        [(-1, 0), [(-1, 0), (-1, 1), (-1, -1)]],  # N
        [(1, 0), [(1, 0), (1, 1), (1, -1)]],  # S
        [(0, -1), [(0, -1), (1, -1), (-1, -1)]],  # W
        [(0, 1), [(0, 1), (1, 1), (-1, 1)]],  # E
    ]
    c = count()
    for _ in c:
        # first half of round, find proposals
        proposals = {}
        for elf in elves:
            if any(add_tup(elf, a) in elves for a in ADJ):
                for d, fan in DIR:
                    if not any(add_tup(elf, dd) in elves for dd in fan):
                        proposals[elf] = add_tup(elf, d)
                        break
        # second half, apply proposals if no collision
        plist = list(proposals.values())
        proposals = {k: v for k, v in proposals.items() if plist.count(v) == 1}
        if len(proposals) == 0:
            return next(c)
        for elf, newelf in proposals.items():
            elves.remove(elf)
            elves.add(newelf)
        DIR.append(DIR.pop(0))

    return next(c)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

    elves = set()
    for i, l in enumerate(open(fname, 'r').readlines()):
        for j, c in enumerate(l.strip()):
            if c == '#':
                elves.add((i, j))

    print('Part 1:', part1(deepcopy(elves)))
    print('Part 2:', part2(deepcopy(elves)))
