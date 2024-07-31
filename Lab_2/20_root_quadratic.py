import cmath

def find_roots(a, b, c):

  discriminant = b**2 - 4*a*c

  if discriminant > 0:
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
  elif discriminant == 0:
    root = -b / (2*a)
    return root, root
  else:
    real_part = -b / (2*a)
    imag_part = cmath.sqrt(-discriminant) / (2*a)
    root1 = complex(real_part, imag_part)
    root2 = complex(real_part, -imag_part)
    return root1, root2

# Example usage
a = 1
b = -5
c = 6

roots = find_roots(a, b, c)

if roots:
  print("The roots are:", roots)
else:
  print("The equation has no real roots.")
