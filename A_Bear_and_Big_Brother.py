a,b=map(int,input().split())
if 1<=a<=10 and 1<=b<=10:
    count=0
    while a-1<b:
        a*=3
        b*=2
        count+=1
    print(count)