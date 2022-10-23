def sum(n):
    s = 0
    for i in n : 
        s += ord(i) - ord('0')
    return str(s)
n = input()
cout=0
if int(n) < 10 and int(n) > -10:
    print(cout+1)
else:
    while (len(n)>1):
        n = sum(n)
        cout+=1
    print(cout)    