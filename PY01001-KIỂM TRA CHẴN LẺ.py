
def check_odd_even(n):
    flag = 1
    if( n % 2 == 0):
        flag= 0
    return flag;  


n = int(input())


check = check_odd_even(n)
 
if check == 1:
    print("LE")
else:
    print("CHAN")
