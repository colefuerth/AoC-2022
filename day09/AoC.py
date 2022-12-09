# /usr/bin/python3

import sys
from copy import deepcopy
import numpy as np

DIRECTIONS = {
    'R': np.array([0, 1]),  # RIGHT
    'L': np.array([0, -1]),  # LEFT
    'D': np.array([1, 0]),  # DOWN
    'U': np.array([-1, 0]),  # UP
}


def part1(f: list) -> int:
    head = np.array([0, 0])
    tail = np.array([0, 0])
    tail_points = set()
    tail_points.add(tuple(tail))
    for direction, steps in f:
        for _ in range(steps):
            head += DIRECTIONS[direction]
            if np.max(np.abs(head - tail)) > 1:
                tail += np.sign(head - tail)
                tail_points.add(tuple(tail))

    return len(tail_points)


def part2(f: list) -> int:
    knots = [np.array([0, 0]) for _ in range(10)]
    knot_points = set()
    knot_points.add(tuple(knots[-1]))
    for direction, steps in f:
        for _ in range(steps):
            knots[0] += DIRECTIONS[direction]
            for i in range(1, 10):
                if np.max(np.abs(knots[i-1] - knots[i])) > 1:
                    knots[i] += np.sign(knots[i-1] - knots[i])
                    if i == 9:
                        knot_points.add(tuple(knots[i]))

    return len(knot_points)


if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [
        l.strip().split(' ')
        for l in open(fname, 'r').readlines()
    ]
    f = [(d, int(i)) for d, i in f]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
