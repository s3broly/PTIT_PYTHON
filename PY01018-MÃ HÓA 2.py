P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True :
    l = input()
    n = ""
    if l == "0":
        break
    k,s= l.split()
    for i in s:
        x = 0
        for j in P:
            if i==j:
                break
            x+=1
        x = (x+int(k))%28
        n = P[x] + n
    print(n)