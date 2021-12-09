from aoc import data
import itertools
import math

ORTHO_DIRECTIONS = ( (-1, 0), (0, -1), (0, 1), (1, 0) )
def getNeighbors(row, col, height, width):
    return {(row + y, col + x) for y, x in ORTHO_DIRECTIONS
            if 0 <= row + y < height and 0 <= col + x < width
            }

def part1(inputData):
    height, width = len(inputData), len(inputData[0])
    return sum(cell + 1 for row, line in enumerate(inputData) for col, cell in enumerate(line) 
            if all(cell < inputData[neighborRow][neighborCol] for neighborRow, neighborCol in getNeighbors(row, col, height, width) )
           )

def getBasin(row, col, inputData):
    height, width = len(inputData), len(inputData[0])
    basin = {(row, col)}
    visited = basin
    while len(visited):
        newNeighbors = {neighbor for row, col in visited for neighbor in getNeighbors(row, col, height, width)
                if inputData[neighbor[0]][neighbor[1]] < 9 and neighbor not in basin
                }
        basin |= (visited := newNeighbors)
    return basin

def part2(inputData):
    basins = list()
    for row, col in itertools.product(range(len(inputData)), range(len(inputData[0]))):
        if inputData[row][col] < 9 and not any((row, col) in x for x in basins):
            basins.append(getBasin(row, col, inputData))
    return math.prod(sorted(map(len, basins), reverse=True)[:3])

parser = lambda line: [int(line[i]) for i in range(len(line))]

if __name__ == "__main__":
    inputData = data(parser=parser)
    print(part1(inputData))
    print(part2(inputData))
