n,h=map(int,input().split())
if 1<=n<=1000 and 1<=h<=1000:
    l1=list(map(int,input().split()))
    count=0
    for hi in l1:
        if hi>h:
            count+=2
        else:
            count+=1
    print(count)