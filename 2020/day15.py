from collections import defaultdict
content = [10, 16, 6, 0, 1, 17]

def part1(content, n=2020):
    numbers = defaultdict(lambda: numCount)
    numbers.update( {x: i+1 for i, x in enumerate(content)} )

    lastSpoke = content[-1]
    for numCount in range(len(content), n):
        numbers[lastSpoke], lastSpoke = numCount, numCount - numbers[lastSpoke]

    return lastSpoke

def part2(content):
    return part1(content, n=30000000)

print(part1(content))
print(part2(content))
