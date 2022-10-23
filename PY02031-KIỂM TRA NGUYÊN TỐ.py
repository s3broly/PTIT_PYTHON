import math

def nto(n):
    if n<2:    
        return False
    for i in range(2 , int(math.sqrt(n)) + 1 ):
        if n%i==0:
            return False
    return True

n, m = [int(x) for x in input().split()]
a = [[0]] * n
for i in range(n) : a[i] = [int(x) for x in input().split()]
for i in range(n) :
    for j in range(m) :
        if nto(a[i][j]):
            a[i][j]=1
        else:
            a[i][j]=0        
for i in range(n) :
    for j in range(m) :
        print(a[i][j],end=' ')
    print()