n=int(input())
sum,count,i=0,1,1
while(count<=n):
    sum+=i
    i+=2
    count+=1
print("Sum=",sum)