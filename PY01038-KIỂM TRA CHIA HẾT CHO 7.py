def check(n):
    if int(n)%7==0:
        return False
    return True

t = int(input())
while t>0:
    t-=1
    n = int(input())
    cout=0
    while check(n):
        n = n + int(str(n)[::-1])
        cout+=1
        if cout == 1001:
            print("-1")
            break
    print(n)