from collections import Counter, defaultdict

stones = Counter(map(int, open(0).read().strip().split()))

# could cache this, but it doesn't make a huge difference
def make_stones(stone):
    if stone == 0:
        return (1,)
    elif len(s := str(stone)) % 2 == 0:
        left = int(s[:len(s)//2])
        right = int(s[len(s)//2:])
        return (left, right,)
    else:
        return (stone * 2024,)

for blink in range(1, 76):
    new_stones = defaultdict(int)
    for stone, qty in stones.items():
        for new_stone in make_stones(stone):
            new_stones[new_stone] += qty
    stones = new_stones
    if blink in (25, 75):
        print(sum(stones.values()))
