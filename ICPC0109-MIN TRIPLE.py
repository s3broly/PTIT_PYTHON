t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = min(a)
    s= a[0]+a[1]+a[2]
    for i in range(0,len(a)):
        temp1 = a[i]
        if a[i] != ans:
            for j in range(i+1,len(a)):
                if a[j] != ans:
                    temp2 = temp1 + a[j] +ans
                    if temp2 <= s:
                        s = temp2
    print(s)   
          
      
    