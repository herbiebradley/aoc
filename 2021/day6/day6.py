from collections import Counter


def solve(data, days):
    counts = Counter(data)
    for day in range(days):
        counts[(7 + day) % 9] += counts[day % 9]
    return sum(counts.values())


with open("day6.txt", 'r') as file:
    data = list(map(int, file.read().splitlines()[0].split(',')))
print(f"Part 1: {solve(data, days=80)}")
print(f"Part 2: {solve(data, days=256)}")
