# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re


def filesize(folder: dict) -> int:
    if 'size' in folder:
        return folder['size']
    size = sum([filesize(folder['subdir'][d]) for d in folder['subdir']])
    size += sum([f[0] for f in folder['files']])
    folder['size'] = size
    return size


def build_filesystem(f: list) -> dict:
    root = {'name': "/", 'subdir': dict(), 'files': list(), 'parent': None}
    fp = root
    for line in f:
        if line == "$ cd ..":
            fp = fp['parent']
        elif line.startswith("$ cd "):
            newdir = line[5:]
            if newdir not in fp['subdir']:
                fp['subdir'][newdir] = {
                    'name': newdir, 'subdir': dict(), 'files': list(), 'parent': fp}
            fp = fp['subdir'][newdir]
        elif line == "$ ls":
            continue
        elif line.startswith("dir "):
            _, dirname = line.split()
            if dirname not in fp['subdir']:
                fp['subdir'][dirname] = {
                    'name': dirname, 'subdir': dict(), 'files': list(), 'parent': fp}
        elif re.match(r"\d+ \w+(\.\w+)?", line):
            size, fname = line.split()
            fp['files'].append((int(size), fname))
        else:
            print("ERROR:", line)
    return root


def part1(f: list) -> int:
    root = build_filesystem(f)
    sizes = []

    def calcsizes(folder: dict):
        sizes.append(filesize(folder))
        for d in folder['subdir']:
            calcsizes(folder['subdir'][d])
    calcsizes(root)
    return sum([s for s in sizes if s <= 100000])


def part2(f: list) -> int:
    root = build_filesystem(f)
    min_del_size = filesize(root) - (70000000 - 30000000)
    sizes = []

    def calcsizes(folder: dict):
        sizes.append(filesize(folder))
        for d in folder['subdir']:
            calcsizes(folder['subdir'][d])
    calcsizes(root)
    return min([s for s in sizes if s >= min_del_size])


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print("Part 1:", part1(deepcopy(f)))
    print("Part 2:", part2(deepcopy(f)))
