from aoc import *

parser = lambda x: (x[0], int(x[1:]))
entries = data(parser=parser, delimiter='\n')

vectors = {
        'N': (0, -1),
        'E': (1, 0),
        'S': (0, 1),
        'W': (-1, 0)
        }

def movePoint(point, vectorKey, distance):
    delta = [d * distance for d in vectors[vectorKey]]
    return tuple(p + d for p, d in zip(point, delta))

def part1(entries):
    bearings = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    actions = { key: lambda ship, bearing, val, key=key: (movePoint(ship, key, val), bearing) for key in vectors.keys() }
    actions.update ({
            'L': lambda ship, bearing, val: (ship, (bearing-val) % 360),
            'R': lambda ship, bearing, val: (ship, (bearing+val) % 360),
            'F': lambda ship, bearing, val: actions[bearings[bearing]](ship, bearing, val)
    })

    ship = (0, 0)
    bearing = 90
    for action, val in entries:
        ship, bearing = actions[action](ship, bearing, val)

    return abs(ship[0]) + abs(ship[1])

def part2(entries):
    def rotate(waypoint, val, direction):
        while val > 0:
            waypoint = (direction*waypoint[1], -direction*waypoint[0])
            val -= 90
        return waypoint

    actions = {
            'L': lambda ship, waypoint, val: (ship, rotate(waypoint, val, 1)),
            'R': lambda ship, waypoint, val: (ship, rotate(waypoint, val, -1)),
            'F': lambda ship, waypoint, val: ((ship[0] + waypoint[0]*val, ship[1] + waypoint[1]*val), waypoint)
    }
    actions.update( { key: lambda ship, waypoint, val, key=key: (ship, movePoint(waypoint, key, val)) for key in vectors.keys() } )

    ship = (0, 0)
    waypoint = (10, -1)
    for action, val in entries:
        ship, waypoint = actions[action](ship, waypoint, val)

    return abs(ship[0]) + abs(ship[1])

print(part1(entries), part2(entries))
