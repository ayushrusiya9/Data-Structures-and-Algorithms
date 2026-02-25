def fabonaci(n):
    a = 0
    b = 1
    for _ in range(n+1):
        print(a)
        c = a + b
        a = b
        b = c

fabonaci(5)