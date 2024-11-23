"""
transferring the just 3-dividend numbers coming 1-100 numbers to the list.
"""

emptylist=[]
for i in range(1,101):
    if i%2==0:
        emptylist.append(i)
print(emptylist)

"""
ı learned after ı developed above that this is the most efficient algorithm.
list= [x for x in range(1,101) if x % 2 == 0]
print(list)
"""