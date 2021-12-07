from aoc import data
from collections import Counter, defaultdict

parser = int

def part1(inputData, days=80):
    fish = Counter(inputData)
    for _ in range(days):
        newFish = fish.pop(0, 0)
        fish = Counter({k-1: v for k, v in fish.items()}) + Counter({6: newFish, 8:newFish})
    return sum(fish.values())

def part2(inputData):
    return part1(inputData, days=256)

parser=int
if __name__ == "__main__":
    inputData = data(parser=parser,delimiter=',')
    print(part1(inputData))
    print(part2(inputData))

