n = int(input())
a = [int(x) for x in input().split()]
cout=0
for i in range(n):
    if a[i]!=a[i-1]:
        cout+=1
print(cout)