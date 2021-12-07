from aoc import data
import parse
from collections import Counter

def part1(inputData):
    # By sorting the endpoints all horizontal segments go left to right
    # and all vertical segments go top to bottom
    inputData = [sorted([(line['x1'], line['y1']), (line['x2'], line['y2'])]) for line in inputData]

    visited = Counter((x, y) 
            for (x1, y1), (x2, y2) in inputData if x1 == x2 or y1 == y2
            for x in range(x1, x2 + 1)
            for y in range(y1, y2 + 1)
            )
    return sum(cell > 1 for cell in visited.values())

def part2(inputData):
    # By sorting the endpoints, all segments are left to right, and either up 45 or top to bottom.
    inputData = [sorted([(line['x1'], line['y1']), (line['x2'], line['y2'])]) for line in inputData]

    # Handle everything except up 45
    visited = Counter((x, y) 
            for (x1, y1), (x2, y2) in inputData if y1 <= y2
            for (x, y) in zip(
                [x1 + (x1 != x2)*d for d in range(max((x2-x1), (y2-y1))+1)],
                [y1 + (y1 < y2)*d for d in range(max((x2-x1), (y2-y1))+1)]
                )
            )

    # Handle up 45
    visited.update((x, y) 
            for (x1, y1), (x2, y2) in inputData if y1 > y2
            for (x, y) in zip(
                [x1 + d for d in range(x2-x1+1)], # 45 degrees, so x2-x1 == y2-y1
                [y1 - d for d in range(x2-x1+1)]
                )
            )
    return sum(cell > 1 for cell in visited.values())

parser = parse.compile('{x1:d},{y1:d} -> {x2:d},{y2:d}').parse

if __name__ == "__main__":
    inputData = data(parser=parser)
    print(part1(inputData[:]))
    print(part2(inputData[:]))
