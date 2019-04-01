def print_max(x,y):
    '''print the maximum of two number打印。

    the two values must be integers'''
    # conver to integers
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y,'is maximum')

print_max(4,6)
print(print_max.__doc__)
help(print_max)