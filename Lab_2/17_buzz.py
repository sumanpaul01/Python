def is_buzz_number(number):
  return number % 7 == 0 or number % 10 == 7

number =int(input("Enter a number: "))
if is_buzz_number(number):
  print(number, "is a Buzz number")
else:
  print(number, "is not a Buzz number")
