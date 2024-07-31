a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
ls=[]
for i in range(1,max(a,b)+1):
    if a %i==0 and b%i==0:
        ls.append(i)

print("GCD=",max(ls))    
