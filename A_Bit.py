t=int(input())
s=0
f=0
if 1<=t<=150:
    for i in range(t):
        n=input()
        if n[0]=='+':
            s+=1
        elif n[0]=='-':
            s-=1
        elif n[-1]=='+':
            s+=1
        elif n[-1]=='-':
            s-=1
    print(s)