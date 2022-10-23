a,k,n = input().split()
res = int(a)
cout = int(k)
m = int(n)
b = cout - res % cout + res
ok = 0
for i in range(b, m + 1, cout) :
    ok = 1
    print(i - res, end = " ")
if ok == 0 : print("-1")
