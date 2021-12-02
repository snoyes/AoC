from aoc import *

entries = set(data(parser=int))

def part1(entries):
    return first(x * y for x in entries 
            for y in entries & {2020 - x}
            )

def part2(entries):
    return first(x * y * z for x in entries 
            for y in entries 
            for z in entries & {2020 - x - y}
            )

print(part1(entries), part2(entries))
