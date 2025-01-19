import random
import time
print("WELCOME THE GUESS NUMBER GAME!\nguess the number between 1-40\n")

myrandomnumber=random.randint(1,40)
rightofprediciton=5
print("your right of prediction:",rightofprediciton)

while True:
    prediciton=int(input("prediction:"))
    if(prediciton<myrandomnumber):
        print("informations are controlling...")
        time.sleep(2)
        print("please,say number is more than yours")
        rightofprediciton-=1
    elif(prediciton>myrandomnumber):
        print("informations are controlling...")
        time.sleep(2)
        print("please,say number is less than yours")
        rightofprediciton -= 1
    else:
        print("informations are controlling...")
        time.sleep(2)
        print("Congratulations!\nnumber:",myrandomnumber)
        break
    if(rightofprediciton==0):
        print("You are out of predictions.")
        print("number:",myrandomnumber)
        break
