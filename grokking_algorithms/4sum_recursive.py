def sumrecursive(arr):
    if arr == []:
        return 0
    return arr[0] + sumrecursive(arr[1:])


print(sumrecursive([1, 2, 3, 4]))
