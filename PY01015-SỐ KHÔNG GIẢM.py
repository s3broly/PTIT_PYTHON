t = int(input())
while t>0:
    t-=1
    s = input()
    l = len(s)
    cout=0
    for i in range(1,l):
        if(s[i]>=s[i-1]):
            cout+=1
    if(cout == l-1):
        print("YES")
    else:
        print("NO")