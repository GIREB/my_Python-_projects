
print("WELCOME TO THE ATM MACHINE...\n\nOperations:\n\n1)Balance inquiry\n\n2)Deposite money\n\n3)withdrawal\n\nto exit the program press the q")

balance=1000

while True:
    operation2=input("please choose the operation you want to do")
    if(operation2=="q"):
        print("see you later again!")
        break
    elif(operation2=="1"):
        print("your balance is:{}".format(balance))
    elif(operation2=="2"):
        amount=int(input("please,enter the amount of money you want to deposite"))
        balance+=amount
    elif(operation2=="3"):
        amount=int(input("please,enter the amount of money that you want to withdraw"))
        if(amount>balance):
            print("you can't withdraw money")
            continue
        balance-=amount
    else:
        print("invalid operation!")
