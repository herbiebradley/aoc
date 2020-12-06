with open("day6.txt", 'r') as file:
    groups = [grp.split("\n") for grp in file.read().rstrip().split("\n\n")]
print(f"Part 1: {sum([len(set(''.join(group))) for group in groups])}")
print(f"Part 2: {sum([len(set.intersection(*(map(set, group)))) for group in groups])}")
