"""
fibonacci series create the new number as sum of previous two number.
"""
a=1
b=1

fibonacci=[a,b]

for i in range(20):
    a,b=b,a+b
    fibonacci.append(b)

print(fibonacci)
