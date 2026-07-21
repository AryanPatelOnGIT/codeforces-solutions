n=int(input())
if 1<=n<=(10**15):
    tot=0
    if n%2==0:
        print(n//2)
    else:
        print(-(n+1)//2)