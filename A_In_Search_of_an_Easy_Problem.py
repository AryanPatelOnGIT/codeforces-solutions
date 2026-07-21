n=int(input())
l1=list(map(int,input().split()))
if len(l1)==n:
    if 1 in l1:
        print("HARD")
    else:
        print("EASY")
