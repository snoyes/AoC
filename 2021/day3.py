from aoc import data
from parse import parse
from functools import partial

def part1(inputData):
    pass

def part2(inputData):
    pass

parser = partial(parse, "{} {:d}")
if __name__ == "__main__":
    inputData = data(parser=parser)
    print(part1(inputData))
    print(part2(inputData))
