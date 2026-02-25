s1 = "ayush"
s2 = "rusiy"

# d1 = {}
# d2 = {}

# if len(s1) == len(s2):
#     for i in s1:
#         d1[i] = d1.get(i, 0) + 1
#     for i in s2:
#         d2[i] = d2.get(i, 0) + 1
    
#     if d1 == d2:
#         print("Anagram")
# else:
#     print("not anagram")

# d = {}

# if len(s1) == len(s2):
#     for i in s1:
#         d[i] = d.get(i, 0) + 1
#     for i in s2:
#         d[i] = d.get(i, 0) - 1

#     for i in d.values():
#         if i != 0:
#             False
#         else:
#             True

# print(d)
s = "anagram"
t = "anagram"

data = [0]*26

if len(s) == len(t):
    for i in range(len(s)):
        data[ord(s[i]) - ord('a')] += 1
        data[ord(t[i]) - ord('a')] -= 1
    for i in data:
        if i == 0:
               print("angram")
            
    
    