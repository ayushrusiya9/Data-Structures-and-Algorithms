def merge_sorted_arrays(arr1,m,arr2,n):
    i = m - 1
    j = n - 1
    k = m + n -1
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[i] = arr2[j]
            j -= 1
        k -= 1  
    
    
arr1 = [1,3,3,5,0,0,0]
arr2 = [2,4,6]

merge_sorted_arrays(arr1, 4, arr2, 3)
print(arr1)
