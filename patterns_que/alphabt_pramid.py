def alphabetPramid(n):
    alpha = ord("A")
    for row in range(1,n+1):
        print(" "*(n - row),end="")
        for alp in range(0,row):
            print(chr(alpha + alp), end="")
        for alp in range(row - 2, -1, -1):
            print(chr(alpha + alp), end="")
        print()

alphabetPramid(4)