s1=input()
s2=input()
if 1<=len(s1)<=100 and 1<=len(s2)<=100:
    s1=s1.lower()
    s2=s2.lower()
    if s1>s2:
        print(1)
    elif s2>s1:
        print(-1)
    elif s1==s2:
        print(0)