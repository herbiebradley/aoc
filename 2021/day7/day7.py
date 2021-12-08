import math

import numpy as np


def part1(data):
    y = np.array(data)
    return int(np.sum(np.abs(y - np.median(y))))


def part2(data):
    y = np.array(data)
    mean = np.mean(y)
    return int(min(np.sum((y - math.floor(mean)) ** 2 + np.abs(y - math.floor(mean))) / 2,
               np.sum((y - math.floor(mean)) ** 2 + np.abs(y - math.floor(mean))) / 2))


with open("day7.txt", 'r') as file:
    data = list(map(int, file.read().splitlines()[0].split(',')))
print(part1(data))
print(part2(data))
