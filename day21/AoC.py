# /usr/bin/python3

import sys


def part1(monkeys: dict) -> int:

    cache = dict()

    def calc(m: str) -> int:
        if isinstance(monkeys[m], int):
            return monkeys[m]
        if m in cache:
            return cache[m]
        cache[m] = int(eval(
            str(calc(monkeys[m][0])) + monkeys[m][1] + str(calc(monkeys[m][2]))
        ))
        return cache[m]
    return calc('root')


def part2(monkeys: dict) -> int:

    def calc(m: str):
        if m == 'humn':
            return 'humn'
        if isinstance(monkeys[m], int):
            return monkeys[m]
        a, b = calc(monkeys[m][0]), calc(monkeys[m][2])
        if isinstance(a, int) and isinstance(b, int):
            return int(eval(str(a) + monkeys[m][1] + str(b)))
        return f'({a}{monkeys[m][1]}{b})'
    a, b = calc(monkeys['root'][0]), calc(monkeys['root'][2])

    # solve for humn
    y, x = (a, b) if isinstance(a, int) else (b, a)
    
    # we can use sympify
    from sympy import sympify
    from sympy.solvers import solve
    return solve(sympify(f'Eq({y},{x})'))[0]


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]

    monkeys = dict()
    for line in f:
        m, s = line.split(': ')
        if s.isdigit():
            monkeys[m] = int(s)
        else:
            monkeys[m] = s.split(' ')

    print('Part 1:', part1(monkeys))
    print('Part 2:', part2(monkeys))
