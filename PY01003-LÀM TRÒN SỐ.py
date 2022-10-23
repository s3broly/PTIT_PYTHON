t = int(input())
while t>0:
    t-=1
    s = input()
    z = ""
    ok = 1
    for i in range(1, len(s)) :
        z = z + "0"
        if ok == 0 :
            if int(s[-i]) > 3 :
                ok = 0
            else :
                ok = 1
        else :
            if int(s[-i]) > 4 :
                ok = 0
            else :
                ok = 1
    if ok == 0 :
        if int(s[0]) == 9 :
            z += "0"
            z = "1" + z
        else :
            z = chr(ord(s[0]) + 1) + z
    else : z = s[0] + z
    print(z)