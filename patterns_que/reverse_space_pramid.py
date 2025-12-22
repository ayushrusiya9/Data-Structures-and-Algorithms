def reverseSpacePramid(n):
    for row in range(1,n + 1):
        for num in range(1,row + 1):
            print(num,end="")
        print(" "*((n * 2) - (row + row)),end="")
        for num2 in range(row, 0,-1):
            print(num2,end="")
        print()

n = 4
reverseSpacePramid(n)
        