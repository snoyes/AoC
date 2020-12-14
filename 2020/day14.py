from aoc import data
import re

def p(section):
    mask = section[:36]
    actions = [(int(key),int(val)) for key, val in re.findall('mem\[(\d+)] = (\d+)', section)]
    return mask, actions

contents = data(parser=p, delimiter='mask = ')[1:]

def part1(contents):
    memory = dict()
    for mask, actions in contents:
        orMask = int(mask.replace('X', '0'), 2)
        andMask = int(mask.replace('X', '1'), 2)
        memory.update( {key: (val | orMask) & andMask for key, val in actions} )
    return sum(memory.values())

def part2(contents):
    def swapX(mask, newX):
        mask = re.split('(X)', mask)
        mask[1::2] = newX
        return int(''.join(mask), 2)

    memory = dict()
    for mask, actions in contents:
        xCount = mask.count('X')
        for i in range(2**xCount):
            newX = bin(i)[2:].zfill(xCount)
            orMask = swapX(mask, newX)
            andMask = swapX(mask.replace('0', '1'), newX)
            memory.update( {(key | orMask) & andMask : val for key, val in actions} )
    return sum(memory.values())

print(part1(contents))
print(part2(contents))
