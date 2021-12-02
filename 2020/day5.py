from aoc import data

p = lambda x: int(x.translate(x.maketrans('FBLR', '0101')), 2)
seats = data(parser=p)

def part1(seats):
    return max(seats)

def part2(seats):
    return next(x for x in range(min(seats), max(seats)) if x not in seats)

print(part1(seats))
print(part2(seats))
