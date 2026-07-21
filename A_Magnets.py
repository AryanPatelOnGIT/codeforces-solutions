n = int(input())
l1 = [0] * n
for i in range(n):
    l1[i] = int(input())

count = 1              
current = [l1[0]]

for i in range(1, n):
    if l1[i] == l1[i-1]:
        current.append(l1[i])   
    else:
        count += 1              
        current = [l1[i]]       

print(count)    