def quick_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)
    return array


def partition(array, left, right):
    pivot = array[right]    # 选择最后一个数作为枢纽元
    location = left - 1    # 指向比 x 小的元素段的尾部
    for i in range(left, right):
        if array[i] <= pivot:
            location += 1
            array[location], array[i] = array[i], array[location]
    array[location + 1], array[right] = array[right], array[location + 1]
    return location + 1


if __name__ == '__main__':
    array2 = [9, 3, 2, 1, 4, 6, 7, 0, 5]
    array3 = [5, 7, 1, 1, 5, 4, 3]
    print(quick_sort(array2, 0, len(array2)-1))
    print(partition(array3, 0, 6))
