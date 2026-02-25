def count_dig_in_num(n):
    count = 0
    for _ in str(n):
        count += 1
    return count

print(count_dig_in_num(123))

# other way 
def count_dig(n):
    count = 0
    while n > 0:
        n = n // 10 
        count += 1
    return count

print(count_dig(1234))