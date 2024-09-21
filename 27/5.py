l1=input("Enter the string separated by commas ").split(",")
count=0
for e in l1:
    if e.endswith("s"):
        count+=1
print("Number of strings with s in end ",count)
