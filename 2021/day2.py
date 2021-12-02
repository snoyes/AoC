from aoc import data
from parse import parse

def part1(inputData):
    actions = {'forward': 1, 'down': 1j, 'up': -1j}
    position = sum(actions[action] * val for action, val in inputData)
    return int(position.real * position.imag)

def part2(inputData):
    actions = {
            'forward': {'x':  0, 'pos': 1},
            'down':    {'x':  1, 'pos': 0},
            'up':      {'x': -1, 'pos': 0}
            }
    x = position = 0
    for action, val in inputData:
        x += actions[action]['x'] * val
        position += actions[action]['pos'] * complex(val, val*x)
    return int(position.real * position.imag)

parser = lambda line: parse("{} {:d}", line)

if __name__ == "__main__":
    inputData = data(parser=parser)
    print(part1(inputData))
    print(part2(inputData))
