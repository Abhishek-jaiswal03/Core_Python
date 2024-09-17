N=int(input("Enter the value of n:"))
l1=[]
i,count=2,0
while(count<N):
    if(i%2==0):
        l1.append(i)
        count+=1
    i+=1
print(l1)