s=input("Enter the string ")
e=input("Enter the elements to search ")
for k in s:
    if(k==e):
        print("Elements presents in string")
        break
    
else:
    print("Element not found")