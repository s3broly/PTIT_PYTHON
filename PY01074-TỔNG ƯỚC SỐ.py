import math

def nto(n):
    if n<2:    
        return False
    for i in range(2 , int(math.sqrt(n)) + 1 ):
        if n%i==0:
            return False
    return True
    
def phantich(n):
    sum = 0
    if nto(n) or n < 2:
        return n
    else:
        for i in range(2,int(n/2)+1):
            while(n % i == 0):
                sum+=i
                n/=i            
        return sum
t = int(input())
summ = 0
while t>0:
    t-=1
    cout=0
    for i in range(2*10000,2*100000):
        print(phantich(i),end=', ')
        cout+=1
        if cout == 30:
            print()
            cout=0
#     n = int(input())
#     summ += phantich(n)
# print(summ)