m,n=map(int,input().split())
if 1<=m<=16 and 1<=n<=16:
    p=int(m*n)
    if p%2==0:
        print(p//2)
    else:
        print(int((p-1)//2))