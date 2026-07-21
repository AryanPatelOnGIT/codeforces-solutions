t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    f=0
    count=(b-(a%b))%b
    print(count)