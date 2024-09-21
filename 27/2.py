l1=input("Enter the list elements separated b commas").split(",")
i=0
for e in l1:
    if i==l1.index(e):
        print(e, " ",l1.count(e))
    i+=1
