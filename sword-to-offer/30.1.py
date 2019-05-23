def get_least_numbers(lst, k):
    if lst is None or k > len(lst) or k <= 0:
        return
    start = 0
    end = len(lst)-1
    index = partition(lst, start, end)
    while index != k-1:
        if index > k-1:
            end = index-1
            index = partition(lst, start, end)
        else:
            start = index+1
            index = partition(lst, start, end)
    print(lst)
    return lst[0:k]


def partition(array, left, right):
    pivot = array[right]
    location = left-1
    for i in range(left, right):
        if array[i] < pivot:
            location += 1
            array[location], array[i] = array[i], array[location]
    array[location+1], array[right] = array[right], array[location+1]
    return location+1


if __name__ == "__main__":
    array2 = [9, 3, 2, 1, 4, 6, 7, 0, 5]
    print(get_least_numbers(array2, 4))
