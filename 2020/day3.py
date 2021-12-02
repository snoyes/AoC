from aoc import *

entries = data()

def impacts(rows, dx, dy, tree='#'):
    return sum([row[dx * y % len(row)] == tree for y, row in enumerate(rows[::dy])])

def part1(entries):
    return impacts(entries, 3, 1)

def part2(entries):
    from math import prod
    return prod(impacts(entries, x, y) for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

print(part1(entries), part2(entries))
