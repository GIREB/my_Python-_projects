"""
algorithm that finds the pronunciation of the numbers.
"""

ones=["","one","two","three","four","five","six","seven","eight","nine"]
tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def pronunciation(num):
    first=num%10
    second=num//10

    return tens[second]+""+ones[first]

num=int(input("num:"))
print(pronunciation(num))