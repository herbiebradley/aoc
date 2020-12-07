import re


def contains_gold(data, name: str) -> bool:
    if data[name][0][0][1] == 0:
        return False
    elif data[name][1] is True:
        return True
    elif data[name][1] is False:
        return False
    contains: bool = False
    for (subname, subcount) in data[name][0]:
        if subname == "shiny gold":
            data[name][1] = True
            return True
        else:
            contains = contains or contains_gold(data, subname)
    data[name][1] = contains
    return contains


def bags_inside(data, name: str) -> int:
    if data[name][0][0][1] == 0:
        return 0
    count = 0
    for (subname, subcount) in data[name][0]:
        count += subcount + subcount * bags_inside(data, subname)
    return count


with open("day7.txt", 'r') as file:
    r = re.compile(r"[0-9]+\s[a-z]+\s[a-z]+")
    data = {}
    for line in file:
        if not re.search(r"\sno\s", line):
            data[line[:line.index("bags") - 1]] = [[(bag[2:], int(bag[:1])) for bag in re.findall(r, line)], None]
        else:
            data[line[:line.index("bags") - 1]] = [[('', 0)], None]

print(f"Part 1: {sum([contains_gold(data, col) for col in data])}")
print(f"Part 2: {bags_inside(data, 'shiny gold')}")
