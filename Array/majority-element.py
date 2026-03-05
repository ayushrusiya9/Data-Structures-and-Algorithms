def majority_element(nums):
    """
    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    you may assume that the majority element always exists in the array.
    """
    count = {}
    for num in nums:
        count[num] += 1
        if count.get(num) // 2 == 0:
            return num       
    return None
 
print(majority_element([2, 2, 1, 1, 1, 2, 2]))