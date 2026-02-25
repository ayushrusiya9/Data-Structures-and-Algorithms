# count digits.
def count_digit(n):
    count = 0
    for char in str(n):
        count += 1
    return count   

n = 123456789123456789
print(count_digit(n))