with open("day8.txt", 'r') as file:
    prog = [[line[0:3], int(line.rstrip()[4:]), -2] for line in file.read().splitlines()]


def terminates_at(prog, change_i=-1):
    acc, i = 0, 0
    while True:
        if i == len(prog) - 1:
            return (i, acc + prog[i][1]) if prog[i][0] == 'acc' else (i, acc)
        elif prog[i][2] == change_i:
            return i, acc
        prog[i][2] = change_i
        if prog[i][0] == 'acc':
            acc += prog[i][1]
        elif change_i >= 0 and i == change_i and prog[change_i][0] == 'jmp':
            i += 1
            continue
        elif prog[i][0] == 'jmp' or (change_i >= 0 and i == change_i and prog[change_i][0] == 'nop'):
            i += prog[i][1] - 1
        i += 1


print(f"Part 1: {terminates_at(prog)[1]}")
for i in range(len(prog)):
    if prog[i][0] != 'acc':
        ind, acc = terminates_at(prog, change_i=i)
        if ind == len(prog) - 1:
            print(f"Part 2: {acc}")
            break
