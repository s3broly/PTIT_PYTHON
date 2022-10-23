t = int(input())
while t>0:
    t-=1
    n = input()
    cout=0
    l = len(n)
    for i in range(0,l):
        if int(n[i]) == int(n[i-2]):
            cout+=1
    if l%2==0:
        if cout==l:
            print("YES")
        else:
            print("NO")    
    else:
        if cout==l-2:
            print("YES")
        else:
            print("NO")       
    