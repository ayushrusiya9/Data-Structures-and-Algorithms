def reverseAlphabet(n):
    for i in range(n):
        start = ord('E') - i
        for ch in range(start, ord('E') + 1):
            print(chr(ch),end=" ")
        print()

reverseAlphabet(5)