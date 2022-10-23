t = int(input())
while t>0:
    t-=1
    n = input()
    k = input()
    n = n.split(k)
    print(len(n)-1)