row = 5
for r in range(1,row + 1):
    print(" "*(row - r), "*"*r)
for c in range(row - r,0,-1):
    print("*"*c)
