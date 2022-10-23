t = int(input())
while t>0:
    t-=1
    s = input()
    cout=0
    for i in s:
        if i !='0' and i !='1' and i !='2':
            cout=1
    if cout == 0  :
        print("YES")
    else:
        print("NO")
         
    