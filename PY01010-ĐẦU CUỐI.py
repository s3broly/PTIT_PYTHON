t = int(input())
while t>0:
    t-=1
    s = input()
    n = len(s)
    if(s[n-1] == s[1] and s[n-2] == s[0]):
        print("YES")
    else:
        print("NO")