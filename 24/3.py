N=int(input("Enter the value of n:"))
l1=[]
i,count=2,0
while(i<=N):
    count=0
    for e in range(2,i+1):
        if(i%e==0):
            count+=1
    i+=1
    if count==2:
        l1.append(i)
print(l1)