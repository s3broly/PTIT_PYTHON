t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = sorted([int(x) for x in input().split()])    
    x=0
    b={}
    for i in range(n):
        if a[i] in b:
            b[a[i]]+=1
        else:
            b[a[i]]=1
    for i in range(n):
        if x < b[a[i]]:
            x = b[a[i]]
            p = a[i]
    if x > len(a)/2:
        print(p)
    else:
        print("NO")        