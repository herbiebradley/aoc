from string import ascii_letters as alphabet

letters = {v: k + 1 for k, v in enumerate(list(alphabet))}
with open("day3.txt", 'r') as file:
    data = file.read().splitlines()

p1_result = 0
for line in data:
    first_half = {letters[i] for i in line[len(line) // 2:]}
    second_half = {letters[i] for i in line[:len(line) // 2]}
    p1_result += (first_half & second_half).pop()

print(p1_result)
p2_result = 0
for i in range(0, len(data), 3):
    e1, e2, e3 = {letters[i] for i in data[i]}, {letters[i] for i in data[i + 1]}, \
        {letters[i] for i in data[i + 2]}
    p2_result += (e1 & e2 & e3).pop()

print(p2_result)
