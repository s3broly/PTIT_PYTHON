def inra(n,m):
    for i in range(0,m):
        print(n,end="")
t = int(input())
while t>0:
    t-=1
    s = input()
    l = len(s)
    for i in range(0,l):
        if(i%2==1):
            inra(s[i-1],int(s[i]))
    print(end="\n")