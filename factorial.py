from math import factorial

print("WELCOME THE FINDING FACTORIAL PROGRAM\n\n\n press the q to exit program")

while True:
    your_count=input("please,enter the count:")
    if(your_count=="q"):
        print("exiting the program...")
        break
    else:
        your_count=int(your_count)
        facto=1
    for i in range(2,your_count+1):
        facto*=i
    print("factorial:",facto)