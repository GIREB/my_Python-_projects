"""
if the number equals the sum of divisors and itself except itself,this number names a perfect number.
"""
while True:
 number = int(input("please,enter the number that you want to learn whether this number is perfect or not..."))
 divisor_sum = 0
 for i in range(1,number):
    if(number%i==0):
        print("divisors we need:",i)
        divisor_sum+=i
 if(number==divisor_sum):
    print("the number is perfect!")
    break
 else:
    print("the number is not perfect!")
    break
