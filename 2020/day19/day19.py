import re


def generate_regex(rules, current_rule, part2=False):
    if part2 and current_rule == "8 11":
        result = []
        fourtwo = generate_regex(rules, rules[42])
        threeone = generate_regex(rules, rules[31])
        for i in range(1, 50):
            result.append(f"{fourtwo}{{{i}}}{threeone}{{{i}}}")
        return "(" + fourtwo + ")+" + "(" + "|".join(result) + ")"

    if "a" in current_rule or "b" in current_rule:
        return current_rule[1]
    if "|" in current_rule:
        or_rules = [r.split() for r in current_rule.split("|")]
        result = (("".join(generate_regex(rules, rules[int(rule)]) for rule in or_rules[0])), "|",
                  "".join(generate_regex(rules, rules[int(rule)]) for rule in or_rules[1]))
    else:
        result = ("".join(generate_regex(rules, rules[int(rule)]) for rule in current_rule.split(" ")))

    return "(" + "".join(result) + ")"


def part1(rules, messages):
    match_count = 0
    regex = re.compile("^" + generate_regex(rules, rules[0]) + "$")
    for message in messages:
        if re.match(regex, message):
            match_count += 1
    return match_count


def part2(rules, messages):
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    regex = re.compile("^" + generate_regex(rules, rules[0], part2=True) + "$")
    match_count = 0
    for message in messages:
        if re.match(regex, message):
            match_count += 1
    return match_count


if __name__ == "__main__":
    with open('day19.txt', 'r') as file:
        data = file.read().splitlines()
    rules = {int(line[:line.index(":")]): line[line.index(": ") + 2:] for line in data if ":" in line}
    messages = [line for line in data if "a" in line and "b" in line]
    print(part1(rules, messages))
    print(part2(rules, messages))
