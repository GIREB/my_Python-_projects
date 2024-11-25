"""
Greatest Common Divisor Algorithm using function...
ı researched the most efficient algorithm for finding GCD,I found the Euclidean Algorithm.
This algorithm is on the principle that the GCD of two numbers also divides their difference.
"""

def G_C_D(mynumber1,mynumber2):
    if(mynumber1<mynumber2):
        mynumber1,mynumber2=mynumber2,mynumber1
    while (mynumber2 != 0):
        remainder = mynumber1 % mynumber2
        mynumber1 = mynumber2
        mynumber2 = remainder
    return mynumber1

while True:
    mynumber1 = int(input("please enter the first number(or type '0' to quit: "))
    mynumber2 = int(input("please enter the second number: "))

    if(mynumber1==0 or mynumber2==0):
        print("exiting program...")

    gcd=G_C_D(mynumber1,mynumber2)
    print("the GCD of {} and {} is: {}".format(mynumber1,mynumber2,gcd))

