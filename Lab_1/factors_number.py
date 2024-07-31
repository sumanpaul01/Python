n=int(input("Enter a number: "))
ls=[]
for i in range(1,n+1):
    if n%i==0:
        ls.append(i)
print(ls)