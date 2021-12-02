from aoc import data
publicKeys = list(map(int, data()))
#publicKeys = [5764801, 17807724]
divisor = 20201227
value = 1
subject = 7

loopsize = 0
while value not in publicKeys:
    value = (value * subject) % divisor
    loopsize += 1
print(f"{value} has loop size {loopsize}")

[otherkey] = [x for x in publicKeys if x != value]
print(f"other key is {otherkey}")

value = 1
for loop in range(loopsize):
    value = (value * otherkey) % divisor
print(f"encryption key is {value}")

