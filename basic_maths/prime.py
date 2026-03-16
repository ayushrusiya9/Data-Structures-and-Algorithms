def primeNumber(n):
    """ if n == 2 :
        return True
    if n == 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True"""
    if n == 2:
        return True
    if n == 1:
        return True

    for i in range(2,n):
        if n % i == 0:
            return False
    return True
# print(primeNumber(12))
print(primeNumber(11))
