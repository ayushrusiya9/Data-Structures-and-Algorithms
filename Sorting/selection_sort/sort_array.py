def selectionz_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        min_index = i
        for j in range(i + 1, l):
            if arr[i] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr

print(selectionz_sort([55,22,11,44,11,22,44,22]))