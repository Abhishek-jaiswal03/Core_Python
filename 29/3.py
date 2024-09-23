s1={"Abhishek","Ayush","Karan","Preeti","Rohan"}
i=0
for p1 in s1:
    i+=1
    for p2 in list(s1)[i::]:#we want the first player to be mapped with all remaining players and then  second player with the remaining thats why slicing oprator.
        print(p1,p2)
    
    
