# /usr/bin/python3

import sys
from copy import deepcopy


def part1(f: list) -> int:
    lst = [(i, l) for i, l in enumerate(f)]
    for i, l in enumerate(f):
        ind = l + lst.index((i, l))
        lst.remove((i, l))
        lst.insert(ind % len(lst), (i, l))

    zero = (f.index(0), 0)
    l = len(lst)
    return sum([
        lst[(lst.index(zero) + i) % l][1]
        for i in [1000, 2000, 3000]
    ])


def part2(f: list) -> int:
    key = 811589153
    f = [key * i for i in f]

    lst = [(i, l) for i, l in enumerate(f)]
    for _ in range(10):
        for i, l in enumerate(f):
            ind = l + lst.index((i, l))
            lst.remove((i, l))
            lst.insert(ind % len(lst), (i, l))

    zero = (f.index(0), 0)
    l = len(lst)
    return sum([
        lst[(lst.index(zero) + i) % l][1]
        for i in [1000, 2000, 3000]
    ])


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = list(map(int, open(fname, 'r').readlines()))

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))
