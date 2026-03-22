# Problem: Maximum Sum Subarray (Kadane's Algorithm)
# Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum:", max_subarray_sum(arr))
