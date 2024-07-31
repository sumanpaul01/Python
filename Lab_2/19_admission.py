m=int(input("Enter a marks of math: "))
p=int(input("Enter a marks of physics: "))
c=int(input("Enter a marks of Chemistry: "))
if m+c+p >=200 or m+p >=150:
    if m>=60 and p>=50 and c>=40:
        print("Your are eligible")
    else:
        print("Your are not eligible")
else:
    print("You are not eligible")
