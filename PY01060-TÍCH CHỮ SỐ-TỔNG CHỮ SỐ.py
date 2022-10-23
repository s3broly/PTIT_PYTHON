t = int(input())
while t>0:
    t-=1
    n = input()
    s1 = 0
    for i in range(0,len(n)):
        if i%2 != 0:
            s1+=int(n[i])
    s2 = 1
    ck = 0
    for i in range(0,len(n)):
        if i%2 == 0:
            if int(n[i]) != 0:
                ck=1
                s2 = s2*int(n[i])
    if ck == 0: s2=0
    print(s2,s1)