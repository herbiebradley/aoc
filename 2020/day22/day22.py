from collections import deque


def calc_score(deck):
    return sum(x * y for x, y in zip(reversed(deck), range(1, len(deck) + 1)))


def part1(deck1, deck2):
    while True:
        if len(deck1) == 0:
            return calc_score(deck2)
        elif len(deck2) == 0:
            return calc_score(deck1)

        if (num1 := deck1.popleft()) > (num2 := deck2.popleft()):
            deck1.extend((num1, num2))
        else:
            deck2.extend((num2, num1))


def part2(deck1, deck2):
    previous_rounds = set()

    while True:
        if len(deck1) == 0 or len(deck2) == 0:
            return (1, deck1) if len(deck1) > 0 else (0, deck2)

        state = tuple(deck1), tuple(deck2)
        if state in previous_rounds:
            return True, deck1

        previous_rounds.add(state)

        num1, num2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= num1 and len(deck2) >= num2:
            p1, _ = part2(deque(list(deck1)[:num1]), deque(list(deck2)[:num2]))
        else:
            p1 = int(num1 > num2)

        if p1 == 1:
            deck1.extend((num1, num2))
        else:
            deck2.extend((num2, num1))


if __name__ == "__main__":
    with open('day22.txt', 'r') as file:
        data = file.read()
    player1_deck = deque(map(int, data[10:data.index("Player 2") - 1].splitlines()))
    player2_deck = deque(map(int, data[data.index("Player 2") + 10:].splitlines()))
    print(part1(player1_deck.copy(), player2_deck.copy()))
    winner, deck = part2(player1_deck, player2_deck)
    print(calc_score(deck))
