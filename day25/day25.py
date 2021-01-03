import math


def BSGS(a, p, r):
    m = math.ceil(math.sqrt(p - 1))
    baby_steps = {pow(r, u, p): u for u in range(m)}
    inv = pow(r, m * (p - 2), p)
    for i in range(m):
        y = (a * pow(inv, i, p)) % p
        if y in baby_steps:
            return i * m + baby_steps[y]


def part1(a, b):
    p = 20_201_227
    r = 7
    a_loop_size = BSGS(a, p, r)
    return pow(b, a_loop_size, p)


if __name__ == "__main__":
    with open('day25.txt', 'r') as file:
        keys = list(map(int, file.read().splitlines()))
    key1, key2 = keys[0], keys[1]
    print(part1(key1, key2))
