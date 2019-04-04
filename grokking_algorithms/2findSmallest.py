# coding: UTF-8
"""
find the smallest in array
"""


def findsmallest (arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


if __name__ == '__main__':
    print(findsmallest(['5', '3', '4', '5', '7']))
