def sum_of_natural_numbers(n):
  return n * (n + 1) // 2
n = int(input("Enter the upper limit: "))
sum_of_numbers = sum_of_natural_numbers(n)
print("The sum of natural numbers up to", n, "is:", sum_of_numbers)

