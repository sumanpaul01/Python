def count_digits(number):

  if number == 0:
    return 1

  count = 0
  while number > 0:
    number //= 10
    count += 1
  return count
num = int(input("Enter a integer: "))
digit_count = count_digits(num)
print("Number of digits in", num, "is:", digit_count)
