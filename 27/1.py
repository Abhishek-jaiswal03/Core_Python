l1=input("Enter the elements separated by comma ").split(",")
l2=[]
for e in l1:
    try:
        num=int(e)
        l2.append(num)
    except ValueError:
        pass
print(l2)
