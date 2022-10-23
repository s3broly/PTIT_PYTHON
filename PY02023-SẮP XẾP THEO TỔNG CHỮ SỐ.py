def tongcs(n):
    s = 0
    while n>0:
        s = s + int(n%10)
        n/=10
    return s

t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    for i in range(n):
        print(tongcs(a[i]),end=' ')
    