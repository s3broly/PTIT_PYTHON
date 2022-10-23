from math import gcd


a,b = input().split()
n = int(a)
k = int(b)
s = pow(10,k)
r = pow(10,k-1)
cout = 0
for i in range (r,s):
    if gcd(n,i)==1:
        print(i,end=" ")
        cout+=1
    if cout ==10:
        print()
        cout=0