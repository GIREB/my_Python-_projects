"""
Q:write a Python program to print the reverse of a given string.
"""
###slicing method
original_string=input("please,enter string wants to reverse:")
reverse_string=original_string[::-1]
print("reverse string:",reverse_string)
"""
###reversed function method
secoriginal_string=input("please,enter string wants to reverse:")
reverse_string="".join(reversed(secoriginal_string))
print("reversed string:",reverse_string)
"""