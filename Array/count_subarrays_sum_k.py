# Count Subarrays with Sum Equal to k
# Given an array of integers and a number k, find the total number of continuous subarrays whose sum equals to k.

def count_subarrays_with_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    seen_sums = {0: 1}

    for num in arr:
        prefix_sum += num
        count += seen_sums.get(prefix_sum - k, 0)
        seen_sums[prefix_sum] = seen_sums.get(prefix_sum, 0) + 1

    return count

if __name__ == "__main__":
    arr = [1, 2, 3]
    k = 3
    print("Input:", arr)
    print("k:", k)
    print("Number of subarrays with sum k:", count_subarrays_with_sum_k(arr, k))
