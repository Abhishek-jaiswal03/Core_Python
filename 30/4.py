N=int(input("Enter the number of data you want to enter "))
d1={}
for  e in range(N):
    batch_code=input(f"Enter the batch code for {e+1} element ")
    batch_size=input(f"Enter the batch size for {e+1} element ")
    d1[batch_code]=batch_size
max_batch_code=list(sorted(d1))[-1]
print(max_batch_code)