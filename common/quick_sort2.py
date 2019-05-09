def quick_sort(lst):
    qsort_rec(lst, 0, len(lst)-1)


def qsort_rec(lst, l, r):
    if l >= r:
        return None
    i = l
    j = r
    pivot = lst[i]  # 从左边开始
    while i < j:
        while i < j and lst[j] >= pivot:    # 右边的值小于pivot的情况
            j -= 1
        if i < j:
            lst[i] = lst[j]     # 将右边值放到左边，同时左边技术坐标 + 1
            i += 1
        while i < j and lst[i] <= pivot:    # 左边的值大于pivot的情况
            i += 1
        if i < j:
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot
    qsort_rec(lst, l, i-1)
    qsort_rec(lst, i+1, r)


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    quick_sort(ret)
    print(ret)
