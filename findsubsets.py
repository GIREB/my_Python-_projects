"""
this algorithm can find subsets that given from sets using recursive function.
"""
def find_Subsets(s):
    if(len(s)==0):
        return [[]]
    subsets=find_Subsets(s[:-1])
    return subsets+[subset+[s[-1]] for subset in subsets]
while True:
    s=input("enter set comma separated:")
    user_list=s.split(",")
    subsets=find_Subsets(user_list)
    print("subsets:",subsets)

