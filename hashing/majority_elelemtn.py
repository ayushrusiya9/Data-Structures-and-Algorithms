def majority_element(nums):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
        if hash_map[num] > len(nums) // 2:
            return num
    return -1

print(majority_element([2, 2, 1, 1, 1, 2, 2]))
