import functools
import itertools
import re

binar = functools.partial(int, base=2)


def part1(data):
    memory = {}
    idx_re = re.compile("1|0")
    for line in data:
        if line.startswith('mask'):
            matches = [(match.group(), match.start()) for match in re.finditer(idx_re, line[7:])]
        else:
            address = line[line.index('[') + 1:line.index(']')]
            num_str = line[line.index('= ') + 1:]
            binary_str = format(int(num_str), f"0{len(num_str)}b")
            binary_str = "0" * (36 - len(binary_str)) + binary_str
            for num, idx in matches:
                binary_str = binary_str[:idx] + num + binary_str[idx + 1:]

            memory[address] = int(binary_str, 2)
    return sum(memory.values())


def part2(data):
    memory = {}
    mask = ""
    for line in data:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            addr = line[line.index('[') + 1:line.index(']')]
            num = int(line[line.index('= ') + 1:])
            addr = format(int(addr), f"0{len(addr)}b")
            addr = "0" * (36 - len(addr)) + addr

            templ = ''.join(['1' if mask[i] == '1' else addr[i] if mask[i] == '0' else 'X' for i in range(len(mask))])
            res = map(binar, (''.join(n) for n in itertools.product(*[(c) if c != 'X' else ('1', '0') for c in templ])))

            for address in res:
                memory[address] = num

    return sum(memory.values())


if __name__ == "__main__":
    with open('day14.txt', 'r') as file:
        data = file.read().splitlines()
    print(part1(data))
    print(part2(data))
