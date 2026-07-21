n=int(input())
if 1<=n<=100:
    p=[0]*n
    q=[0]*n
    count=0
    for i in range(n):
        p[i],q[i]=map(int,input().split())
        if q[i]-p[i]>=2:
            count+=1
    print(count)
    