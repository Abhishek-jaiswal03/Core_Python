print("Enter the elements in list")
l1=[int(s) for s in input().split(",")]
l2=[]
l3=[]
for e in l1:
    if e>0:
        l2.append(e)
    else:
        l3.append(e)
print(l2)
print(l3)