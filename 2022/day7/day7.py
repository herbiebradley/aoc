from anytree import Node, PostOrderIter


with open("/home/users/hyper1on/aoc/2022/day6/day6.txt", 'r') as file:
    data = file.read().splitlines()

root = Node("root", total_size=0)
current_dir = root
for line in data[1:]:
    if line.startswith("$ cd"):
        if line[5:] == "..":
            current_dir = current_dir.parent
        else:
            for child in current_dir.children:
                if child.name == line[5:]:
                    current_dir = child
                    break
    elif line.startswith("dir"):
        Node(line[4:], parent=current_dir, total_size=0)
    elif not line.isalpha() and line[0] != "$":
        file_size, _ = line.split()
        current_dir.total_size += int(file_size)

total_p1 = 0
smallest_big_dir = 100_000_000
for node in PostOrderIter(root):
    for child in node.children:
        node.total_size += child.total_size
    if node.total_size <= 100_000:
        total_p1 += node.total_size
size_req = 30000000 - (70000000 - root.total_size)
for node in PostOrderIter(root):
    if node.total_size >= size_req and node.total_size < smallest_big_dir:
        smallest_big_dir = node.total_size
print(total_p1)
print(smallest_big_dir)
