n = int(input())
a = [float(x) for x in input().split()]
s = 0
c = []
for i in range(n):
    if a[i] != min(a) and a[i] != max(a):
        s = s + float(a[i])
        c = c+[a[i]]
print('%.2f' % float(s/(len(c))))