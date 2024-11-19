#finding the roof of a quadratic equation with one unknown
#equation: ax^2 + bx + c

#1.roof: (-b-delta**0.5)/(2*a)
#2.roof: (-b+delta**0.5)/(2*a)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta=b**2-4*a*c

x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

print("1.roof:{}\n,2.roof:{}\n".format(x1,x2))
