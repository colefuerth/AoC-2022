# /usr/bin/python3

import sys
from copy import deepcopy
import re
import numpy as np
import progressbar as pb


class Monkey:
    def __init__(self, items, operation, test, cases):
        self.items = items
        self.operation = operation
        self.test = test
        self.cases = cases
        self.inspected = 0

    def inspect(self, item: int) -> tuple:
        # returns tuple of (item, newmonkey_index)
        self.inspected += 1
        item = eval(self.operation.replace('old', str(item))) // 3
        return item, self.cases[int(item % self.test == 0)]

    def inspect2(self, item: int) -> tuple:
        # returns tuple of (item, newmonkey_index)
        self.inspected += 1
        item = eval(self.operation.replace('old', str(item)))
        return item, self.cases[int(item % self.test == 0)]


def part1(monkeys: list) -> int:

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                item, newmonkey = monkey.inspect(item)
                monkeys[newmonkey].items.append(item)
            monkey.items = []
    return np.prod(sorted([monkey.inspected for monkey in monkeys], reverse=True)[:2])


def part2(monkeys: list) -> int:

    test_lcm = np.lcm.reduce([monkey.test for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                item, newmonkey = monkey.inspect2(item)
                item = item % test_lcm
                monkeys[newmonkey].items.append(item)
            monkey.items = []
    return np.prod(sorted([monkey.inspected for monkey in monkeys], reverse=True)[:2])


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]
    f = re.split(r'Monkey \d+:\n', '\n'.join(f))
    f = [m.split('\n') for m in f if m != '']

    monkeys = []
    reint = re.compile(r'\d+')
    for items in f:
        start_items = list(map(int, reint.findall(items[0])))
        operation = items[1].replace('Operation: new = ', '')
        test = int(reint.findall(items[2])[0])
        cases = [int(reint.findall(items[4])[0]),
                 int(reint.findall(items[3])[0])]
        monkeys.append(Monkey(start_items, operation, test, cases))

    print('Part 1:', part1(deepcopy(monkeys)))
    print('Part 2:', part2(deepcopy(monkeys)))
