n=int(input())
l1=list(map(int,input().split()))
result=[0]*(n+1)
recive=0
for i in range(n):
    result[l1[i]]=i+1
for i in range(1,n+1):
    print(result[i],end=" ")
