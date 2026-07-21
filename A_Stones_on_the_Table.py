n=int(input())
if 1<=n<=50:
    st1=input()
    if len(st1)==n:
        count=0
        result=""
        for i in range (n-1):
            if st1[i]==st1[i+1]:
                count+=1
        print(count)