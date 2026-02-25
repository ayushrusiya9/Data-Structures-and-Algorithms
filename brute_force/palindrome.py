def checkPalindrome(num):
    s_num = str(num)
    if s_num == s_num[::-1]:
        print("Palindrome")
    else:
        print('Not Palindrom')

n = input("enter: ")
checkPalindrome(n)