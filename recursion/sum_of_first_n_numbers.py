def sumOfNumbers(n):
    sum = 0
    i = 1
    while i < n:
        sum = sum + i
        i = i + 1
    return sum

print(sumOfNumbers(10))