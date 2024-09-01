n=int(input("Enter a number "))
match n:
    case n if n>0:
        print("Postive Number")
    case n if n<0:
        print("Negative number")
    case n if n==0:
        print("Zero")
