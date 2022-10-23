class Rectangle :
    def __init__(r, w, h, color) :
        r.w = w
        r.h = h
        r.colorr = color[0:1:].upper() + color[1::].lower()
    def check(r) :
        if r.w <= 0 or r.h <=0 : return False
        return True    
    def perimeter(r):
        return (r.w + r.h) * 2
    def area(r):
        return r.w * r.h
    def color(r):
        return r.colorr
    def output(r) :
        if r.check() == 1 : print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        else : print('INVALID')
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
r.output()