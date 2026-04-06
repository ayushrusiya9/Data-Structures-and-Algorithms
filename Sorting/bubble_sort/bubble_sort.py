def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[i] < arr[j + 1]:
                arr[i], arr[j + 1] = arr[j + 1], arr[i]
                swapped = True

    if not swapped:
        return arr
    return arr
    
print(bubble_sort([5,4,3,2,1]))