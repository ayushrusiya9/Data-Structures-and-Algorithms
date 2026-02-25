row = 5

# for i in range(1,row + 1):

#     for space in range(row -  i):
#         print(" ",end="")
    
#     for star in range(2 * i - 1):
#         print("*",end="")
    
#     print()

for i in range(1,row + 1):
    print(" "*(row -i), "*"*((2*i) - 1))


    