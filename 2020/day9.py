numbers = list(map(lambda x: int(x), open('input', 'r').read().strip().split('\n')))

for x in range(25, len(numbers)):
    found = False
    for y in range(x):
        if numbers[x] - numbers[y] in numbers:
            found = True
            break
    if not found:
        print(numbers[x])


