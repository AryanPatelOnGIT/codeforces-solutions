n=int(input())
l1=[""]*n
for i in range(n):
    l1[i]=input()
su=0
for x in l1:
    if x=="Tetrahedron":
        su+=4
    elif x=="Cube":
        su+=6
    elif x=="Octahedron":
        su+=8
    elif x=="Dodecahedron":
        su+=12
    elif x=="Icosahedron":
        su+=20
print(su)