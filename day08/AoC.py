# /usr/bin/python3

import sys
from itertools import product
from copy import deepcopy
import numpy as np

DIRECTIONS = list(map(np.array, [
    (0, 1), # right
    (0, -1), # left
    (1, 0), # down
    (-1, 0), # up
]))

def traverse(coord, direction) -> tuple:
    coord = np.array(coord)
    direction = np.array(direction)
    while True:
        coord += direction
        yield tuple(coord)


def part1(trees: np.ndarray) -> int:
    coords = set(map(tuple, product(range(trees.shape[0]), range(trees.shape[1]))))
    vis = np.zeros(f.shape)
    def visible(coord:tuple) -> bool:
        height = trees[coord]
        for direction in DIRECTIONS:
            for new_coord in traverse(coord, direction):
                if new_coord not in coords:
                    return True
                if trees[new_coord] >= height:
                    break
        return False
    for coord in coords:
        vis[coord] = visible(coord)
    return int(vis.sum())

def part2(trees: np.ndarray) -> int:
    coords = set(map(tuple, product(range(trees.shape[0]), range(trees.shape[1]))))
    vis = np.zeros(f.shape)

    def scenic(coord:np.ndarray) -> int:
        height = trees[coord]
        visible_by_direction = np.zeros(len(DIRECTIONS))
        for i, direction in enumerate(DIRECTIONS):
            for new_coord in traverse(coord, direction):
                if new_coord not in coords:
                    break
                visible_by_direction[i] += 1
                if trees[new_coord] >= height:
                    break
        return np.prod(visible_by_direction)
    for coord in coords:
        vis[coord] = scenic(coord)
    return int(max(vis.flatten()))


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = np.array([
        np.array(list(map(int, l.strip())))
        for l in open(fname, 'r').readlines()
    ])

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
