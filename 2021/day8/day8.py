from collections import defaultdict


def part1(outputs):
    digit_to_length = {1: 2, 4: 4, 7: 3, 8: 7}
    count = 0
    lengths_set = set(digit_to_length.values())
    for line in outputs:
        for string in line:
            if len(string) in lengths_set:
                count += 1
    return count


def part2(inputs, outputs):
    digit_to_length = {1: 2, 4: 4, 7: 3, 8: 7}
    result = 0
    for i, line in enumerate(inputs):
        linedct = defaultdict(list)
        for strset in line:
            linedct[len(strset)].append(strset)
        # get unique digits
        digitsmap = {
            1: linedct[digit_to_length[1]][0],
            4: linedct[digit_to_length[4]][0],
            7: linedct[digit_to_length[7]][0],
            8: linedct[digit_to_length[8]][0],
            linedct[digit_to_length[1]][0]: 1,
            linedct[digit_to_length[4]][0]: 4,
            linedct[digit_to_length[7]][0]: 7,
            linedct[digit_to_length[8]][0]: 8,
        }

        for digit in linedct[6]:  # length 6 digits
            if digitsmap[4] < digit:
                digitsmap[9] = digit
                digitsmap[digit] = 9
            elif digitsmap[1] < digit:
                digitsmap[0] = digit
                digitsmap[digit] = 0
            else:
                digitsmap[6] = digit
                digitsmap[digit] = 6
        for digit in linedct[5]:  # length 5 digits
            if digitsmap[1] < digit:
                digitsmap[3] = digit
                digitsmap[digit] = 3
            elif digit < digitsmap[6]:
                digitsmap[5] = digit
                digitsmap[digit] = 5
            else:
                digitsmap[2] = digit
                digitsmap[digit] = 2

        output_num = 0
        for digit in outputs[i]:
            output_num *= 10
            output_num += digitsmap[digit]
        result += output_num
    return result


with open("day8.txt", 'r') as file:
    data = [x.split(' | ') for x in file.read().splitlines()]
inputs = [line[0].split() for line in data]
inputs = [[frozenset(word) for word in strlist] for strlist in inputs]
outputs = [line[1].split() for line in data]
outputs = [[frozenset(word) for word in strlist] for strlist in outputs]
print(part1(outputs))
print(part2(inputs, outputs))
