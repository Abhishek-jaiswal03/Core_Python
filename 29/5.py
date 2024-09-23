N=int(input("Enter the sum of dice number "))
s1=set()
for i in range(1,7):#first dice
    for j in range(1,7):#second dice 
        sum=i+j
        if sum==N:
            s1.add((i,j))
print(s1)

    