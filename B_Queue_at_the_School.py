n,t=map(int,input().split())
if 1<=n<=50 and 1<=t<=50:
    st=input()
    if len(st)==n:
        st1=list(st)
        for s in range(t):
            i=0
            while i <n-1:
                if st1[i]=='B' and st1[i+1]=='G':
                    st1[i], st1[i+1] = st1[i+1], st1[i]
                    i+=2
                else:
                    i+=1
        st="".join(st1)
        print(st)
