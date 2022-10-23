t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    print("Test ",i+1,": ",sep='',end='')
    if len(s1) != len(s2):
        print("NO")
    else:
        if sorted(s1) == sorted(s2):
            print("YES")
        else:
            print("NO") 