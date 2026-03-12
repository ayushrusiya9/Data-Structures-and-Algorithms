# Rotate Array
# Given an array, rotate it to the right by k steps.

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]

if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotated = rotate_array(arr, k)
    print(f"Original array: {arr}")
    print(f"Rotated by {k}: {rotated}")
