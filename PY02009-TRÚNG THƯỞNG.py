t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = []
    b = {}
    x = 0
    p = 1001
    for i in range(n):
        a.append(int(input()))
        if a[i] in b:
            b[a[i]]+=1
        else:
            b[a[i]]=1
    for i in range(n):
        if x < b[a[i]]:
            x = b[a[i]]
    for i in range(n):
        if b[a[i]]==x:
            if p > a[i]:
                p = a[i]
    print(p)