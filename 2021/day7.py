from aoc import data
from statistics import median, mean

def part1(inputData):
    goal = int(median(inputData))
    fuel = lambda crab, goal: abs(crab-goal)
    return sum(fuel(crab, goal) for crab in inputData)

def part2(inputData):
    goalLowerBound = int(mean(inputData))
    goalUpperBound = goalLowerBound + 1
    fuel = lambda crab, goal: abs(crab-goal) * (abs(crab-goal) + 1) // 2
    return min(
            sum(fuel(crab, goal) for crab in inputData) 
            for goal in (goalLowerBound, goalUpperBound)
           )

parser = int

if __name__ == "__main__":
    inputData = data(parser=parser,delimiter=',')
    print(part1(inputData))
    print(part2(inputData))

