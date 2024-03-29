def part1(data):
    pos, depth = 0, 0
    for line in data:
        if line[0] == 'f':
            pos += ord(line[8]) - 48
        elif line[0] == 'u':
            depth -= ord(line[3]) - 48
        else:
            depth += ord(line[5]) - 48

    return pos * depth


def part2(data):
    pos, depth, aim = 0, 0, 0
    for line in data:
        if line[0] == 'f':
            num = ord(line[8]) - 48
            pos += num
            depth += aim * num
        elif line[0] == 'u':
            aim -= ord(line[3]) - 48
        else:
            aim += ord(line[5]) - 48

    return pos * depth


with open("day2.txt", 'r') as file:
    data = file.read().splitlines()
print(part1(data))
print(part2(data))
