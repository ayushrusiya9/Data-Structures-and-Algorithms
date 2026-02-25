def alphabetLeftSide(n):
    alpha = ord("A")
    for row in range(0,n):
        for col in range(0,row + 1):
            print(chr(alpha + row),end=" ")
        print()

alphabetLeftSide(5)