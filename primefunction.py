def Is_Prime(number):
    if(number==1):
        return False
    elif(number==2):
        return True
    else:
        for i in range(2,number):
            if(number%i==0):
                return False
        return True

while True:
    number=input("number:")
    if(number=="q"):
        break
    else:
        number=int(number)
        if(Is_Prime(number)):
            print(number,"is prime")
        else:
            print(number,"is not prime")
