from aoc import data
from itertools import pairwise
from more_itertools import triplewise

def part1(depths):
    return sum(a < b for a, b in pairwise(depths))

def part2(depths):
    return part1(map(sum, triplewise(depths)))

if __name__ == "__main__":
    inputData = data(parser=int)
    print(part1(inputData))
    print(part2(inputData))
