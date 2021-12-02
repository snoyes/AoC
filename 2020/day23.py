debug = False
def debugPrint(m=''):
    if debug:
        print(m)

def playCups(cups, moves):
    current = cups[0]
    currentIndex = cups.index(current)
    for move in (range(1, moves+1)):
        if move % 100 == 0:
            print(f"move: {move}")
        cups = cups[currentIndex:] + cups[:currentIndex]
        #debugPrint(f"-- move {move} --")
        #cupsList = ' '.join([str(v) if v != current else f"({v})" for v in cups[:10]])
        #debugPrint(f"cups: {cupsList}")
        pickup = cups[1:4]
        #pickup += cups[:3-min(3, len(pickup))]
        #debugPrint(f"pick up: {', '.join(map(str, pickup))}")
        try:
            destination = max([x for x in cups if x not in pickup and x < current])
        except ValueError:
            destination = max([x for x in cups if x not in pickup])
        #debugPrint(f"destination: {destination}")
        #cups = cups[0:1] + cups[4:]
        destinationIndex = cups.index(destination)
        cups = cups[0:1] + cups[4:destinationIndex+1] + pickup + cups[destinationIndex+1:]

        currentIndex = cups.index(current)
        currentIndex = (currentIndex + 1) % len(cups)
        current = cups[currentIndex]
        #debugPrint()
    #debugPrint("-- final --")
    cupsList = ' '.join([str(v) if v != current else f"({v})" for v in cups])
    #debugPrint(f"cups: {cupsList}")
    oneIndex = cups.index(1)
    cups = cups[oneIndex:] + cups[:oneIndex]
    return cups


def part1(cups):
    cups = playCups(cups, 100)
    return ''.join(map(str, cups[1:]))

def part2(cups):
    cups = playCups(cups, 10000000)
    print(' '.join(map(str, cups[1:3])))
    return cups[1] * cups[2]

inputCups = '389125467'
#inputCups = '586439172'

cups = list(map(int, list(inputCups)))
print(part1(cups))

cups = list(map(int, list(inputCups))) + list(range(10, 1000001))
print(part2(cups))
