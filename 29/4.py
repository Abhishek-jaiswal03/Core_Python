l1={"Abhishek","Suraj","Kiran","Raju","Hemanth","Rajesh","Ravi"}
bhat={"Suraj","Kiran","Raju","Ravi"}
rshoes={"Suraj","Raju","Hemanth","Ravi"}
"""for p1 in l1:
    if p1  in bhat and p1 in rshoes:
        print(p1)  OR"""
s1=bhat.intersection(rshoes)#intersection is set class method which return a set with common elements of both sets
print(s1)
