def fibonacci_series(n):
    if n == 0:
        print(0)
    elif n == 1:
        print("0 1")
    else:
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        
        for i in range(2,n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]     
            print(f"fibonacci series up to {n}th term.")
            print(" ".join(str(num) for num in fib))
fibonacci_series(6)
