n=int(input())
if 1<=n<=100:
    l1=list(map(int,input().split()))
    tot=0
    tv=0
    for i in l1:
        tot=tot+i
    tv=len(l1)
    avg=tot/tv
    print(f"{avg:.12f}")