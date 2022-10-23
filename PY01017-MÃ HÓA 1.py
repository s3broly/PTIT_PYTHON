t = int(input())
while t>0:
    t-=1
    s = input()
    l = len(s)
    k = 1
    for i in range(1, l) :
        if s[i] != s[i - 1] :
            print(k,end = "")
            print(s[i - 1],end = "")
            k = 1
        else: 
            k += 1
    print(k,end="")
    print(s[l - 1])