from aoc import *
import re

def parse(s):
    low, high, needle, haystack = re.findall('[^: -]+', s)
    return (int(low), int(high), needle, haystack)

entries = data(parse)

def part1(entries):
    valid = lambda low, high, needle, haystack: low <= haystack.count(needle) <= high
    return len([entry for entry in entries if valid(*entry)])

def part2(entries):
    valid = lambda low, high, needle, haystack: [haystack[x-1] for x in (low, high)].count(needle) == 1
    return len([entry for entry in entries if valid(*entry)])

print(part1(entries), part2(entries))
