def quicksort(array):
    if len(array) < 2:
        return array  # base only one element
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i >= pivot]
        array_sort = quicksort(less) + [pivot] + quicksort(greater)
        return array_sort


arr = [2, 5, 1, 2, 2, 6, 8, 10]
print(quicksort(arr))
