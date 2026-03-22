# Problem: Longest Subarray with Sum = K
# Given an array of integers and an integer K, find the length of the longest subarray whose sum is equal to K.

def longest_subarray_with_sum_k(nums, k):
    sum_indices = {}
    current_sum = 0
    max_len = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum == k:
            max_len = i + 1
        if current_sum - k in sum_indices:
            max_len = max(max_len, i - sum_indices[current_sum - k])
        if current_sum not in sum_indices:
            sum_indices[current_sum] = i
    return max_len

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, 9]
    k = 15
    print("Length of longest subarray with sum", k, ":", longest_subarray_with_sum_k(arr, k))
