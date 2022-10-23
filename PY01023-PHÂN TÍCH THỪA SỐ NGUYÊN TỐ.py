def check_prime_number(n):
        if(n<2):
            return False
        i=2
        while i <= n/2:
            if(n%i == 0):
                return False
            i+=1
        return True
def phantich(n):
    print("1 * ",end="")
    if check_prime_number(n):
        print(str(n)+"^1",end="")
    else:
        for i in range(2,n):
            dem = 0
            while(n % i == 0):
                dem+=1
                n /= i
            if dem :
                print(i,end="")
                if dem >= 1 : 
                    print("^"+str(dem),end=" ")
                if n > i:
                    print("*",end=" ")
t = int(input())
while t>0:
    t-=1
    n = int(input())
    phantich(n)
    print()   
