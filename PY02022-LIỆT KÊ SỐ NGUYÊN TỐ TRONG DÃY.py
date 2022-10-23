import math

def nto(n):
    if n<2:    
        return False
    for i in range(2 , int(math.sqrt(n)) + 1 ):
        if n%i==0:
            return False
    return True
    
n = int(input())
a = [int(x) for x in input().split()]
b={}
for i in range(0,n):
    if nto(a[i]):
        if a[i] in b:
            b[a[i]]+=1    
        else:
            b[a[i]]=1
for i in b:
    print(i,b[i],end=" ")
    print()
            