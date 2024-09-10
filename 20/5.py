for e in range(15,46):
    count=0
    for x in range(2,e):
        if e%x==0:
            count+=1
    if count==0:
        print(e ,end=" ")