def is_perfect_number(num):
    if num <= 0:
        return False
    
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    
    return sum_divisors == num

def is_armstrong_number(num):
    if num < 0:
        return False
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = 0
    
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    return sum_of_powers == num


num=int(input("Enter a nuumber: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")


if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

