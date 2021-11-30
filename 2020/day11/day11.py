import re
from copy import deepcopy


def automata(seats, part1=True):
    while True:
        seats_copy = deepcopy(seats)
        for i in range(1, len(seats) - 1):
            for j in range(1, len(seats[0]) - 1):
                if seats_copy[i][j] == '.':
                    continue
                if part1:
                    occ_count = (int(seats[i - 1][j] == '#') + int(seats[i][j - 1] == '#') +
                                 int(seats[i + 1][j] == '#') + int(seats[i][j + 1] == '#') +
                                 int(seats[i - 1][j - 1] == '#') + int(seats[i - 1][j + 1] == '#') +
                                 int(seats[i + 1][j - 1] == '#') + int(seats[i + 1][j + 1] == '#'))
                else:
                    occ_count = 0
                    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                    for direction in directions:
                        x = i
                        y = j
                        while True:
                            x += direction[0]
                            y += direction[1]
                            if not seats[x][y] == ".":
                                occ_count += int(seats[x][y] == "#")
                                break
                if seats_copy[i][j] == 'L' and occ_count == 0:
                    seats_copy[i][j] = '#'
                elif seats_copy[i][j] == '#' and ((part1 and occ_count >= 4) or (not part1 and occ_count >= 5)):
                    seats_copy[i][j] = 'L'
        if seats == seats_copy:
            break
        seats = seats_copy

    return sum([row.count('#') for row in seats])


if __name__ == "__main__":
    pattern = re.compile("L")
    with open('day11.txt', 'r') as file:
        seats = [['!'] + list(re.sub(pattern, '#', line)) + ['!'] for line in file.read().splitlines()]
        seats = [['!'] * len(seats[0])] + seats + [['!'] * len(seats[0])]
    print(f"Part 1: {automata(seats)}\nPart 2: {automata(seats, part1=False)}")
