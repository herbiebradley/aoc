def part1(nums):
    for i in range(len(nums)):
        if i >= 25:
            prods = set()
            for j in range(i - 25, i):
                prod = nums[j] * (nums[i] - nums[j])
                if prod in prods:
                    break
                else:
                    prods.add(prod)
            else:
                return nums[i]


def part2(nums, p1_num):
    for i in range(len(nums)):
        cumul_sum, smallest, largest = 0, max(nums), min(nums)
        for j in range(i, len(nums)):
            cumul_sum += nums[j]
            if cumul_sum > p1_num:
                break
            if cumul_sum == p1_num:
                return smallest + largest
            if nums[j] > largest:
                largest = nums[j]
            if nums[j] < smallest:
                smallest = nums[j]


if __name__ == "__main__":
    with open("day9.txt", 'r') as file:
        nums = [int(x) for x in file.read().splitlines()]
    p1_num = part1(nums)
    p2_num = part2(nums, p1_num)
    print(f"Part 1: {p1_num}\nPart 2: {p2_num}")
