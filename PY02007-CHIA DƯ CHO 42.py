n = 0
b=[0]*42
s=0
while True:
    a = [int(x) for x in input().split()]
    n += len(a)
    for i in a:
        if i%42 != 0:
            b [i%42] =1
        if i%42 == 0:
            b[0] = 1
    if n == 10 : break
for i in b:
    if i>0 :
        s+=1
print(s)