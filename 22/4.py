"""n=int(input("enter a number "))
n1=bin(n)
print(n1)"""
n=int(input("Enter a number "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n//=2
a.reverse()
for e in a:
    print(e,end="")