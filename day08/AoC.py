# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
import numpy as np

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider

# how many of these trees are visible from the edge?

directions = list(map(np.array, [
    (0, 1), # right
    (0, -1), # left
    (1, 0), # down
    (-1, 0), # up
]))


def part1(trees: np.ndarray) -> int:
    coords = set(map(tuple, product(range(trees.shape[0]), range(trees.shape[1]))))
    vis = np.zeros(f.shape)
    def visible(coord:np.ndarray) -> bool:
        # from the coord, look in all directions
        # if there is a tree in the way, it is not visible

        # get the height of the tree at the coord
        height = trees[coord]
        for direction in directions:
            # get the next coord in the direction
            new_coord = coord + direction
            while True:
                if tuple(new_coord) not in coords:
                    return True
                # if the new coord is a tree, it is not visible
                if trees[tuple(new_coord)] >= height:
                    break
                new_coord += direction
        return False
    for coord in coords:
        vis[coord] = visible(coord)
    # print(vis)
    return int(vis.sum())

def part2(trees: np.ndarray) -> int:
    coords = set(map(tuple, product(range(trees.shape[0]), range(trees.shape[1]))))
    vis = np.zeros(f.shape)

    def scenic(coord:np.ndarray) -> int:
        height = trees[coord]
        visible_by_direction = np.zeros(len(directions))
        for i, direction in enumerate(directions):
            # get the next coord in the direction
            new_coord = coord + direction
            while True:
                if tuple(new_coord) not in coords:
                    break
                visible_by_direction[i] += 1
                if trees[tuple(new_coord)] >= height:
                    break
                new_coord += direction
        return np.prod(visible_by_direction)
    for coord in coords:
        vis[coord] = scenic(coord)
    # print(vis)
    return int(max(vis.flatten()))


if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = np.array([
        np.array(list(map(int, l.strip())))
        for l in open(fname, 'r').readlines()
    ])
    # print(f)

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
