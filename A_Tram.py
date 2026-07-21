n=int(input())
if 2<=n<=1000:
    a=[0]*n
    b=[0]*n
    tot=0
    mtot=0
    for i in range(n):
        a[i],b[i]=map(int,input().split())
        tot=tot+(b[i]-a[i])
        mtot=max(mtot,tot)
    print(mtot)