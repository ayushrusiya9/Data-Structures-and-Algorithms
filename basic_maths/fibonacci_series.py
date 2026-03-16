def fibonacciSeries(n):
    a = 0
    b = 1
    l = []
    i = 0
    while n > i:
        l.append(a)
        c = a + b
        a = b
        b = c 
        i = i + 1
    return l
print(fibonacciSeries(10))

