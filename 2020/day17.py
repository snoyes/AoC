from aoc import data
from collections import Counter
from itertools import product

def getNeighbors(cell):
    neighbors = [tuple(cell[i] + v[i] for i in range(len(cell))) for v in product([-1, 0, 1], repeat=len(cell)) ]
    neighbors.remove(cell)
    return neighbors

def playLife(layout, dimensions=2, cycles=6):
    assert(dimensions >= 2)
    living = {(x, y) + (0,)*(dimensions - 2) for x, line in enumerate(layout) for y, cell in filter(lambda c: c[1] == '#', enumerate(line))}
    for cycle in range(cycles):
        neighbors = Counter(neighbor for cell in living for neighbor in getNeighbors(cell))
        living = {cell for cell, neighborCount in filter(lambda x: x[1] == 3, neighbors.items())}.union(
                 {cell for cell, neighborCount in filter(lambda x: x[1] == 2, neighbors.items())}.intersection(living)
                 )
    return len(living)

layout = data()
for part in range(2):
    print(f"Part {part+1}:", playLife(layout, part+3))
