def reverse_number(num):
    rev = 0
    while num > 0:
        lastDig = num % 10
        rev = rev * 10 + lastDig
        num = num // 10
    return rev 

print(reverse_number(1234))