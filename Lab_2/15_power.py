b=int(input("Enter base value: "))
e=int(input("Enter exponent value: "))
re=1
for i in range(e):
    re*=b

print("The power value: ",re)