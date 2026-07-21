t=int(input())
if 1<=t<=100:
    for i in range(t):
        wrd=input().strip()
        if len(wrd)>=10 and wrd.islower():
            print(f"{wrd[0]}{len(wrd)-2}{wrd[-1]}")
        elif wrd.islower():
            print(wrd)