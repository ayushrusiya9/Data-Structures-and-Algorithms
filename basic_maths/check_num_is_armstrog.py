def checkArmstrong(n):
    """
    check given num is armstrong or not.
    """
    k = len(str(n))
    num = n
    sum = 0
    while 0 < n:
        last_dig = n % 10
        sum = sum + last_dig ** k
        n = n // 10
    return sum == num

print(checkArmstrong(407))