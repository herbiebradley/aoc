input = [9,6,0,10,18,2,1]
turn, last_num = 0, 0
spoken = {0: (0, 0)}

for i, num in enumerate(input):
    spoken[num] = (i + 1, 0)
    last_num = num
    turn += 1

while turn != 30000000:
    turn += 1
    if spoken[last_num][1]:
        last_turn, second_last_turn = spoken[last_num]
        last_num = last_turn - second_last_turn
        spoken[last_num] = (turn, spoken[last_num][0]) if last_num in spoken else (turn, 0)
    else:
        spoken[0] = (turn, spoken[0][0])
        last_num = 0
print(last_num)
