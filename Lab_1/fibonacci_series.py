def generate_fibonacci_series(n):
    fibonacci_series = []
    
    a, b = 0, 1
    
    while a <= n:
        fibonacci_series.append(a)
        a, b = b, a + b
    
    return fibonacci_series
n = int(input("Enter a number: "))
fib_series = generate_fibonacci_series(n)
print(f"Fibonacci series up to {n}:")
print(fib_series)
