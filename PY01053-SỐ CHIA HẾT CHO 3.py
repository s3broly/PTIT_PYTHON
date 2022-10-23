def tongcs(n):
    s=0
    for i in n:
        s += int(i)
    return s 
t = int(input())
while t>0:
    t-=1
    n = input()
    s = tongcs(n)
    if s%3==0:
        print("YES")
    else:
        print("NO")
    
    