# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
import numpy as np
from collections import defaultdict, Counter
import progressbar as pb


class Valve:
    def __init__(self, name, rate, dest, dist=None):
        self.name = name
        self.rate = rate
        self.dest = dest
        self.dist = dist if dist else dict()

    def __hash__(self):
        return hash(self.name)

    def __getitem__(self, key):
        return self.dest[key]

    def __iter__(self):
        return iter(self.dest)

    def __repr__(self):
        return f'Valve({self.name}, {self.rate}, {self.dest}, {self.dist})'
    # def __deepcopy__(self, memo):
    #     return Valve(self.name, self.rate, self.dest, self.dist)



def calcDistances(valve: Valve, valves: dict) -> dict:
    # calculate the distance from valve to all other valves
    # use a BFS
    visited = set()
    queue = [(valve, 0)]
    while queue:
        v, dist = queue.pop(0)
        if v not in visited:
            visited.add(v)
            valve.dist[v] = dist
            for d in v.dest:
                queue.append((valves[d], dist+1))
    return valve.dist


def part1(valves: dict) -> int:
    # treat f as a stack, if pos not at the best valve, pop and try again
    pos = valves['AA']
    pressure = 0

    closed = set(valves.values())
    minutes_left = 30
    while minutes_left > 0:
        valve_values = {
            v: v.rate * (minutes_left - pos.dist[v] - 1)
            for v in closed
            if pos.dist[v] < minutes_left}
        if not valve_values:
            break
        best_valve = max(valve_values, key=valve_values.get)
        print(f'pos is {pos.name}, moving to {best_valve.name} in {pos.dist[best_valve]} minutes')
        print(f'opening valve {best_valve.name} at minute {30-minutes_left+pos.dist[best_valve]}')
        minutes_left -= pos.dist[best_valve] + 1
        pressure += valve_values[best_valve]
        closed.remove(best_valve)
        pos = best_valve
    return pressure


def part2(f: list) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]
    valves = dict()
    for valve in f:
        v, t = valve.split('; ')
        name = v.split(' ')[1]
        rate = int(re.findall(r'\d+', v)[0])
        dest = list(t.replace('tunnels lead to valves ', '').replace(
            'tunnel leads to valve ', '').split(', '))
        valves.update({name: Valve(name, rate, dest)})
    # print(valves)

    for v in valves.values():
        calcDistances(v, valves)

    # for v in valves.values():
    #     print(v.name, v.dist)

    print('Part 1:', part1(valves))
    print('Part 2:', part2(valves))
