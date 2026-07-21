n,k=map(int,input().split())
s=1
for i in range(1,n+1):
    if i%2==0 and s==1:
        print("."*(k-1)+"#")
        s=0
    elif i%2==0 and s==0:
        print("#"+"."*(k-1))
        s=1
    else:
        print("#"*k)