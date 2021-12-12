import numpy as np


def get_neighbours(x, y, grid):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for row, col in zip(dx, dy):
        final_row, final_col = x + row, y + col
        if 0 <= final_row < grid.shape[0] and 0 <= final_col < grid.shape[1]:
            yield final_row, final_col


def solve(data, part2=False):
    days = 1000 if part2 else 100
    flash_count = 0
    for step in range(days):
        flashed = np.zeros_like(data, dtype=bool)
        data += 1
        while True:
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    if data[i, j] > 9 and not flashed[i, j]:
                        data[i, j] = 0
                        flashed[i, j] = True
                        flash_count += 1
                        for row, col in get_neighbours(i, j, data):
                            if not flashed[row, col]:
                                data[row, col] += 1
            if not np.any(data > 9):
                if part2 and np.all(flashed):
                    return step
                break
    return flash_count


with open("day11.txt", 'r') as file:
    data = np.array([[int(c) for c in line] for line in file.read().splitlines()])
print(f"Part 1: {solve(data.copy())}")
print(f"Part 2: {solve(data, part2=True)}")
