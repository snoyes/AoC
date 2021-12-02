from random import *
from day2 import *

exampleInput = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()

exampleData = list(map(parser, exampleInput.split("\n")))

def test_part1_example():
    assert part1(exampleData) == 150

minVal, maxVal = -10000, 10000
maxNumDirections = 1000
commands = ('forward', 'down', 'up')

def test_part1_order_irrelevant():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(minVal, maxVal)) for _ in range(numDirections)]
    assert part1(inputData) == part1(sample(inputData, k=len(inputData)))

def test_part1_negate_numbers():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(minVal, maxVal)) for _ in range(numDirections)]
    invertedData = [(action, -val) for action, val in inputData]
    assert part1(inputData) == part1(invertedData)

def test_part1_up_to_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(0, maxVal)) for _ in range(numDirections)]
    commandMap = {'forward': 'forward', 'down': 'down', 'up': 'down'}
    invertedData = [(commandMap[action], val) for action, val in inputData]
    assert part1(inputData) <= part1(invertedData)

def test_part1_down_to_up():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(0, maxVal)) for _ in range(numDirections)]
    commandMap = {'forward': 'forward', 'down': 'up', 'up': 'up'}
    invertedData = [(commandMap[action], val) for action, val in inputData]
    assert part1(inputData) >= part1(invertedData)

def test_part1_upside_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(minVal, maxVal)) for _ in range(numDirections)]
    commandMap = {'forward': 'forward', 'down': 'up', 'up': 'down'}
    invertedData = [(commandMap[action], val) for action, val in inputData]
    assert part1(inputData) == -part1(invertedData)

def test_part1_no_forward():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(('down', 'up')), randrange(minVal, maxVal)) for _ in range(numDirections)]
    assert part1(inputData) == 0

def test_part1_no_up_or_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [('forward', randrange(minVal, maxVal)) for _ in range(numDirections)]
    assert part1(inputData) == 0

def test_part1_no_up():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(('forward', 'down')), randrange(0, maxVal)) for _ in range(numDirections)]
    assert part1(inputData) >= 0

def test_part1_no_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(('forward', 'up')), randrange(0, maxVal)) for _ in range(numDirections)]
    assert part1(inputData) <= 0

def test_part1_new_forward():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(1, maxVal)) for _ in range(numDirections)]
    extraCommand = ('forward', randrange(1, maxVal))
    i = randint(0, numDirections)
    extraData = inputData[:i] + [extraCommand] + inputData[i:]
    assert abs(part1(inputData)) <= abs(part1(extraData))

def test_part2_example():
    assert part2(exampleData) == 900

def test_part2_negate_numbers():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(minVal, maxVal)) for _ in range(numDirections)]
    invertedData = [(action, -val) for action, val in inputData]
    assert part2(inputData) == -part2(invertedData)

def test_part2_up_to_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(0, maxVal)) for _ in range(numDirections)]
    commandMap = {'forward': 'forward', 'down': 'down', 'up': 'down'}
    invertedData = [(commandMap[action], val) for action, val in inputData]
    assert part2(inputData) <= part2(invertedData)

def test_part2_down_to_up():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(0, maxVal)) for _ in range(numDirections)]
    commandMap = {'forward': 'forward', 'down': 'up', 'up': 'up'}
    invertedData = [(commandMap[action], val) for action, val in inputData]
    assert part2(inputData) >= part2(invertedData)

def test_part2_upside_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(commands), randrange(minVal, maxVal)) for _ in range(numDirections)]
    commandMap = {'forward': 'forward', 'down': 'up', 'up': 'down'}
    invertedData = [(commandMap[action], val) for action, val in inputData]
    assert part2(inputData) == -part2(invertedData)

def test_part2_no_forward():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(('down', 'up')), randrange(minVal, maxVal)) for _ in range(numDirections)]
    assert part2(inputData) == 0

def test_part2_no_up_or_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [('forward', randrange(minVal, maxVal)) for _ in range(numDirections)]
    assert part2(inputData) == 0

def test_part2_no_up():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(('forward', 'down')), randrange(0, maxVal)) for _ in range(numDirections)]
    assert part2(inputData) >= 0

def test_part2_no_down():
    numDirections = randrange(maxNumDirections + 1)
    inputData = [(choice(('forward', 'up')), randrange(0, maxVal)) for _ in range(numDirections)]
    assert part2(inputData) <= 0
