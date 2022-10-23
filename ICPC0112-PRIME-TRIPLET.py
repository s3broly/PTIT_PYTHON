import math
def nto(n):
    if n<2:    
        return False
    for i in range(2 , int(math.sqrt(n)) + 1 ):
        if n%i==0:
            return False
    return True
    
t = int(input())
for i in range(t):
    n = int(input())
    cout=0
    for i in range(n):
        if nto(i) and i+6 < n:
            if (nto(i+2) and nto(i+6)):
                cout+=1
            if (nto(i+4) and nto(i+6)):
                cout+=1
    print(cout)