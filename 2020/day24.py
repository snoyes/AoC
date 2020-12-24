from collections import Counter
from aoc import data
import re

parser = lambda x: re.findall('ne|nw|se|sw|e|w', x)
instructions = data(parser=parser)

directions = { "nw": (-1-1j), "ne": (1-1j), "sw": (-1+1j), "se": (+1+1j), "w": (-2+0j), "e": (+2+0j) }

findTile = lambda instruction: sum(directions[i] for i in instruction)
flippedTiles = Counter(map(findTile, instructions))
blackTiles = [tile for tile, times in filter(lambda x: x[1] % 2, flippedTiles.items())]
part1 = len(blackTiles)

findNeighbors = lambda tile: {tile + d for d in directions.values()}
for day in range(1, 101):
    neighbors = Counter(tile for nearby in map(findNeighbors, blackTiles) for tile in nearby)
    blackTiles = {tile for tile, n in filter(lambda x: x[1] == 1, neighbors.items())}.intersection(blackTiles).union(
                 {tile for tile, n in filter(lambda x: x[1] == 2, neighbors.items())}
                 )
part2 = len(blackTiles)

print(part1)
print(part2)
