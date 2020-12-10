def part1(nums):
    prods = set()
    for i in range(len(nums)):
        if i >= 25:
            for j in range(i - 25, i):
                prod = nums[j] * (nums[i] - nums[j])
                if prod in prods:
                    break
                else:
                    prods.add(prod)
            else:
                return nums[i]


def part2(nums, p1_num):
    cumul_sum, left, right = 0, 0, 0
    while cumul_sum != p1_num:
        while cumul_sum < p1_num:
            cumul_sum += nums[right]
            right += 1
        else:
            cumul_sum -= nums[left]
            left += 1
    return min(nums[left:right - 1]) + max(nums[left:right - 1])


if __name__ == "__main__":
    with open("day9.txt", 'r') as file:
        nums = [int(x) for x in file.read().splitlines()]
    p1_num = part1(nums)
    p2_num = part2(nums, p1_num)
    print(f"Part 1: {p1_num}\nPart 2: {p2_num}")
