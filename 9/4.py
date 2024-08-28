n=int(input("Enter a number "))
count,temp =0,n
while temp>0:
    temp//=10
    count+=1
n//=10**(count-1)
print(n)