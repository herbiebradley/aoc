def part1(data):
    pos, depth = 0, 0
    for line in data:
        if line[0] == "f":
            pos += int(line[-1])
        elif line[0] == "u":
            depth -= int(line[-1])
        else:
            depth += int(line[-1])

    return pos * depth


def part2(data):
    pos, depth, aim = 0, 0, 0
    for line in data:
        if line[0] == "f":
            pos += int(line[-1])
            depth += aim * int(line[-1])
        elif line[0] == "u":
            aim -= int(line[-1])
        else:
            aim += int(line[-1])

    return pos * depth


with open("day2.txt", 'r') as file:
    data = file.read().splitlines()
print(part1(data))
print(part2(data))
