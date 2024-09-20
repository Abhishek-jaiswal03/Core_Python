l1=input("Enter the elements in the given list separated by comma ").split(",")
same=[]
temp=[]
l1.sort()
alpha="abcdefghijklmnopqrstuvwxyz"
e=0
for e in range(0,26):
    temp.clear()
    for j in l1:
        if j.startswith(alpha[e]):
            temp.append(j)
    if len(temp)>0:
        same.append(tuple(temp))
print(same)