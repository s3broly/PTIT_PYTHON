while True:
    n = int(input())
    if n==0:
        break
    cout=1
    while n!=1:
        if n%2==0:
            n = n/2
            cout+=1
        elif n%2!=0:
            n = n*3+1
            cout+=1     
    if n==1:
        print(cout)
                