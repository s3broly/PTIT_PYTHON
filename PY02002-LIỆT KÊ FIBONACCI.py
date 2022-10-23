a = [0, 1 , 1]
p1 = 1
p2 = 1
for i in range(3, 93) :
    k = p1 + p2
    a = a + [k]
    p2 = p1
    p1 = k
t = int(input())
while t>0:
    t-=1
    c,b = input().split()
    for i in range(int(c),int(b)+1):
        print(a[i],end=" ")
    print()    