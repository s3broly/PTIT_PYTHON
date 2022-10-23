def NTCN(n,m):
        if(m==0):
            return n 
        return NTCN(m,n%m)
t = int(input())
while t>0:
    t-=1
    a=input()
    b=input()
    print(NTCN(int(a),int(b)))