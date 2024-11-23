sum_of_numbs=0
while True:
    numb=int(input("please enter the number..."))
    if(numb=="q"):
        break
    numb=int(numb)

    sum_of_numbs+=numb
    print("sum of nums you entered:",sum_of_numbs)
