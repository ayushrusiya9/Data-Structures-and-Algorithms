def isPalindrome(n):
    """rev = 0
    while n > 0:
        lastDig = n % 10
        rev = rev * 10 + lastDig
        n = n // 10
    if rev == n:
        return True
    return False"""
    rev = 0
    checkNum = n
    while n > 0:
        lastDig = n % 10
        rev = rev * 10 + lastDig
        n = n // 10 
    if rev ==  checkNum:
        return True
    return False

print(isPalindrome(1221))
