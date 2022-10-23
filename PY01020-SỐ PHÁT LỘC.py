t = int(input())
while t>0:
    t-=1
    s = input()
    l = len(s)
    k=0
    for i in s:
        if s[l-1]=="6" and s[l-2]=="8":
            k=1
    if k==1:
        print("YES")
    else:
        print("NO")