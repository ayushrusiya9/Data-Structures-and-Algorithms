def isPalindrome(p):
    s = str(p)
    if p == s[::-1]:
        return True
    return False

print(isPalindrome("ayush"))
print(isPalindrome("madam"))
