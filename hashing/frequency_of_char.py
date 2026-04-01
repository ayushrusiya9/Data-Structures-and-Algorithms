def frequency_of_char(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(frequency_of_char("ayushhh"))
            
