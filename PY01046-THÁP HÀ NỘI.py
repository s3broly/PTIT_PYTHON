def chuyen(n,a,b):
    print(a + " -> "+ b)
def thapHN(n,a,b,c):
	if(n==1):
		chuyen(1,a,c)
	else:
		thapHN(n-1,a,c,b)
		chuyen(n,a,c)
		thapHN(n-1,b,a,c)

n = int(input())
a='A'
b='B'
c='C'
thapHN(n,a,b,c)
