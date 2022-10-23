t = int(input())
while t>0:
    t-=1
    s1=input()
    s2=""
    l = len(s1)
    k=1
    for i in s1:
            s2 = i + s2
    for i in range(1,l):    
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            k=0
    if k==1:
        print("YES")
    else:
        print("NO")