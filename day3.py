import math


def part1(data, right, down):
    col, tree_count = right, 0
    for row_num in range(down, len(data), down):
        if data[row_num][col] == '#':
            tree_count += 1
        col = (col + right) % len(data[0])
    print(f"Right: {right}, down: {down} - {tree_count} trees.")
    return tree_count


def part2(data):
    res = math.prod([part1(data, 1, 1), part1(data, 3, 1), part1(data, 5, 1), part1(data, 7, 1), part1(data, 1, 2)])
    print(f"Result: {res}")


if __name__ == "__main__":
    data = []
    with open("day3.txt", 'r') as file:
        for line in file:
            data.append(line.rstrip())
    part2(data)
