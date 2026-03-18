# Longest Subarray with Sum Zero
# Given an array of integers, find the length of the longest subarray with a sum equal to zero.

def longest_subarray_with_sum_zero(arr):
    sum_indices = {}
    max_len = 0
    curr_sum = 0
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum == 0:
            max_len = i + 1
        elif curr_sum in sum_indices:
            max_len = max(max_len, i - sum_indices[curr_sum])
        else:
            sum_indices[curr_sum] = i
    return max_len

if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    print("Input:", arr)
    print("Length of longest subarray with sum 0:", longest_subarray_with_sum_zero(arr))
