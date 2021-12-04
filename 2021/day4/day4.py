import numpy as np


def bingo(nums, boards, play_all: bool = False):
    boards_alive = set(range(boards.shape[0]))
    for num in nums:
        ind = np.where(boards == num)
        for k in [(ind[0][x], ind[1][x], ind[2][x]) for x in range(len(ind[0]))]:
            boards[k] = -1
        bingo_cols = np.where((boards == -1).all(axis=1))
        bingo_rows = np.where((boards == -1).all(axis=2))
        winning_boards = np.concatenate((np.unique(bingo_cols[0]),
                                         np.unique(bingo_rows[0])))
        for winning_board in winning_boards:
            if winning_board in boards_alive:
                if not play_all:
                    return np.sum(boards[winning_boards[0]]) * num
                boards_alive.remove(winning_board)
                last_won = boards[winning_board]
        if len(boards_alive) == 0:
            return np.sum(last_won[last_won > 0]) * num


with open("day4.txt", 'r') as file:
    input = file.read().splitlines()
nums = list(map(int, input[0].strip().split(',')))
for i, line in enumerate(input[2:]):
    if len(line) < 1:
        size = i
        break
num_boards = (len(input) - 1) // (size + 1)
boards = np.empty((num_boards, size, size), dtype=int)
for board in range(num_boards):
    board_data = [list(map(int, x.split())) for x in
                  input[board * (size + 1) + 2: (board + 1) * (size + 1) + 1]]
    boards[board] = np.array(board_data, dtype=int)

print(f"Part 1: {bingo(nums, boards.copy())}")
print(f"Part 2: {bingo(nums, boards, play_all=True)}")
