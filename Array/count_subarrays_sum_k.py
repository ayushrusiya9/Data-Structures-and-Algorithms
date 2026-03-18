# Count Subarrays with Sum Equal to k
# Given an array of integers and a number k, find the total number of continuous subarrays whose sum equals to k.

def count_subarrays_with_sum_k(arr, k):
    count = 0
    n = len(arr)
    for start in range(n):
        curr_sum = 0
        for end in range(start, n):
            curr_sum += arr[end]
            if curr_sum == k:
                count += 1
    return count

if __name__ == "__main__":
    arr = [1, 2, 3]
    k = 3
    print("Input:", arr)
    print("k:", k)
    print("Number of subarrays with sum k:", count_subarrays_with_sum_k(arr, k))
