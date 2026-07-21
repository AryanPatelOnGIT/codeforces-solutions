n,k=map(int,input().split())
if 2<=n<=(10**9) and 1<=k<=50:
    for i in range(1,k+1):
        if n%10==0:
            n=n/10
        else:
            n=n-1
    print(int(n))