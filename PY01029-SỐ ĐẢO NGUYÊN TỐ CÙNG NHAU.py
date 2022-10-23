def NTCN(n,m):
        if(m==0):
            return n 
        return NTCN(m,n%m)
t = int(input())
while t>0:
    t-=1
    n = input()
    m = ""
    for i in n:
            m = i + m
    if NTCN(int(n),int(m))==1:
        print("YES")
    else:
        print("NO")
        