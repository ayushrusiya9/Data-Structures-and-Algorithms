def twoSum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        remaining = target - num
        match_index = seen.get(remaining)
        if match_index is not None:
            return [match_index, index]
        seen[num] = index
    return []

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target)) 