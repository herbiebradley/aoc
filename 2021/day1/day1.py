import numpy as np


def part1(data):
    return np.sum((data[1:] - data[:-1]) > 0)


with open("day1.txt", 'r') as file:
    data = np.array([int(x) for x in file.read().splitlines()])
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part1(np.convolve(data, [1, 1, 1], mode='valid'))}")
