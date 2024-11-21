"""
for instance,think the 4-digit number,if the number equals the sum of digit's exponents separately, this number named armstrong number.
"""
import math
print("WELCOME THE POSITIVE ARMSTRONG CONTROL ALGORITHM\n\n\nthis algorithm can control the until 5 digits number.")
while True:
    number1=int(input("please,enter the number that you want to learn the number is the armstrong or not"))
    original_num=number1

    num_of_digits= len(str(number1))
    print("number of digits:",num_of_digits)

    digits=[]
    while(number1>0):
        digit=number1%10
        digits.append(digit)
        number1//=10
    digits.reverse()
    print("digits:",digits)

    sum_of_digits=0
    for digit in digits:
        result=pow(digit,num_of_digits)
        sum_of_digits+=result

    print("sum of digits raised to the power:",int(sum_of_digits))

    if(int(sum_of_digits==original_num)):
        print("the number is an armstrong\n")
    else:
        print("the number is not an armstrong number")

