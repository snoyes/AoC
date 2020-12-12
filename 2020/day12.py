from aoc import *
import re

parser = lambda x: (x[0], int(x[1:]))
entries = data(parser=parser, delimiter='\n')

vectors = {
        'N': (0, -1),
        'E': (1, 0),
        'S': (0, 1),
        'W': (-1, 0)
        }

def movePoint(point, vector, distance):
    return (point[0] + vectors[vector][0] * distance, point[1] + vectors[vector][1] * distance)

def part1(entries):
    bearings = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    actions = {
            'N': lambda ship, bearing, val: (movePoint(ship, 'N', val), bearing),
            'E': lambda ship, bearing, val: (movePoint(ship, 'E', val), bearing),
            'S': lambda ship, bearing, val: (movePoint(ship, 'S', val), bearing),
            'W': lambda ship, bearing, val: (movePoint(ship, 'W', val), bearing),
            'L': lambda ship, bearing, val: (ship, (bearing-val) % 360),
            'R': lambda ship, bearing, val: (ship, (bearing+val) % 360),
            'F': lambda ship, bearing, val: actions[bearings[bearing]](ship, bearing, val)
                }
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
            'N': lambda ship, waypoint, val: (ship, movePoint(waypoint, 'N', val)),
            'E': lambda ship, waypoint, val: (ship, movePoint(waypoint, 'E', val)),
            'S': lambda ship, waypoint, val: (ship, movePoint(waypoint, 'S', val)),
            'W': lambda ship, waypoint, val: (ship, movePoint(waypoint, 'W', val)),
            'L': lambda ship, waypoint, val: (ship, rotate(waypoint, val, 1)),
            'R': lambda ship, waypoint, val: (ship, rotate(waypoint, val, -1)),
            'F': lambda ship, waypoint, val: ((ship[0] + waypoint[0]*val, ship[1] + waypoint[1]*val), waypoint)
    }
    ship = (0, 0)
    waypoint = (10, -1)
    for action, val in entries:
        ship, waypoint = actions[action](ship, waypoint, val)
    return abs(ship[0]) + abs(ship[1])

print(part1(entries), part2(entries))
