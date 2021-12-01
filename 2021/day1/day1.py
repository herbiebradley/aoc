import numpy as np


def part1(data):
    return np.sum((data[1:] - data[:-1]) > 0)


def part2(data):
    return part1(np.sum(np.lib.stride_tricks.sliding_window_view(data, 3), axis=1))


with open("day1.txt", 'r') as file:
    data = np.array([int(x) for x in file.read().splitlines()])
    print(part1(data))
    print(part2(data))
