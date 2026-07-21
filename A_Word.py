st1=input()
lcount=0
ucount=0
for ch in st1:
    if ch.islower():
        lcount+=1
    else:
        ucount+=1
if lcount>ucount:
    print(st1.lower())
elif ucount>lcount:
    print(st1.upper())
else:
    print(st1.lower())