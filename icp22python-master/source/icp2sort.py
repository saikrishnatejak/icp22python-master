def longest(val):
    list1=[]
    for x in val:
        list1.append((len(x),x))
    list1.sort()
    return list1[-1]
print(longest(["sharath","madhukar","vinneth12345"]))