import math

def print_factorial_series(N):
    for i in range(1, N + 1):
        print(math.factorial(i), end=", " if i < N else "\n")

n=int(input("Enter a number: "))
print("The factorial series up to", n, "terms is:")
print_factorial_series(n)
