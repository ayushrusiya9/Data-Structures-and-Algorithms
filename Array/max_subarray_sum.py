# Maximum Sum Subarray (Kadane's Algorithm)
# Given an array of integers, find the maximum sum of a contiguous subarray.
# Example: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] => Output: 6

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum sum of contiguous subarray:", max_subarray_sum(arr))
