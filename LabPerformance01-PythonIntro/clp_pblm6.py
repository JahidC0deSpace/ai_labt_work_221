def fibonacci(n):
    fib_series = [0, 1]
    
    for _ in range(n - 2):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
    
    return fib_series[:n]

num_terms = input("Give the num: ")
print("Fibonacci Series:", fibonacci(int(num_terms)))
