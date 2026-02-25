def divisiorsOfNumber(num : int):
    '''
    all divisors of given number.
    '''
    d = 1
    n = []
    while d < num:
        if num % d == 0:
            n.append(d)
        d = d + 1
    return n

print(divisiorsOfNumber(32))   