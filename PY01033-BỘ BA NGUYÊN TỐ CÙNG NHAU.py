from math import gcd

n,m = input().split()
l = int(n)
r = int(m)
for i in range(l,r+1):
    for j in range (i+1,r+1):
        for t in range (j+1,r+1):
            if gcd(i,j)==1 and gcd(j,t)==1 and gcd(i,t)==1:
                print("(",end = "")
                print(i, end = ", ")
                print(j, end = ", ")
                print(t, end = ")\n")
        