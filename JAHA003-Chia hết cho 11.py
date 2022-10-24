def cnt(n):
    s = str(n)
    s1 = 0
    s2 = 0
    for i in range(len(s)):
        if i % 2 == 0 :
            s1+=int(s[i])
        else:
            s2+=int(s[i])        
    return abs(s1-s2)
t = int(input())
for x in range(t):
    n = int(input())
    if cnt(n)%11==0:
        print("YES")
    else:
        print("NO")