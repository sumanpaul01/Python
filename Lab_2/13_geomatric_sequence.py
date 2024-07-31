
first_term = 2
common_ratio = 3
number_of_terms = 6

# Print the first 6 terms of the geometric sequence
print("The first 6 terms of the geometric sequence are:")
for n in range(number_of_terms):
    term = first_term * (common_ratio ** n)
    print(term)
