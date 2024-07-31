x=int(input("Enter 1st numbers: "))
y=int(input("Enter 2nd numbers: "))
z=int(input("Enter 3rd numbers: "))
if x>y and x>z:
    print("Maximum number is ",x)
elif y>x and y>z:
    print("Maximum number is ",y)
else:
    print("Maximum number is ",z)