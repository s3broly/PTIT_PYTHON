s1 = input()
s2=""
cout=0
l = len(s1) - 1
while True:
    cout+=1
    s2 = s1[l] + s2
    if l == 0 : break
    if cout == 3:
        s2 = ',' + s2
        cout=0
    l-=1
print(s2)