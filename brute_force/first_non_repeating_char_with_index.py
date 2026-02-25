# Given a string s, find the first non-repeating character in the string and return its index.
# If no such character exists, return -1.

def first_non_repeating_char_with_index(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
    
    return -1