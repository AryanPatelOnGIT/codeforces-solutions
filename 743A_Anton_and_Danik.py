n=int(input())
if 1<=n<=1000000:
    st=input()
    if len(st)==n:
        acount=0
        dcount=0
        for ch in st:
            if ch=='A' or ch=='a':
                acount+=1
            elif ch=='D' or ch=='d':
                dcount+=1
        if acount>dcount:
            print("Anton")
        elif dcount>acount:
            print("Danik")
        else:
            print("Friendship")
    