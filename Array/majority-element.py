def majority_element(nums):
    """
    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    you may assume that the majority element always exists in the array.
    """
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        print(count)
        if count.get(num) // 2 == 0:
            print(count)
            return f'Majority Element is {num}'
        if count.get(num, 0) > len(nums) // 2:
            return f'Majority Element is {num}'
    return 'No Majority Element'
 
print(majority_element([2, 2, 1, 1, 1, 2, 2,1 ,1,1, 1]))