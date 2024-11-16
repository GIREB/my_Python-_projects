print("""********************
calculator program

1. Add

2. Substraction

3.Multiplication

4.Division
********************
""")
a=int(input("first number:"))
b=int(input("second number:"))

operation=input("enter the operation...")

if operation=="1":
    print("{} + {}={} ".format(a,b,a+b))
elif operation=="2":
    print("{} - {}={} ".format(a, b, a - b))
elif operation=="3":
    print("{} * {}={} ".format(a, b, a * b))
elif operation=="4":
    print("{} / {}={} ".format(a, b, a / b))
else:
    print("invalid operation!!!")