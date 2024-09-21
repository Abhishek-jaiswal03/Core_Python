l1=input("Enter the list elements separated by commas ").split(",")
i=0
for e in l1:
    if i!=l1.index(e):
        print("First occurance of string is = ",e)
        break
    i+=1
else:
    print("Not found")