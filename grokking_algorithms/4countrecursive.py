def countrecursive(arr):
    if arr == []:
        return 0
    return 1 + countrecursive(arr[1:])


print(countrecursive(['a', 'bsadasd', 'c']))