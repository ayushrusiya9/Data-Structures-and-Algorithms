def frquency_of_ele(l):
    freq = {}
    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(frquency_of_ele([1,2,3,4,5,6,6,7,8,8,8,8]))