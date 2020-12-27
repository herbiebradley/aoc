import numpy as np
from scipy.signal import convolve


def game_of_life(board, dims, gens):
    kernel = np.ones([3] * dims, dtype=np.uint8)
    for _ in range(dims - 2):
        board = np.expand_dims(board, 0)

    for _ in range(gens):
        padded_board = np.pad(board, 1)
        nbrs_count = convolve(board, kernel) - padded_board
        board = (nbrs_count == 3) | (padded_board & (nbrs_count == 2))

    return np.sum(board)


if __name__ == "__main__":
    with open('day17.txt', 'r') as file:
        data = np.array([list(map(int, list(line)))
                         for line in file.read().translate(str.maketrans(".#", "01")).splitlines()], dtype=np.uint8)
    print(game_of_life(data, dims=3, gens=6))
    print(game_of_life(data, dims=4, gens=6))
