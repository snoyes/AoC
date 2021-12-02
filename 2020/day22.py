from aoc import data
from collections import deque, defaultdict
def p(section):
    return deque(map(int, section.split('\n')[1:]))
hands = data(parser=p, delimiter='\n\n')

def part1(hands):
    while all(len(hand) > 0 for hand in hands):
        cards = [hand.popleft() for hand in hands]
        if cards[0] == max(cards):
            hands[0].extend(cards)
        else:
            hands[1].extend(cards[::-1])

    [winner] = [hand for hand in hands if len(hand) > 0]
    return sum((k+1)*v for k, v in enumerate(list(winner)[::-1]))

highgamenum = 0
debug = True
def play2(hands, gamenum=1):
    global highgamenum, debug
    hashes = set()
    highgamenum = max(highgamenum, gamenum)

    if debug:
        print(f"=== Game {gamenum} ===")
        print()
    roundnum = 1
    while all(len(hand) > 0 for hand in hands):
        if debug:
            print(f"-- Round {roundnum} (Game {gamenum}) --")
            print(f"Player 1's deck: {', '.join(str(x) for x in hands[0])}")
            print(f"Player 2's deck: {', '.join(str(x) for x in hands[1])}")
        hashed = hash('\n'.join(''.join(map(str, hand)) for hand in hands))
        if hashed in hashes:
            # player 1 wins
            if debug:
                print(f"Player 1 wins round {roundnum} of game {gamenum}! (hash repeats)")
            return 0
        hashes = hashes.union({hashed})

        cards = [hand.popleft() for hand in hands]
        if debug:
            print(f"Player 1 plays: {cards[0]}")
            print(f"Player 2 plays: {cards[1]}")
        if any(cards[i] > len(hands[i]) for i in range(len(hands))):
            if cards[0] == max(cards):
                winner = 0
            else:
                winner = 1
        else:
            if debug:
                print("Playing a subgame to determine the winner...")
                print()
            hand1 = deque(list(hands[0])[:cards[0]])
            hand2 = deque(list(hands[1])[:cards[1]])
            if max(hand1) > max(hand2): # It's impossible for player 1 to lose with the largest card
                if debug:
                    print("Actually, no need. Player 1 will win.")
                    print()
                winner = 0
            else:
                winner = play2([hand1, hand2], gamenum=highgamenum+1)
            if debug:
                print(f"...anyway, back to game {gamenum}.")

        if debug:
            print(f"Player {winner + 1} wins round {roundnum} of game {gamenum}!")
            print()
        roundnum += 1
        if winner == 0:
            hands[0].extend(cards)
        else:
            hands[1].extend(cards[::-1])

    if len(hands[0]) == 0:
        if debug:
            print(f"The winner of game {gamenum} is player 2!")
            print()
        return 1
    else:
        if debug:
            print(f"The winner of game {gamenum} is player 1!")
            print()
        return 0

def part2(hands):
    global debug
    winner = play2(hands)
    winningHand = hands[winner]
    if debug:
        print("== Post-game results ==")
        print(f"Player 1's deck: {hands[0]}")
        print(f"Player 2's deck: {hands[1]}")
    return sum((k+1)*v for k, v in enumerate(list(winningHand)[::-1]))

#print(part1(hands))
print(part2(hands))
