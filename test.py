def winthegift(n , x):
    count =0
    while x > 0:
        count += 1
        if count > n:
            count = 1

        x -= 1
    return count
def main():
    s = input().split()
    n = int(s[0])
    x = int(s[1])
    print(winthegift(n , x))

main()
main()
