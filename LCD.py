"""
 LEAST COMMON DIVISOR ALGORITHM
"""
def L_C_D(num1,num2):
    i=2
    lcd=1
    while True:
        if(num1%i==0 and num2%i==0 ):
            lcd*=i
            num1//=i
            num2//=i
        elif(num1%i==0 and num2%i!=0):
            lcd*=i
            num1//=i
        elif(num1!=0 and num2%i==0):
            lcd*=i
            num2//=i
        else:
            i+=1

        if(num1==1 and num2==1):
            break
    return lcd

num1=int(input("num1:"))
num2=int(input("num2:"))

print("lcd:",L_C_D(num1,num2))