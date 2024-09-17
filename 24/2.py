N=int(input("Enter the value of n:"))
l1=[0,1,1]
i,count,sum=2,0,0
while(count<=N-3):
    sum=l1[i]+l1[i-1]
    l1.append(sum)
    i+=1
    count+=1
    
print(l1)