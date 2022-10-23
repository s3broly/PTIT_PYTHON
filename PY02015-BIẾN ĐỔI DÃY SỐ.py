o = [0]*4
def Try(a,res):
    if n[0]==n[1]==n[2]==n[3]: return res
    else:
        x = n[0] ; y = n[1]
        z = n[2] ; t = n[3]
        n[0] = abs(x-y) ; n[1] = abs(y-z)
        n[2] = abs(z-t) ; n[3] = abs(x-t)
        return Try(n, res+1)
while True:
    n = [int(i) for i in input().split()]
    if n == o:
        break
    print(Try(n,0))
    