def check(n):
    if len(n)%2==0:
        return False
    for i in range(0,len(n)):
        if n[0]!=n[1]:
            return True
    for i in range(0,len(n),2):
        if n[i]!=n[i-2]:
            return False
        else:
            return True
t = int(input())
while t>0:
    t-=1
    n = input()
    l = len(n)
    if check(n):
        print("YES")
    else:
        print("NO")