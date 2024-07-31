n=int(input("Enter a number: "))
l=len(str(n))
for i in range(0,l):
    r=n%10
    n=n//10
    print(r,end="")

