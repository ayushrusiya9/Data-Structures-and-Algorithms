def twoSum(nums, target):
    # Ek empty dictionary banayein jo value aur uske index ko store karegi
    seen = {}
    
    # Array ke har element par traverse karein
    for index, num in enumerate(nums):
        # Hume kis number ki talaash hai?
        remaining = target - num
      
        if remaining in seen:
            return [seen[remaining], index]
            
        # Agar nahi dikha, toh current number aur uska index dictionary mein daal dein
        seen[num] = index
        
    return []  # Agar koi pair na mile (waise question ke mutabik hamesha milega)

# Test the function
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]