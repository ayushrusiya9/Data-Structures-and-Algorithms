def sub_array_sum(arr, target):
    """
    Given an array of integers and a target sum, determine if there is a contiguous subarray that sums up to the target."""
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            return True

    return False