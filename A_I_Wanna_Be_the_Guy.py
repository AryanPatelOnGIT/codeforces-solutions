n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.sort()
l2.sort()
l3=set(l1).union(set(l2))
if n==len(set(l3)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")