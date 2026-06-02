def productExceptSelf(nums: list[int]) -> list[int]:
    """Return array where each element is the product of all others (O(n) time, O(1) extra space)."""
    n = len(nums)
    if n == 0:
        return []

    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
