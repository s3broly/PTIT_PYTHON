def tichcs(n):
    s=1
    for i in n:
        if i!='0':
            s = s*int(i)   
    return s 
t = int(input())
while t>0:
    t-=1
    n = input()
    s = tichcs(n)
    print(s)
    