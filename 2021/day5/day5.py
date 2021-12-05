from collections import defaultdict


def solve(data, calc_diagonals: bool = False):
    coords_map = defaultdict(int)
    for (x1, y1), (x2, y2) in data:
        if not calc_diagonals and x1 != x2 and y1 != y2:
            continue
        points_to_add = max(abs(x1 - x2), abs(y1 - y2))
        xs = range(x1, x2, (x2 - x1) // points_to_add) if x2 != x1 else [x1] * points_to_add
        ys = range(y1, y2, (y2 - y1) // points_to_add) if y2 != y1 else [y1] * points_to_add
        for x, y in zip(xs, ys):
            coords_map[(x, y)] += 1
        coords_map[(x2, y2)] += 1
    return len([key for key, value in coords_map.items() if value > 1])


with open("day5.txt", 'r') as file:
    input = [line.split(" -> ") for line in file.read().splitlines()]
    input = [[list(map(int, line[0].split(','))),
              list(map(int, line[1].split(',')))] for line in input]
print(f"Part 1: {solve(input, calc_diagonals=False)}")
print(f"Part 2: {solve(input, calc_diagonals=True)}")
