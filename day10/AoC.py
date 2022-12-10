# /usr/bin/python3

import sys
from copy import deepcopy
import numpy as np


def part1(f: list) -> int:
    X = 1
    cycles = 0
    points = []
    for line in f:
        if line == 'noop':
            cycles += 1
            if (cycles - 20) % 40 == 0:
                points.append(cycles * X)
        else:
            for _ in range(2):
                cycles += 1
                if (cycles - 20) % 40 == 0:
                    points.append(cycles * X)
            X += int(line.split(' ')[1])
    return sum(points)


def part2(f: list) -> str:
    X = 1
    cycles = - 1
    screen = np.zeros((6, 40))
    for line in f:
        if line == 'noop':
            cycles += 1
            screen[cycles // 40, cycles % 40] = (abs(X - cycles % 40) < 2)
        else:
            for _ in range(2):
                cycles += 1
                screen[cycles // 40, cycles % 40] = (abs(X - cycles % 40) < 2)
            X += int(line.split(' ')[1])
    return '\n' + '\n'.join([''.join(['#' if x else '.' for x in row]) for row in screen])


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
