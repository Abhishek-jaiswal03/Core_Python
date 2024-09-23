S={2,4,3,9,8,7,11,17,19,22,33,44}
even=set()
odd=set()
for e in S:
    if e%2==0:
        even.add(e)
    else:
        odd.add(e)
print("Even numbers are :",even)
print("Odd numbers are:",odd)