from collections import deque


class LinkedListNode:
    def __init__(self, value):
        self.next = self.prev = None
        self.value = value


class CircularLinkedList:
    def __init__(self, values):
        self.lookup = {}
        head = prev = None
        for value in values:
            node = LinkedListNode(value)
            if not head:
                head = node
            if prev:
                prev.next = node
                node.prev = prev
            self.lookup[value] = prev = node
        head.prev = prev
        prev.next = head

    def get(self, key):
        return self.lookup[key]

    def move(self, key, destination):
        item, destination = self.lookup[key], self.lookup[destination]
        prev_next = destination.next
        item.prev.next = item.next
        item.next.prev = item.prev
        destination.next.prev = item
        destination.next = item
        item.prev = destination
        item.next = prev_next


def play(cups, iterations):
    ll = CircularLinkedList(cups)
    item = ll.get(cups[0])
    for _ in range(iterations):
        pickup = [item.next.value, item.next.next.value, item.next.next.next.value]
        destination = len(cups) if item.value == 1 else item.value - 1
        while destination in pickup:
            destination = len(cups) if destination == 1 else destination - 1
        while pickup:
            ll.move(pickup.pop(), destination)
        item = item.next
    return ll.get(1)


def part1(input: deque):
    min_cup, max_cup = min(input), max(input)
    for i in range(100):
        current = max_cup if input[0] == min_cup else input[0] - 1
        input.rotate(-1)
        one, two, three = input.popleft(), input.popleft(), input.popleft()
        while current == one or current == two or current == three:
            current = max_cup if current == min_cup else current - 1

        destination = input.index(current) + 1

        input.rotate(-1 * destination)
        input.extendleft((three, two, one))
        input.rotate(destination)

    destination = input.index(1)
    input.rotate(-1 * destination)
    input.popleft()
    return "".join(map(str, input))


def part2(input):
    result = play(input + list(range(10, 10**6 + 1)), 10**7)
    return result.next.value * result.next.next.value


if __name__ == "__main__":
    input = "562893147"
    print(part1(deque(list(map(int, list(input))))))
    print(part2(list(map(int, list(input)))))
