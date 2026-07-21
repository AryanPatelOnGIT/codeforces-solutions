n1=input()
n2=input()
l1,l2=list((n1)),list((n2))
result=[0]*(len(l1))
for i in range(len(l1)):
    x=int(l1[i])+int(l2[i])
    if x==2:
        result[i]='0'
    else:
        result[i]=str(x)
for i in range (len(result)):
    print(result[i],end="")