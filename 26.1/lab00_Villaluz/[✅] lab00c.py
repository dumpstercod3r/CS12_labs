def missing(nums: list[int] | tuple[int, ...]) -> int:
    if not nums:
        return 1

    nums_set = set(nums)
    nums_max = max(nums_set)

    if nums_max < 0:
        return 1

    for num in range(1, nums_max):
        if num not in nums_set:
            return num

    return nums_max + 1

assert missing([0, 1]) == 2
assert missing(tuple()) == 1
assert missing([*(i for i in range(1, 350000)), 10**16]) == 350000