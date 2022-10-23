def sum(n):
    s=0
    m = int(n)
    while m>0:
       s = s + m%10
       m = int(m/10)
    if s%10==0:
        return True
    else:
        return False
def check(n):
    l = len(n)
    for i in range(1,l):
        if abs(ord(n[i])-ord(n[i-1]))==2 :
            return True
        else:
            return False
t = int(input())
while t>0:
    t-=1
    n = input()
    if sum(n) and check(n):
        print("YES")
    else:
        print("NO")