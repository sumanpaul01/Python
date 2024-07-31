
def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) // gcd(a, b)

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
result = lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", result)
