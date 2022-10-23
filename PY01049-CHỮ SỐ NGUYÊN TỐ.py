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
t = int(input())
while t>0:
    t-=1
    n = input()
    l = len(n)
    cout1 = cout2 = 0
    for i in range(0,l):
        if(nguyento(n[i])):
            cout1+=1
        else:
            cout2+=1   
    if nguyento(l) and (cout1>cout2):
        print("YES")
    else:
        print("NO")
    