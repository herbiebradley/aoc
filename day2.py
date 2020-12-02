def part1(data):
    count = 0
    for (num_list, letter, password) in data:
        if password.count(letter) >= num_list[0] and password.count(letter) <= num_list[1]:
            count += 1
    print(count)


def part2(data):
    count = 0
    for (num_list, letter, password) in data:
        if (password[num_list[0] - 1] == letter) ^ (password[num_list[1] - 1] == letter):
            count += 1
    print(count)


if __name__ == "__main__":
    data = []
    with open("day2.txt", 'r') as file:
        for line in file:
            pw = line.rstrip().split()
            data.append((list(map(int, pw[0].split("-"))), pw[1][0], pw[2]))
    part1(data)
    part2(data)
