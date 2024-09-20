l1=input("Enter the character in Uppercase separated by commas ").split(",")
t1=[]
temp=[]
for e in l1:
    temp.clear()
    temp.append(e)
    temp.append(ord(e))
    t1.append(tuple(temp))
print(t1)


