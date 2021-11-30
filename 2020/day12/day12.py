def navigate(instructions, rotation, part1=True):
    dirs = {'N': 0 + 1j, 'E': 1 + 0j, 'S': 0 + -1j, 'W': -1 + 0j, 'R': 0 - 1j, 'L': 0 + 1j}
    ship = 0 + 0j
    for letter, number in instructions:
        if letter in 'NSWE':
            if part1:
                ship += dirs[letter] * number
            else:
                rotation += dirs[letter] * number
        elif letter in 'LR':
            rotation *= dirs[letter] ** (number // 90)
        else:
            ship += rotation * number
    return round(abs(ship.real) + abs(ship.imag))


if __name__ == "__main__":
    with open('day12.txt', 'r') as file:
        instructions = [(line[0], int(line[1:])) for line in file.read().splitlines()]
    print(navigate(instructions, rotation=1 + 0j))
    print(navigate(instructions, rotation=10 + 1j, part1=False))
