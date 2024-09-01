str=input("Enter a string ")
match str:
    case str if str in "mysirg":
        print("One")
    case str if str in "education":
        print("Two")
    case str if str in "services":
        print("Three")
