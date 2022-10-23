t = int(input())
while t>0:
    t-=1
    n = input()
    s = 0
    if int(n)%2 == 0:
        for i in range(2,int(n)+1,2):
            s = s + 1/int(i)
        print('%.6f' % s)

    else:
        for i in range(1,int(n)+1,2):
            s = s + 1/int(i)
        print('%.6f' % s)
