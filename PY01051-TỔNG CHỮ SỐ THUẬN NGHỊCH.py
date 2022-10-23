def tongcs(n):
    s=0
    for i in n :
        s += int(i)
    return s 
t = int(input())
while t>0:
    t-=1
    n = input()
    s = tongcs(n)
    g = int(str(s)[::-1])
    if s>10 and s==g:
        print("YES")
    else:
        print("NO")
    