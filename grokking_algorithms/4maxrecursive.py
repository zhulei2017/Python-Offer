def maxrecursive(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > maxrecursive(arr[1:]):
            return arr[0]
        else:
            return maxrecursive(arr[1:])


print(maxrecursive([1, 123123, 6, 4]))
