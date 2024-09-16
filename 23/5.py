l1=[1,2,3,4,5,6,7,8,9,10]
i=0
l=[]
while(i<len(l1)):
    if i%2==0:
        l.append(l1[i])
    i+=1   
print(l)
