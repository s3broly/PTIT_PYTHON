n = input()
l = len(n)
if(int(n[0]) + int(n[4]) == int(n[l-1])):
    print("YES")
else:
    print("NO")