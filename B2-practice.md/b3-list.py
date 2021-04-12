def large_number(items):
    max=0
    for i in items:
        if i>max:
            max=i;
    return max
print(large_number([1,2,3,4,8,2]))

