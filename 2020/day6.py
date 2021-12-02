from collections import Counter
from aoc import data
rows = data(delimiter='\n\n')
def part1(rows):
    return sum(len(set(row.replace('\n', ''))) for row in rows)

def part2(rows):
    return sum(len([x for x in Counter(row).values() if x == len(row.split('\n'))]) for row in rows)

print(part1(rows))
print(part2(rows))
