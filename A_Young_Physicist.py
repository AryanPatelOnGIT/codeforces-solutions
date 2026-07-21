t=int(input())
totx=0
toty=0
totz=0
for i in range(t):
    x,y,z=map(int,input().split())
    totx+=x
    toty+=y
    totz+=z
if(totx==0 & toty==0 & totz==0):

    print("YES")

else:
    print("NO")