# 3. Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
string = input("Enter a sequence of lines: ")
string = string.upper()
print("Lines after making all characters in the sentence capitalized: ", string, end="")