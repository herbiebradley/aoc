from sympy.ntheory.modular import crt


def part1(depart, times):
    smallest_mod, smallest_bus = depart, 0
    for _, bus in times:
        mod = bus - (depart % bus)
        if mod < smallest_mod:
            smallest_mod, smallest_bus = mod, bus
    return smallest_mod * smallest_bus


def part2(times):
    ind, mods = [-i % bus for (i, bus) in times], [bus for (i, bus) in times]
    t, N = crt(mods, ind)
    return t % N


if __name__ == "__main__":
    with open('day13.txt', 'r') as file:
        data = file.read().splitlines()
        depart = int(data[0])
        times = [(i, int(bus)) for (i, bus) in enumerate(data[1].split(',')) if bus != 'x']

    print(part1(depart, times))
    print(part2(times))
