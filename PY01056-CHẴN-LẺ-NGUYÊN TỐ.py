def nguyento(n):
    n = int(n)
    if(n<2):
        return False
    i=2
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True
def tongcs(n):
    s=0
    for i in n:
        s+=int(i)
    return s 
def check(n):
    for i in range(0,len(n)):
        if i%2==0:
            if ord(n[i])%2==0:
                return True
            else:
                return False
        else:
            if ord(n[i])%2!=0:
                return True
            else:
                return False
t = int(input())
while t>0:
    t-=1
    n = input()
    s = tongcs(n)
    if nguyento(s) and check(n):
        print("YES")
    else:
        print("NO")
    
    