def ascendingNumberTriangle(n):
    c = 0
    for row in range(1,n+1):
        for col in range(1,row + 1):
            c = c + 1
            print(c, end=" ")
        print()

n = 5
ascendingNumberTriangle(n)