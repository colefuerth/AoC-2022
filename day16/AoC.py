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

def hashset(s: set) -> int:
    return sum(hash(v) for v in s)
bestPathCache = dict()
def bestPath(valve: Valve, valves:dict, closed: set, minutes_left: int) -> tuple:
    # find the best path from valve to a closed valve
    # return the valve, the pressure, and the minutes left
    # use a DFS
    if (valve, hashset(closed), minutes_left) in bestPathCache:
        return bestPathCache[(valve, hashset(closed), minutes_left)]
    
    if not closed:
        return None, 0

    # create a cache of the next best valve to investigate
    valve_values = {
        v: v.rate * (minutes_left - valve.dist[v] - 1)
        for v in closed
        if valve.dist[v] < minutes_left}
    if not valve_values:
        return None, 0
    valve_values = sorted(valve_values.items(), key=lambda x: x[1], reverse=True)

    best_valve, best_pressure = None, 0
    worse_count = 0
    for v, p in valve_values:
        closed.remove(v)
        vp, pp = bestPath(v, valves, closed, minutes_left - valve.dist[v] - 1)
        closed.add(v)
        if pp > best_pressure:
            best_valve, best_pressure = vp, pp
        else:
            worse_count += 1
        if worse_count > 10:
            break
    best_pressure += p

    bestPathCache[(valve, hashset(closed), minutes_left)] = best_valve, best_pressure
    return best_valve, best_pressure

def part1(valves: dict) -> int:
    # treat f as a stack, if pos not at the best valve, pop and try again
    pos = valves['AA']
    pressure = 0

    closed = set(valves.values())
    minutes_left = 30
    best_valve, best_pressure = bestPath(pos, valves, closed, minutes_left)
    return best_pressure


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
