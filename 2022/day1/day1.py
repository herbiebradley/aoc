from heapq import nlargest

with open("day1.txt", 'r') as file:
    data = file.read().split('\n\n')
res = [sum(tuple(map(int, chunk.split()))) for chunk in data]
print(max(res))
print(sum(nlargest(3, res)))
