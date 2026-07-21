k,w,n=map(int,input().split())
if 1<=k<=1000 and 1<=w<=1000 and 0<=n<=(10**9):
    tot=0
    borrow=0
    tot = k * n * (n + 1) // 2 
    borrow=tot-w
    if borrow>0:
        print(borrow)
    else:
        print(0)