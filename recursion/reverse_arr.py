def reverse_arr(n):
    l = len(n)
    ans = [0] * l 
    for i in range(l):
        ans[i] = n[l - 1 - i]
    return ans
print(reverse_arr([1,2,3,4,5]))
