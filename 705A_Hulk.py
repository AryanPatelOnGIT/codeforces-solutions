n=int(input())
for i in range(1,n+1):
    if i==n and n%2!=0:
        print("I hate it")
    elif i%2==0 and i==n:
        print("I love it",end=" ")
    elif i%2==0:
        print("I love that",end=" ")
    else:
        print("I hate that",end=" ")