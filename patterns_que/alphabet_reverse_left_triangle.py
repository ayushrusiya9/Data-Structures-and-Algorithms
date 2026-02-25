def alphabetReverseTriangle(n):
    alpha = ord("A")
    for row in range(n,0,-1):
        for col in range(0,row):
            print(chr(alpha + col),end=" ")
        print()

q = 5
alphabetReverseTriangle(q)
