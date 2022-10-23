t = int(input())
while t:
    t-=1
    def NTCN(n,m):
        if(m==0):
            return n 
        return NTCN(m,n%m)
    
    def check_prime_number(n):
        if(n<2):
            return False
        i=2
        while i <= n/2:
            if(n%i == 0):
                return False
            i+=1
        return True
    def NT(n):
        k = 0
        for i in range(1,n):
            if NTCN(n,i)==1:
                k+=1
        return k
    
    n = int(input())
    g = NT(n)
    if  check_prime_number(g):
        print("YES")
    else:
        print("NO")
        