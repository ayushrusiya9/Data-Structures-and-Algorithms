li = [1,2,2,2,3,3,3,4,5,5,5]

def removeDuplicate(n):
    # print(n)
    n = set(n)
    # print(remove_dup)
    n = list(n)
    # print(set_to_list)
    n.sort()
    return n

ans = removeDuplicate(li)
print(ans,"lenth:", len(ans))
