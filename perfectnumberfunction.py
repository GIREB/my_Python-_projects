"""
if the number equals the sum of divisors and itself except itself,this number names a perfect number.
control algorithm that controls the number is perfect or not between 1-1000
"""
def Is_Perfect(number):
    sum_divisors=0
    for i in range(1,number):
        if(number%i==0):
            sum_divisors+=i

    return sum_divisors==number

for i in range(1,1001):
    if(Is_Perfect(i)):
        print("perfect number:",i)
