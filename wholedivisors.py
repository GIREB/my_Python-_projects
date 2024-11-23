def whole_divisors(number):
    wholedivs=[]

    for i in range(2,number):
        if(number%i==0):
            wholedivs.append(i)
    return wholedivs

while True:
    number=input("number:")

    if(number=="q"):
        print("exiting...")
        break
    else:
        number=int(number)
        print("whole divisors:",whole_divisors(number))