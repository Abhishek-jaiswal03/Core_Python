n=eval(input("Enter some data "))
match n:
    case n if type(n)==int:
        print("Monday")
    case n if type(n)==float:
        print("Tuesday")
    case n if type(n)==complex:
        print("Wednesday")
    case n if type(n)==bool:
        print("Thursday")