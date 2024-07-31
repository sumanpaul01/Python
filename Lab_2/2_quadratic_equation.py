import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-discriminant) / (2 * a)
        return (realPart + 1j * imaginaryPart, realPart - 1j * imaginaryPart)

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

roots = solve_quadratic(a, b, c)
print("Roots of the quadratic equation are:", roots)
