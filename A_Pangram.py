import re
n=int(input())
s=input()
if len(s)==n:
    tot=0
    s=s.lower()
    s=re.sub(r'[^\w\s]','',s)
    k=set(s)
    for i in k:
        tot+=ord(i)
    if tot>=2834:
        print("YES")
    else:
        print("NO")