def firstUniqueChar(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        freq[char] = 1
    for index, char in enumerate(s):
        if freq[char] == 1:
            return index
    return -1

print(firstUniqueChar("ayush"))