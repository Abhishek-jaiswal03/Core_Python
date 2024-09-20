t1=([ int(e) for e in input("Enter the numbers separated by commas ").split(",")])
sum=0
for e in t1:
    if e%2!=0:
        sum+=e

print(sum)