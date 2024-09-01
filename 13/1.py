"""n=int(input("Enter a number "))
count=0
while(n>0):
    n//=10
    count+=1
if count==3:
    print("Three digit number")
else:
    print("Not a three digit number")"""
n=int(input("Enter a number"))
count=0
while(n>0):
    n//=10
    count+=1
match count:
    case n if count==3:
        print("Three digit number ")
    case n if count!=3:
        print("Not a three digit number")