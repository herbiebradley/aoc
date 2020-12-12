from copy import deepcopy


def part1(seats):
    while True:
        seats_copy = deepcopy(seats)
        for i in range(1, len(seats) - 1):
            for j in range(1, len(seats[0]) - 1):
                if seats_copy[i][j] == '.':
                    continue
                occ_count = (int(seats[i - 1][j] == '#') + int(seats[i][j - 1] == '#') + int(seats[i + 1][j] == '#') +
                             int(seats[i][j + 1] == '#') + int(seats[i - 1][j - 1] == '#') +
                             int(seats[i - 1][j + 1] == '#') + int(seats[i + 1][j - 1] == '#') +
                             int(seats[i + 1][j + 1] == '#'))
                if seats_copy[i][j] == 'L' and occ_count == 0:
                    seats_copy[i][j] = '#'
                elif seats_copy[i][j] == '#' and occ_count >= 4:
                    seats_copy[i][j] = 'L'
        if seats == seats_copy:
            break
        seats = seats_copy

    return sum([row.count('#') for row in seats])


def part2(seats):
    while True:
        seats_copy = deepcopy(seats)
        for i in range(1, len(seats) - 1):
            for j in range(1, len(seats[0]) - 1):
                if seats_copy[i][j] == '.':
                    continue
                first_seats = []
                directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
                for direction in directions:
                    x = i
                    y = j
                    while True:
                        x += direction[0]
                        y += direction[1]
                        if not seats[x][y] == ".":
                            first_seats.append(seats[x][y])
                            break
                occ_count = first_seats.count('#')
                if seats_copy[i][j] == 'L' and occ_count == 0:
                    seats_copy[i][j] = '#'
                elif seats_copy[i][j] == '#' and occ_count >= 5:
                    seats_copy[i][j] = 'L'
        if seats == seats_copy:
            break
        seats = seats_copy

    return sum([row.count('#') for row in seats])


if __name__ == "__main__":
    with open('day11.txt', 'r') as file:
        seats = [['!'] + list(line) + ['!'] for line in file.read().splitlines()]
        seats = [['!'] * len(seats[0])] + seats + [['!'] * len(seats[0])]
    print(f"Part 1: {part1(seats)}\nPart 2: {part2(seats)}")
