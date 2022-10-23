s = input()
t=0
h=0
for i in s:
    if i>='a' and i<='z':
        t+=1
    else:
        h+=1
if t>=h:
    print(s.lower())
else:
    print(s.upper())
    