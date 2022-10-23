t = int(input())
for i in range(t):
    a,b = input().split()
    d = int(a)
    m = int(b)
    if m==1:
        if d <=19:
            print("Ma Ket") 
        elif d>19 and d<=31:
            print("Bao Binh")
    if m==2:
        if d <= 18:
            print("Bao Binh") 
        elif d>18 and d<=29:
            print("Song Ngu")
    if m==3:
        if d <= 20:
            print("Song Ngu") 
        elif d>20 and d<=31:
            print("Bach Duong")
    if m==4:
        if d <= 19:
            print("Bach Duong") 
        elif d>19 and d<=30:
            print("Kim Nguu")
    if m==5:
        if d <= 20:
            print("Kim Nguu") 
        elif d>20 and d<=31:
            print("Song Tu")
    if m==6:
        if d <= 20:
            print("Song Tu") 
        elif d>20 and d<=31:
            print("Cu Giai")
    if m==7:
        if d <= 22:
            print("Cu Giai") 
        elif d>22 and d<=31:
            print("Su Tu")
    if m==8:
        if d <= 22:
            print("Su Tu") 
        elif d>22 and d<=31:
            print("Xu Nu")
    if m==9:
        if d <= 22:
            print("Xu Nu") 
        elif d>22 and d<=31:
            print("Thien Binh")        
    if m==10:
        if d <= 22:
            print("Thien Binh") 
        elif d>22 and d<=31:
            print("Thien Yet")
    if m==11:
        if d <= 22:
            print("Thien Yet") 
        elif d>22 and d<=31:
            print("Nhan Ma")
    if m==12:
        if d <= 21:
            print("Nhan Ma") 
        elif d>21 and d<=31:
            print("Ma Ket")