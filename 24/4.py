print("Enter the 9 elemets of first list row wise")
l1=[
    [int(s) for s in input().split(',')],
    [int (s) for s in input().split(',')],
    [int (s) for s in input().split(',')]
]     
print("Enter the 9 elemets of second list row wise")
l2=[
    [int(s) for s in input().split(',')],
    [int (s) for s in input().split(',')],
    [int (s) for s in input().split(',')]
]  
l3=[[0,0,0],[0,0,0],[0,0,0]]   
for i in range(0,3):
    for j in range(0,3):
        l3[i][j]=l1[i][j]+l2[i][j]
        print(l3[i][j],end=" ")
    print()

    