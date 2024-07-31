def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base=int(input("Enter base value: "))
exponent=int(input("Enter exponent value: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
