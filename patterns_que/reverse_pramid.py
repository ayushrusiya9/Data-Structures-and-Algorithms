rows = 5

# for i in range(1,rows + 1):

#     for space in range(i-1):
#         print(" ",end="")

#     for star in range(2*(rows - i) + 1):
#         print("*",end="")

#     print()

for i in range(1,rows + 1):
    print(' '*(i - 1),"*"*(2*(rows - i) + 1))