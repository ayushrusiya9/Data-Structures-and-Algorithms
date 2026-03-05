def two_sum(nums, target):
    for i in range(1, len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j+1] == target:
                return "Yes!"
    return 'NO!!!'

print(two_sum([1, 2, 3, 4], 5))