t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    cout=1
    a.sort()
    b.sort()
    for i in range(n):
        if a[i]>b[i]:
            cout=0
    if cout==1:
        print("YES")
    else:
        print("NO")
