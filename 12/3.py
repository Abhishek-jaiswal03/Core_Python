a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("enter the value of c")) 
d=b*b-4*a*c 
if d>0:
    print("Real and Distict roots")
else:
    if d==0:
        print("Real  and Equal roots")
    else:
        print("Imaginary roots")  