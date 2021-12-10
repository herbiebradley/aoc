from collections import deque

import numpy as np


def solve(data):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137,
              '(': 1, '[': 2, '{': 3, '<': 4}
    brackets = {'[': ']', '<': '>', '{': '}', '(': ')'}
    corr_score = 0
    comp_scores = []
    linestack = deque()
    for line in data:
        comp_score = 0
        linestack.clear()
        for char in line:
            if char in brackets:
                linestack.append(char)
            elif char != brackets[linestack.pop()]:
                corr_score += scores[char]
                break
        else:
            while len(linestack) > 0:
                comp_score *= 5
                comp_score += scores[linestack.pop()]
            comp_scores.append(comp_score)

    return corr_score, int(np.median(comp_scores))


with open("day10.txt", 'r') as file:
    data = file.read().splitlines()
print(solve(data))
