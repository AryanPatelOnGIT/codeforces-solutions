eq=input()
if '+' in eq:
    l1=list(eq.split('+'))
    l1.sort()
    print(('+'.join(l1)))
else:
    print(eq)