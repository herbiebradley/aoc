def part1(nums):
    one_diff, three_diff = 0, 1  # 1 because of the last adapter
    for i in range(1, len(nums)):
        one_diff += nums[i] - nums[i - 1] == 1
        three_diff += nums[i] - nums[i - 1] == 3
    return one_diff * three_diff


def part2(nums):
    nums.reverse()
    branches = {nums[0]: 1}
    for i in range(1, len(nums)):
        branches[nums[i]] = branches.get(nums[i] + 1, 0) + branches.get(nums[i] + 2, 0) + branches.get(nums[i] + 3, 0)
    return branches[0]


if __name__ == "__main__":
    with open("day10.txt", 'r') as file:
        nums = [int(x) for x in file.read().splitlines()]
    nums = [0] + sorted(nums)
    print(f"Part 1: {part1(nums)}\nPart 2: {part2(nums)}")
