scores = {"X": 1, "A": 1, "Y": 2, "B": 2, "C": 3, "Z": 3}


def part1(data):
    score = 0
    for row in data:
        p1 = row[0]
        p2 = row[-1]
        if scores[p1] == scores[p2]:
            score += 3 + scores[p2]
        elif p2 == "X":
            if p1 == "B":
                score += 0 + scores[p2]
            elif p1 == "C":
                score += 6 + scores[p2]
        elif p2 == "Y":
            if p1 == "A":
                score += 6 + scores[p2]
            elif p1 == "C":
                score += 0 + scores[p2]
        elif p2 == "Z":
            if p1 == "B":
                score += 6 + scores[p2]
            elif p1 == "A":
                score += 0 + scores[p2]
    return score


def part2(data):
    score = 0
    for row in data:
        p1 = row[0]
        outcome = row[-1]
        if outcome == "Y":
            score += scores[p1] + 3
            continue
        if p1 == "A":
            if outcome == "Z":  # win
                score += 6 + 2
            else:  # lose
                score += 3
        if p1 == "B":
            if outcome == "Z":
                score += 6 + 3
            else:
                score += 1
        if p1 == "C":
            if outcome == "Z":
                score += 6 + 1
            else:
                score += 2
    return score


with open("day2.txt", 'r') as file:
    data = file.read().splitlines()

print(part1(data))
print(part2(data))
