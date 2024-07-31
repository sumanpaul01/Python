n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n+1):
        if n%i!=0:
            print(i,end=" ")
else:
    print("not prime")   