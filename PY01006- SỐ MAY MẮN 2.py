t = int(input())
while t:
    t-=1
    n = input()
    d=0
    for i in n:
        if i!='4' and i!='7':
            d+=1
    if(d==0):
        print("YES")
    else:
        print("NO")
