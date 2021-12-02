from aoc import data
import sys
from math import ceil

earliest, idString = data()
earliest = int(earliest)
ids = [x if x == 'x' else int(x) for x in idString.split(',')]

def part1(earliest, ids):
    ids = [x for x in ids if x != 'x']
    soonest = {ceil(earliest / id) * id:id for id in ids}
    bus = soonest[min(soonest)]
    wait = min(soonest) - earliest
    return bus * wait

def part2(ids):
    positions = [(k, int(v)) for k, v in enumerate(ids) if v != 'x']
    lcm, time = 1, 0
    for pos, bus in positions:
        [time] = [x * lcm + time for x in range(bus) if (x * lcm + time + pos) % bus == 0]
        lcm *= bus

    return(time)
    
print(part1(earliest, ids))
print(part2(ids))
