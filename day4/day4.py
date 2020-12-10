import re


def part1(data):
    valid_count = 0
    for passport in data:
        keystr = "".join(sorted(re.findall("(.{3}?):", passport)))
        if keystr == "byrcidecleyrhclhgtiyrpid" or keystr == "byrecleyrhclhgtiyrpid":
            valid_count += 1
    print(valid_count)


def part2(data):
    byr = re.compile(r"\b(byr:(19[2-9]\d|200[0-2]))\b")
    iyr = re.compile(r"\b(iyr:(201\d|2020))\b")
    eyr = re.compile(r"\b(eyr:(202\d|2030))\b")
    hgt = re.compile(r"\b(hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in))\b")
    hcl = re.compile(r"\b(hcl:#([0-9a-f]{6}))\b")
    ecl = re.compile(r"\b(ecl:(amb|blu|brn|gry|grn|hzl|oth))\b")
    pid = re.compile(r"\b(pid:(\d{9}))\b")
    print(sum([all([x.search(passport) for x in [byr, iyr, eyr, hgt, hcl, ecl, pid]]) for passport in data]))


if __name__ == "__main__":
    with open("day4.txt", 'r') as file:
        data = [re.sub('\n', ' ', x) for x in file.read().split("\n\n")]
    part1(data)
    part2(data)
