n=input()
if 1<=len(n)<=(10**9):
    count=0
    for ch in n:
        if ch=='4' or ch=='7':
            count+= 1
    if count==4 or count ==7:
        print("YES")
    else:
        print("NO")