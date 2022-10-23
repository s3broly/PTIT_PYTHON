import math
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True
def check(n):
    cout1=cout2=0
    for i in n:
        if nto(int(i)):
            cout1+=1
        else:
            cout2+=1
    if nto(len(n)) and cout1>cout2:
        return True
    else:
        return False    
t =  int(input())
while t>0:
    t-=1
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")