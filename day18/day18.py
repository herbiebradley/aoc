import re

parens = re.compile(r"\(([^()]+)\)")
plus = re.compile(r"(\d+)\s(\+)\s(\d+)")
times = re.compile(r"(\d+)\s(\*)\s(\d+)")
ops = re.compile(r"(\d+)\s([+*])\s(\d+)")


def add(string_tuple):
    string_tuple = string_tuple.groups()
    return str(int(string_tuple[0]) + int(string_tuple[2]))


def multiply(string_tuple):
    string_tuple = string_tuple.groups()
    return str(int(string_tuple[0]) * int(string_tuple[2]))


def parse(string):
    if match := re.search(parens, string):
        return parse(string.replace(match.group(), str(parse(match.group()[1:-1])), 1))

    match = re.search(ops, string)
    while match is not None:
        if match.groups()[1] == '+':
            string = re.sub(plus, add, string, count=1)
        else:
            string = re.sub(times, multiply, string, count=1)
        match = re.search(ops, string)
    return int(string)


def parsetwo(string):
    if match := re.search(parens, string):
        string = parsetwo(string.replace(match.group(), str(parsetwo(match.group()[1:-1])), 1))

    match = re.search(plus, string)
    while match is not None:
        string = re.sub(plus, add, string, count=1)
        match = re.search(plus, string)

    match = re.search(times, string)
    while match is not None:
        string = re.sub(times, multiply, string, count=1)
        match = re.search(times, string)
    return string


if __name__ == "__main__":
    with open('day18.txt', 'r') as file:
        data = file.read().splitlines()
    print(sum(parse(line) for line in data))
    print(sum(map(int, (parsetwo(line) for line in data))))
