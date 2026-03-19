# Find the length of the longest subarray with sum zero
# Example: arr = [1, 2, -2, 4, -4] => Output: 4 ([2, -2, 4, -4])

def longest_subarray_sum_zero(arr):
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
    arr = [1, 2, -2, 4, -4]
    print("Length of longest subarray with sum zero:", longest_subarray_sum_zero(arr))
