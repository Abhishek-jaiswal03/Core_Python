n=int(input("Enter the number "))
i=n
count=0
while(i>0):
    i//=10
    count+=1
print(count)