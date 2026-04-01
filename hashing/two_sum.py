def two_sum(nums, target):
    freq = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in freq:
            return [freq[complement], index]
        freq[value] = index

print(two_sum([2,3,4,6,7], 9))