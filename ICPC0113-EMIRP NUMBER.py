import math
def nto(n):
    if n<2:    
        return False
    for i in range(2 , int(math.sqrt(n)) + 1 ):
        if n%i==0:
            return False
    return True
def check(n):
    m = str(n)[::-1]
    if nto(n) and nto(int(m)) and m != str(n): 
        return True
    return False
t = int(input())
for i in range(t):
    n = int(input())
    a=[]
    for i in range(10,int(n)):
        if check(i) and int(str(i)[::-1]) < n and i < int(str(i)[::-1]):
            print(i,int(str(i)[::-1]),end=' ')
    print()