n = int(input())
a = [int(x) for x in input().split()]
cout=0
for i in range(n):
    for j in range (i+1,n):
        if a[i] > a[j]:
           cout+=1 
print(cout)