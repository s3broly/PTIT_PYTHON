import math
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True
def tongcs(n):
    s=0
    for i in n:
        s += int(i)
    return s 
t = int(input())
while t>0:
    t-=1
    n = input()
    s = tongcs(n)
    if nto(s):
        print("YES")
    else:
        print("NO")