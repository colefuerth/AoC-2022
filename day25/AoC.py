# /usr/bin/python3

import sys

S2D_D = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


def s2d(s: str) -> int:
    digit = 0
    for i, c in enumerate(reversed(s)):
        digit += S2D_D[c] * 5**i
    return digit


def d2s(d: int) -> str:
    s = ''
    c = ''
    S2D_R = {v: k for k, v in S2D_D.items()}
    while d != 0:
        d, r = divmod(d, 5)
        if c != '':
            r += S2D_D[c]
        if r in S2D_R:
            s = S2D_R[r] + s
            c = ''
        else:
            c, ss = {3: ('1', '='), 4: ('1', '-'), 5: ('1', '0')}[r]
            s = ss + s

    return c + s


def part1(f: list) -> int:
    return d2s(sum(s2d(l) for l in f))


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]

    print('Part 1:', part1(f))
