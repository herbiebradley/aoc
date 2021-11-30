import re


def walk(moves):
    dirs = {'e': (1, 0), 'w': (-1, 0), 'se': (1, 1), 'sw': (0, 1), 'ne': (0, -1), 'nw': (-1, -1)}
    x, y = 0, 0

    for move in moves:
        dx, dy = dirs[move]
        x += dx
        y += dy

    return x, y


def black_adjacent(grid, x, y):
    deltas = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
    return sum((x + dx, y + dy) in grid for dx, dy in deltas)


def all_neighbors(grid):
    deltas = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
    return set((x + dx, y + dy) for x, y in grid for dx, dy in deltas)


def part1(input):
    grid = set()
    rexp = re.compile(r'e|w|se|sw|ne|nw')

    for line in input:
        moves = rexp.findall(line)
        p = walk(moves)

        if p in grid:
            grid.remove(p)
        else:
            grid.add(p)

    return grid, len(grid)


def part2(grid):
    for _ in range(100):
        new = set()

        for p in all_neighbors(grid):
            n = black_adjacent(grid, *p)

            if n == 2 or (n == 1 and p in grid):
                new.add(p)
        grid = new

    return len(grid)


if __name__ == "__main__":
    with open('day24.txt', 'r') as file:
        data = file.read().splitlines()
    grid, result = part1(data)
    print(result)
    print(part2(grid))
