def print_pattern():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print("/", end="")
        for j in range(1, i + 1):
            print("\\", end="")
        print()

print_pattern()
