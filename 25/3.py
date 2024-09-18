s=input("Enter the string ")
count=0
for e in s:
    if e.lower() in ('a','e','i','o','u'):
        count=count+1
    elif e.upper() in ('A','E','I','O','U'):
        count=count+1
print("Number of vowels in string is=",count)