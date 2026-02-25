def removeDuplicate(nums):
    k = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k = k + 1
        
    return k

ans = removeDuplicate([1,1,2])
print(ans)