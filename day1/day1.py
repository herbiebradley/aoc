def part1(nums):
    prods = set()
    for i in nums:
        prod = i * (2020 - i)
        if prod in prods:
            print(prod)
            break
        else:
            prods.add(prod)


def part2(nums):
    left, mid, right = 0, 1, len(nums) - 1
    while True:
        if nums[left] + nums[mid] + nums[right] == 2020:
            print(nums[left] * nums[mid] * nums[right])
            break
        elif nums[left] + nums[mid] + nums[right] < 2020 and mid < right - 1:
            mid += 1
        elif nums[left] + nums[mid] + nums[right] < 2020 and mid == right - 1:
            left += 1
            mid = left + 1
        elif nums[left] + nums[mid] + nums[right] > 2020 and mid < right - 1:
            right -= 1


if __name__ == "__main__":
    nums = []
    with open("day1.txt", 'r') as file:
        for line in file:
            nums.append(int(line.rstrip()))
    part1(nums)
    nums.sort()
    part2(nums)
