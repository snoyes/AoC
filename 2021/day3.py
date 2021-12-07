from aoc import data
from collections import Counter

def part1(inputData):
    length = len(inputData[0])
    c = [Counter([line[digit] for line in inputData]) for digit in range(length)]
    gamma   = int(''.join(c[digit].most_common()[ 0][0] for digit in range(length)), 2)
    epsilon = int(''.join(c[digit].most_common()[-1][0] for digit in range(length)), 2)
    # equivalent: epsilon = ~gamma & 2**length-1

    return gamma * epsilon


def part2(inputData):
    length = len(inputData[0])
    oxy = [x for x in inputData]
    co2 = [x for x in inputData]
    for i in range(length):
        c = Counter([line[i] for line in oxy])
        m = '1' if c['1'] == c['0'] else c.most_common()[0][0]
        oxy = [x for x in oxy if x[i] == m]

        c = Counter([line[i] for line in co2])
        print(f'{i=} {c=}')
        m = '0' if c['1'] == c['0'] else c.most_common()[-1][0]
        co2 = [x for x in co2 if x[i] == m]

    print(f'{oxy=} {co2=}')

    oxy = int(''.join(oxy[0]), 2)
    co2 = int(''.join(co2[0]), 2)
    print(f'{oxy=} {co2=}')

    return oxy * co2

if __name__ == "__main__":
    inputData = data()
    print(part1(inputData))
    print(part2(inputData))
