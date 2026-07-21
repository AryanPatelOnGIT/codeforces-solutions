import math
t=int(input())
if 1<=t<=500:
    for i in range(t):
        n=int(input())
        if 1<=n<=100:
            y,r=map(int,input().split())
            if 1<=y<2*n or 1<=r<=n:
                count =0
                while y>0:
                    count+=1
                    y-=1
                count=math.floor(count//2)
                if r>0:
                    count =(count+r)
                if count>n:
                    print(n)
                else:
                    print(count)
            else:
                print(0)