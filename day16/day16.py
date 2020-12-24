import collections
import math
import re


def part1(fields, nearby):
    range_re = re.compile(r"(\d+\S\d+)")
    ranges = []
    for field in fields:
        ranges.append([list(map(int, match.split('-'))) for match in re.findall(range_re, field)])
    invalids = []
    to_remove = []
    for i, ticket in enumerate(nearby):
        for num in ticket:
            valid_fields = []
            for ran in ranges:
                r1_start, r1_end, r2_start, r2_end = ran[0][0], ran[0][1], ran[1][0], ran[1][1]
                valid_fields.append(r1_start <= num <= r1_end or r2_start <= num <= r2_end)
            if not any(valid_fields):
                invalids.append(num)
                to_remove.append(i)
                break

    new_nearby = [ticket for i, ticket in enumerate(nearby) if i not in to_remove]
    return sum(invalids), new_nearby


def part2(fields, ticket, nearby):
    range_re = re.compile(r"(\d+\S\d+)")
    ranges = []
    for field in fields:
        ranges.append([list(map(int, match.split('-'))) for match in re.findall(range_re, field)])

    valid_fields = collections.defaultdict(set)
    for i in range(len(nearby[0])):
        for j, ran in enumerate(ranges):
            r1_start, r1_end, r2_start, r2_end = ran[0][0], ran[0][1], ran[1][0], ran[1][1]
            if all([r1_start <= ticket[i] <= r1_end or r2_start <= ticket[i] <= r2_end for ticket in nearby]):
                valid_fields[fields[j][:fields[j].index(":")]].add(i)

    for _ in range(len(valid_fields)):
        for i, field in enumerate(valid_fields):
            if len(valid_fields[field]) == 1:
                field_idx = {valid_fields[field].pop()}
                for f in valid_fields:
                    valid_fields[f] -= field_idx
                valid_fields[field] = field_idx

    return math.prod([ticket[valid_fields[field].pop()] for field in valid_fields if field.startswith('dep')])


if __name__ == "__main__":
    with open('day16.txt', 'r') as file:
        data = file.read().splitlines()
    fields, ticket, nearby = [], [], []
    for i in range(len(data)):
        if data[i].startswith(('d', 'a', 'c', 'p', 'r', 's', 't', 'w', 'z')):
            fields.append(data[i])
        elif data[i].startswith('y'):
            ticket = list(map(int, data[i + 1].split(',')))
        elif data[i].startswith('n'):
            nearby = [list(map(int, (line.split(',')))) for line in data[i + 1:]]
    invalid_rate, nearby = part1(fields, nearby)
    print(invalid_rate)
    print(part2(fields, ticket, nearby))
