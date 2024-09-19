str=input("Enter the string  ")
l1=str.split(" ")
max=0
for e in l1:
    if len(e)>max:  #built in methods of str
        max=len(e)
        str2=e
    
print(str2)