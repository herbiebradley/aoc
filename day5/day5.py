with open("day5.txt", 'r') as file:
    seat_ids = {int(seat, 2) for seat in file.read().translate(str.maketrans("FBLR", "0101")).splitlines()}
print(f"Part 1: {max(seat_ids)}\nPart 2: {(set(range(min(seat_ids), max(seat_ids))) - seat_ids).pop()}")
