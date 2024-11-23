"""this algorithm covers the times table from 1 to 10."""
for i in range(1,11):
    for j in range(1, 11):
        print("{} times {}={}".format(i,j,i*j))
    print("-" * 20)