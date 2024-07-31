def print_multiples_of_ten(start, end):

  for num in range(start, end + 1):
    if num % 10 == 0:
      print(num, end=" ")

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print_multiples_of_ten(start, end)
