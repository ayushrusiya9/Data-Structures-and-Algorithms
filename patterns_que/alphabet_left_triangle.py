def alphabetLeftTriangle(n):
    alpha = ord("A")
    for row in range(1,n+1):
        for col in range(0,row):
            print(chr(alpha + col),end=" ")
        print()

n = 5
alphabetLeftTriangle(n)