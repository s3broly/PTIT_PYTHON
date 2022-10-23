def gt(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s
t = int(input())
for i in range(t):
    sum = 0
    n = input()
    for i in n:
        sum = sum + gt(int(i))
    if int(n)==sum:
        print("Yes")
    else:
        print("No") 