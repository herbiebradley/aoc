def part1(data, num_steps):
    start = data[0]
    letters_dict = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in data[1:]}
    str_tree = []
    for i in range(len(start) - 1):
        str_tree.append(start[i:i + 2])
    for step in range(num_steps):
        new_lst = []
        for pair in str_tree:
            new_pair = letters_dict[pair]
            new_lst.append(pair[0] + new_pair)
            new_lst.append(new_pair + pair[1])
        str_tree = new_lst
    print(str_tree[0] + "".join([char[1] for char in str_tree[1:-2]]) + str_tree[-1])


with open("tst.txt", 'r') as file:
    data = [x for x in file.read().splitlines() if len(x) != 0]
print(part1(data, 3))
