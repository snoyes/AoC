from aoc import data
from math import sqrt
import re

def topEdge(tile):
    return tile.split('\n')[0]

def rightEdge(tile):
    return ''.join(row[-1] for row in tile.split('\n'))

def leftEdge(tile):
    return ''.join(row[0] for row in tile.split('\n'))

def bottomEdge(tile):
    return tile.split('\n')[-1]

def findSquareSize(numtiles):
    return int(sqrt(numtiles))

def rotateTile(tile, turns=1):
    for turn in range(turns):
        tile = '\n'.join(
                [''.join(
                    [line[i] for line in tile.split('\n')[::-1]]
                    ) for i in range(len(tile.split('\n')))
                ]
             )
    return tile

def flipTile(tile):
    return '\n'.join(line[::-1] for line in tile.split('\n'))

# (id, flip, turns)
grid = []
squareSize = 0

def solve():
    global grid, squareSize, tiles
    if None not in [v for line in grid for v in line]:
        print(grid)
        print(grid[0][0][0] * grid[-1][0][0] * grid[0][-1][0] * grid[-1][-1][0])
    for y in range(squareSize):
        for x in range(squareSize):
            if grid[y][x] is None:
                for id in tiles:
                    if id in [v[0] for line in grid for v in line if v is not None]:
                        continue
                    for flip in range(2):
                        for turn in range(4):
                            if possible(y, x, id, flip, turn):
                                grid[y][x] = (id, flip, turn)
                                solve()
                                grid[y][x] = None
                return

def getPositionedTile(id, flip, turn):
    global tiles
    tile = tiles[id]
    for _ in range(flip):
        tile = flipTile(tile)
    for _ in range(turn):
        tile = rotateTile(tile)

    return tile

def possible(y, x, id, flip, turn):
    global grid, squareSize, tiles
    debug = False
    if debug:
        print(grid)
    if id in [v[0] for line in grid for v in line if v is not None]:
        if debug:
            print(f"Already in")
        return False

    if debug:
        print(f"I am {id} {flip} {turn} in {y},{x}")

    tile = getPositionedTile(id, flip, turn)
    if debug:
        print(tile)

    if x > 0:
        neighbor = grid[y][x-1]
        neighborEdge = rightEdge(getPositionedTile(*neighbor))
        edge = leftEdge(tile)
        if debug:
            print(f"Left neighbor: {neighbor}")
            print(f"neighborEdge: {neighborEdge}")
            print(f"      myEdge: {edge}")
        if neighborEdge != edge:
            if debug:
                print("does not match")
            return False

    if y > 0:
        neighbor = grid[y-1][x]
        neighborEdge = bottomEdge(getPositionedTile(*neighbor))
        edge = topEdge(tile)
        if debug:
            print(f"Top neighbor: {neighbor}")
            print(f"neighborEdge: {neighborEdge}")
            print(f"      myEdge: {edge}")
        if neighborEdge != edge:
            if debug:
                print("does not match")
            return False

    return True

if __name__ == "__main__":
    p = lambda s: re.findall(r'Tile (\d+):\n(.*)', s, re.DOTALL)
    contents = data(parser=p, delimiter='\n\n')
    tiles = {int(key):value for [[key, value]] in contents}
    squareSize = findSquareSize(len(tiles))
    grid = [[None]*squareSize for _ in range(squareSize)]
    #solve()

    from day20solution import solution 
    tileSize = len(tiles[solution[0][0][0]].split('\n'))
    image = ""
    for line in solution:
        for i in range(1, tileSize - 1):
            for cell in line:
                tile = getPositionedTile(*cell)
                image += tile.split('\n')[i][1:-1]
            image += '\n'
    image = image.strip()

    seaMonster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.replace(' ', '.')
    for flip in range(2):
        for turn in range(4):
            tile = image
            for _ in range(flip):
                tile = flipTile(tile)
            for _ in range(turn):
                tile = rotateTile(tile)
            monstersFound = 0
            for i in range(len(image.split('\n')[0]) - len(seaMonster.split('\n')[0])):
                lead = '.' * i
                search = lead + seaMonster.replace('\n', '.*\n' + lead)
                results = re.findall(search, tile)
                monstersFound += len(results)

            if monstersFound > 0:
                print(monstersFound)
                print(tile.count('#') - (seaMonster.count('#') * monstersFound))
