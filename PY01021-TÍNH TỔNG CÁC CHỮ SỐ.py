t = int(input())
while t>0:
    t-=1
    n = input()
    sum=0
    s = ''
    for i in n :
        if i.isdigit():
            sum+=int(i)
        else : 
            s = s + i
    print(''.join(sorted(s)),sum,sep='')
    