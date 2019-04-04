# coding: UTF-8
"""
order the array
"""


def findsmallest (arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        print('it is {} times'.format(i))
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newarr = []
    for i in list(range(len(arr))):
        smallest_index = findsmallest(arr)
        newarr.append(arr.pop(smallest_index))
    return newarr


aa = [512, 23, 423, 151, 712]
print(findsmallest(aa))
print(selectionsort(aa))
