row = 5

for i in range(1,row + 1):

    for space in range(row -  i):
        print(" ",end="")
    
    for star in range(2 * i - 1):
        print("*",end="")
    
    print()

rows = 5

for i in range(1,rows + 1):

    for space in range(i-1):
        print(" ",end="")

    for star in range(2*(rows - i) + 1):
        print("*",end="")

    print()