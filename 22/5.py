n=int(input("Enter a number "))
a=[]
while(n>0):
    dig=n%8
    a.append(dig)
    n//=8
a.reverse()
for e in a:
    print(e,end="")