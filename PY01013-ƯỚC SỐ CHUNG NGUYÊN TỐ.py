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
def tongcs(n):
    s=0
    while n>0:
        s = s + int(n)%10
        n = int(n)/10
    return s   
t = int(input())
while t>0:
    t-=1
    n,m=input().split()
    res = NTCN(int(n),int(m))
    s = tongcs(res)
    if(check_prime_number(s)):
        print("YES")
    else:
        print("NO")
    
    