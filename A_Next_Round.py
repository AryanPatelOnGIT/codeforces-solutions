n,k=map(int,input().split())
if 1<=n<=50 and 1<=k<=50:
    a=list(map(int,input().split()))
    trgt=int(a[k-1])
    f=0
    count=0
    i=0
    for x in a:
        if int(x)>=trgt and x>0:
            count+=1
    print(count)
