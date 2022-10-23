t = int(input())
for i in range(t):
    n,d = input().split()
    a = [int(x) for x in input().split()]
    for i in range(int(d),int(n)):
        print(a[i],end=' ')
    for i in range(0,int(d)):
        print(a[i],end=' ')
    print()
         