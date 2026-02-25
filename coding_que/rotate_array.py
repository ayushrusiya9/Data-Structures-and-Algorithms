def rotate_array(arr,elements):
    s = len(arr) - elements
    f = arr[s:]
    l = arr[:s]
    return f[-1::-1] + l

print(rotate_array([1,2,3,4,5,6,7,8],5))