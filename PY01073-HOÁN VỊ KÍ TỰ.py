n = input()
l = len(n)
a = [0] * l
def Try(s,k):
    if k == l:
        print(s)
    for i in range(l):
        if a[i] == 0:
            a[i]=1
            Try(s+n[i],k+1)
            a[i]=0            
Try("",0) 