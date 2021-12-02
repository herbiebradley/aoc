def part1(data):
    pos, depth = 0, 0
    for line in data:
        num = int(line[-1])
        if line[0] == "f":
            pos += num
        elif line[0] == "u":
            depth -= num
        else:
            depth += num

    return pos * depth


def part2(data):
    pos, depth, aim = 0, 0, 0
    for line in data:
        num = int(line[-1])
        if line[0] == "f":
            pos += num
            depth += aim * num
        elif line[0] == "u":
            aim -= num
        else:
            aim += num

    return pos * depth


with open("day2.txt", 'r') as file:
    data = file.read().splitlines()
print(part1(data))
print(part2(data))
