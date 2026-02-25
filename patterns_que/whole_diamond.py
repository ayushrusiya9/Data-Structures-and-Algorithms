def wholeDiamond(n):
    total = 2*n - 1

    for i in range(n-1):
        print("*"*(n-i), end="")
        if i > 0:
            print(" "*(2*i-1), end="")
        print("*"*(n-i))

    print("*" + " "*(total-2) + "*")

    for i in range(1, n):
        print("*"*i, end="")
        print(" "*(2*(n-i)-1), end="")
        print("*"*i)

wholeDiamond(5)
