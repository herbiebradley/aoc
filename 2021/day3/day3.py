import numpy as np


def part1(data):
    m = len(data[0])
    a = 1 << np.arange(m)[::-1]
    data = (((np.array([int(x, 2) for x in data])[:, None] & a)) > 0).astype(int)
    gamma, epsilon = np.empty(m, dtype=bool), np.empty(m, dtype=bool)
    for pos in range(m):
        gamma[pos] = np.argmax(np.bincount(data[:, pos]))
        epsilon[pos] = np.argmin(np.bincount(data[:, pos]))
    return gamma.dot(a) * epsilon.dot(a)


def find_rating(arr: np.ndarray, bit_criteria: str = 'most'):
    pos = 0
    while pos < len(arr[0]) and len(arr) > 1:
        bins = np.bincount(arr[:, pos])
        if bit_criteria == 'most':
            bit = 1 if np.argmax(bins) == np.argmin(bins) else np.argmax(bins)
        elif bit_criteria == 'least':
            bit = 0 if np.argmax(bins) == np.argmin(bins) else np.argmin(bins)

        arr = arr[(arr[:, pos] == bit), :]
        pos += 1
    return arr[0]


def part2(data):
    a = 1 << np.arange(len(data[0]))[::-1]
    data = (((np.array([int(x, 2) for x in data])[:, None] & a)) > 0).astype(int)
    oxy = find_rating(data, bit_criteria='most')
    co2 = find_rating(data, bit_criteria='least')
    return oxy.dot(a) * co2.dot(a)


with open("day3.txt", 'r') as file:
    data = file.read().splitlines()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
