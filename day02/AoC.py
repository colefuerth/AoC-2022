#/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy

# AoC template for python3

# A for rock, B for paper, C for scissors on column A
# X for rock, Y for paper, Z for scissors on column B
# score is the sum of scores for each round / row
# score is what you selected, 1 for rock, 2 for paper, 3 for scissors, plus the score of the outcome of the round (0 for lose, 3 for draw, 6 for win)


def part1(f:list) -> int:
    # f is a list of lists of strings, each pair is a round
    choices = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    outcomes = {
        'A':{'X': 3, 'Y': 6, 'Z': 0},
        'B':{'X': 0, 'Y': 3, 'Z': 6},
        'C':{'X': 6, 'Y': 0, 'Z': 3}
    }
    score = 0
    for round in f:
        score += choices[round[1]] + outcomes[round[0]][round[1]]
    return score

def part2(f:list) -> int:
    # X means I lose
    # Y means draw
    # Z means I win
    xyz = ['X', 'Y', 'Z']
    abc = ['A', 'B', 'C']
    offset = {
        'X': -1,
        'Y': 0,
        'Z': -2
    }
    choices = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    outcomes = {
        'A':{'X': 3, 'Y': 6, 'Z': 0},
        'B':{'X': 0, 'Y': 3, 'Z': 6},
        'C':{'X': 6, 'Y': 0, 'Z': 3}
    }
    score = 0
    for r in f:
        mychoice = xyz[abc.index(r[0]) + offset[r[1]]]
        score += choices[mychoice] + outcomes[r[0]][mychoice]
    return score

if __name__ == "__main__":
    # start by getting file as a list of strings
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [l.split() for l in open(fname, 'r')]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
