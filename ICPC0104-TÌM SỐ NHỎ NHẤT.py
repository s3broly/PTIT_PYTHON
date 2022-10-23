t = int(input())
while t>0:
    t-=1
    n = input()
    n = n + 'z'
    ans = 10**18
    s = 0
    for i in range(0,len(n)) :
        if n[i].isalpha() :
            if i != 0 and n[i - 1].isdigit() : 
                ans = min(ans, s)
            s = 0
        else : 
            s = s * 10 + int(n[i])
    print(ans)
    