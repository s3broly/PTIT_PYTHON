import math
t = int(input())
while t:
    t-=1
    n,x,m = input().split()
    res = float(m)/float(n)
    nm = math.log(res)/math.log(1+(float(x)/100))
    if(nm == int(nm)):
        print(int(nm))
    else:
        print(int(nm)+1)
            